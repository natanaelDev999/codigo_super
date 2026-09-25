import math
import LibraryVectorNatan as lvt

tela = []


esfera = [[0,0,3,6]]

y_tela = 9
x_tela = 16

raios = []

#camera
viewport_h = 2.0
viewport_w = viewport_h * (x_tela/y_tela)
focal_l = 1.0
camera_center = [0,0,0]

viewport_u = [viewport_w,0,0]
viewport_v = [0, -viewport_h, 0]

pixel_delta_u = lvt.divide_vetores(viewport_u, [y_tela,y_tela,y_tela])
pixel_delta_v = lvt.divide_vetores(viewport_v, [x_tela,x_tela,x_tela])

viewport_upper_left = lvt.subtrai_vetores(
                        lvt.subtrai_vetores(
                        lvt.subtrai_vetores(camera_center,
                 [0,0,focal_l]),
                        lvt.divide_vetores(viewport_u,
                  [2,2,2])),
                        lvt.divide_vetores(viewport_v,[2,2,2]))
pixel00_loc = lvt.multiplica_vetores(
    lvt.soma_vetores(viewport_upper_left,[0.5,0.5,0.5]),
    lvt.soma_vetores(pixel_delta_u,pixel_delta_v)
    )

def renderRayTracing():
    global y_tela,x_tela,tela
    for c in range(0,y_tela):
        for v in range(0,x_tela):
            pixel_c = lvt.soma_vetores(lvt.soma_vetores(pixel00_loc,
                                       lvt.multiplica_vetores(
                                           [v,v,v],pixel_delta_u)),
                                       lvt.multiplica_vetores([c,c,c],pixel_delta_v))
            direcao = lvt.subtrai_vetores(pixel_c,camera_center)
            print(f'\033[38;2;{0};{0};{c*30}m#\033[m',end=' ')
        print()

def at(orig,t,dir):
    return orig + t*dir
def main():
    renderRayTracing()
main()