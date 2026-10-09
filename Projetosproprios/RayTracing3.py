import LibraryVectorNatan as lvt
import sys
import time

esferas = [[[2,0,3],0.5,[0,255,0]],[[0,0,2],0.5,[255,0,0]],[[0.5,0,1],0.5,[0,0,255]]]

y_tela = 36
x_tela = 104

#camera
viewport_h = 2.0
viewport_w = viewport_h * (x_tela/y_tela)
focal_l = 1.0
camera_center = [0,0,0]

viewport_u = [viewport_w,0,0]
viewport_v = [0, -viewport_h, 0]

pixel_delta_u = lvt.divide_vetores(viewport_u, [x_tela,x_tela,x_tela])
pixel_delta_v = lvt.divide_vetores(viewport_v, [y_tela,y_tela,y_tela])

viewport_upper_left = lvt.subtrai_vetores(
                        lvt.subtrai_vetores(
                        lvt.subtrai_vetores(camera_center,
                 [0,0,focal_l]),
                        lvt.divide_vetores(viewport_u,
                  [2,2,2])),
                        lvt.divide_vetores(viewport_v,[2,2,2]))

pixel00_loc = lvt.soma_vetores(viewport_upper_left,
                               lvt.multiplica_vetores([0.5,0.5,0.5],
                               lvt.soma_vetores(pixel_delta_u,
                                                pixel_delta_v)
                                                      ))

def renderRayTracing():
    global y_tela,x_tela,tela,esferas
    for c in range(0,y_tela):
        for v in range(0,x_tela):
            pixel_c = lvt.soma_vetores(lvt.soma_vetores(pixel00_loc,
                                       lvt.multiplica_vetores(
                                           [v,v,v],pixel_delta_u)),
                                       lvt.multiplica_vetores([c,c,c],pixel_delta_v))
            direcao = lvt.subtrai_vetores(pixel_c,camera_center)
            raio = [camera_center,direcao]

            x = at(raio[0][0],1,camera_center[0]-raio[1][0])
            y = at(raio[0][1],1,camera_center[1]-raio[1][1])
            z = at(raio[0][2],1,camera_center[2]-raio[1][2])

            cor = [0,0,0]
            # for j in esferas:
            #      if hit_sphere(j[0],j[1],[camera_center,[x,y,z]]) == True:
            #          cor = j[2]
            if hit_quad(raio,[-0.5,-0.5,1],[0.5,0.5,1.5]):
                 cor = [255,0,0]
            print(f'\033[38;2;{cor[0]};{cor[1]};{cor[2]}m#\033[m',end=' ')
        print()

def at(orig,t,dir):
    return orig + t*dir

def hit_quad(raio, c_min , c_max):
    t = False
    for c in range(0,3):
        # para o x
        if round(raio[1][0]+raio[1][0]) >= c_min[0] and round(raio[1][0]+raio[1][0]) <= c_max[0]:
            t = True

        # para o y
        if round(raio[1][1]+raio[1][1]) >= c_min[1] and round(raio[1][1]+raio[1][1]) <= c_max[1]:
            t = True
        else:
            t = False

        # para o z
        if round(raio[1][2]+raio[1][2]) >= c_min[2] and round(raio[1][2]+raio[1][2]) <= c_max[2]:
            t = True

    return t

def hit_cube(raio,c_min,c_max):
    t_x1 = (c_min[0]-raio[0][0]) * 1./ raio[1][0]
    t_x2 = (c_max[0]-raio[0][0]) * 1./ raio[1][0]

    tmin = min(t_x1,t_x2)
    tmax = max(t_x1,t_x2)

    t_y1 = (c_min[1] - raio[0][1]) * 1. / raio[1][1]
    t_y2 = (c_max[1] - raio[0][1]) * 1. / raio[1][1]

    tmin = max(tmin,min(t_y1,t_y2))
    tmax = min(tmax,max(t_y1,t_y2))

    t_z1 = (c_min[2] - raio[0][2]) * 1. / raio[1][2]
    t_z2 = (c_max[2] - raio[0][2]) * 1. / raio[1][2]

    tmin = max(tmin,min(t_z1,t_z2))
    tmax = min(tmax, max(t_z1,t_z2))

    return tmax >= min(tmin,0.) and tmin <= 10

def hit_sphere(center,radius,ray):
    oc = lvt.subtrai_vetores(center,ray[0])
    a = lvt.produto_escalar3(ray[1],ray[1])
    b = -2.0*lvt.produto_escalar3(ray[1],oc)
    c = lvt.produto_escalar3(oc,oc) - radius*radius
    discriminate = b*b - 4*a*c
    return discriminate >= 0
def main():
    while True:
        renderRayTracing()
        time.sleep(0.016)
        sys.stdout.write('\033[H')
        sys.stdout.flush()
main()