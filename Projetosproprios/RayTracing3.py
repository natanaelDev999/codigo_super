import LibraryVectorNatan as lvt

tela = []


esferas = [[[0.5,0,1],0.5,[0,0,255]],[[0,0,2],0.5,[255,0,0]],[[2,0,3],0.5,[0,255,0]]]

y_tela = 9
x_tela = 16

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

def hit_sphere(center,radius,ray):
    oc = lvt.subtrai_vetores(center,ray[0])
    a = lvt.produto_escalar3(ray[1],ray[1])
    b = -2.0*lvt.produto_escalar3(ray[1],oc)
    c = lvt.produto_escalar3(oc,oc) - radius*radius
    discriminate = b*b - 4*a*c
    return discriminate >= 0

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

            cor = [0,0,0]
            for j in esferas:
                if hit_sphere(j[0],j[1],raio) == True:
                    cor = j[2]
                    break
            print(f'\033[38;2;{cor[0]};{cor[1]};{cor[2]}m#\033[m',end=' ')
        print()

def at(orig,t,dir):
    return orig + t*dir
def main():
    renderRayTracing()
main()