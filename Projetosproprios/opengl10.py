import os
import glfw
import math
import time
import random
from OpenGL.GL import *
from OpenGL.GLU import *

estr = sorted([[-1400000,40,-84000,25012,[random.randint(25,50)/10,random.randint(25,50)/10,0]]])

iten = sorted([[random.randint(19000, 39000), random.randint(-10, 20),640000,
         random.randint(9012, 15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
         random.randint(0,50)],

        [random.randint(-3200, 3000), random.randint(-10, 20), 840000,
         random.randint(9012, 15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
         random.randint(0,50)],

        [random.randint(-164000,3000), random.randint(-10,10), 1400000,
         random.randint(9012,15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
         random.randint(0,50)],

        [random.randint(5000,6000), random.randint(-10,20),-84000,
         random.randint(9012,15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
         random.randint(0,50)],

        [random.randint(-6500,9000), random.randint(-10,10), -940000,
         random.randint(9012,15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
         random.randint(0,50)]
               ])

sib = ['va','ve','vi','vo','vu','ta','te','ti','to','tu','sa','se','si','so','su','ca','ce','ci','co','cu','vac','vec','voc','c',
       'a','e','i','o','u','tri','tre','la','le','li','lo','lu','tho','the','r']

np = []

sate = []

ship = {'max':20,'nave':'tectel I','pulo espacial':150000,'pulo hypespacial':2000000}

pr_ships = []

x = 0
y = 0
z = -3
angle = 0
mov = False
vel = 1.5
comb = 500.0
cr = 100.0
maxc = 0
cont = []
estpreco = []
hyper = False
maxca = 10

def create_name_planets():
    global np,sib,iten
    for c in iten:
        colonia = random.randint(0,30)
        if colonia <= 20:
            np.append([random.choice(sib)+random.choice(sib)+random.choice(sib),'humanos',random.randint(1,15)])
        else:
            np.append([random.choice(sib)+random.choice(sib)+random.choice(sib),
                       random.choice(['felinos','crustáceos','reptilianos']) +' '+ random.choice(['pretos','amarelos','brancos'])+
                       ' '+random.choice(['encouraçados','lisos','peludos']),random.randint(1,15)])

def create_world():
    global iten,estr
    co = estr[0]
    estr.append([co[0], co[1], co[2] * 50,random.randint(25012,30000),[random.randint(25,50)/10,random.randint(25,50)/10,0]])
    for v in range(random.randint(1,8)):
        y = random.randint(0,50)
        # iten.append([co[0]+random.randint(2000,6000),
        #              co[1]+random.randint(100,250),
        #              co[2] * 100+random.randint(4000,8000),random.randint(9012, 15000),
        #              [random.random(),random.random(),random.random()],
        #              random.randint(900,3000),
        #              float(random.randint(-10,10)),
        #              random.randint(0,50)])
        if y < 25:
            iten.append([co[0]+random.randint(800000,1200000)+v*100,co[1]+random.randint(400,1250)+v*300,co[2] * 50+random.randint(1200000,1800000)+v*100,
             random.randint(9012, 15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
             random.randint(0,50)])
        elif y > 25:
            iten.append([co[0] + -random.randint(800000, 1200000)+v*-100, co[1] + -random.randint(400, 1250)+v*300,
                         co[2] * 50 + -random.randint(1200000, 1800000)+v*-100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])
    estr.append([co[0], co[1], -co[2]*100,random.randint(25012,30000),[random.randint(25,50)/10,random.randint(25,50)/10,0]])
    for v in range(random.randint(1,8)):
        y = random.randint(0,50)
        # iten.append([co[0]+random.randint(2000,6000),
        #              co[1]+random.randint(100,250),
        #              co[2] * 100+random.randint(4000,8000),random.randint(9012, 15000),
        #              [random.random(),random.random(),random.random()],
        #              random.randint(900,3000),
        #              float(random.randint(-10,10)),
        #              random.randint(0,50)])
        if y < 25:
            iten.append([co[0]+random.randint(800000,1200000)+v*100,co[1]+random.randint(400,1250)+v*300,-co[2]*100+random.randint(1200000,1800000)+v*100,
             random.randint(9012, 15000),[random.random(),random.random(),random.random()],random.randint(900,3000),float(random.randint(-10,10)),
             random.randint(0,50)])
        elif y > 25:
            iten.append([co[0] + -random.randint(800000, 1200000)+v*100, co[1] + -random.randint(400, 1250)+v*300,
                         -co[2]*100 + -random.randint(1200000, 1800000)+v*100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])

    estr.append([-co[0] * 3.5, co[1], co[2], random.randint(25012,30000), [random.randint(25, 50) / 10, random.randint(25, 50) / 10, 0]])
    for v in range(random.randint(1, 8)):
        y = random.randint(0, 50)
        # iten.append([co[0]+random.randint(2000,6000),
        #              co[1]+random.randint(100,250),
        #              co[2] * 100+random.randint(4000,8000),random.randint(9012, 15000),
        #              [random.random(),random.random(),random.random()],
        #              random.randint(900,3000),
        #              float(random.randint(-10,10)),
        #              random.randint(0,50)])
        if y < 25:
            iten.append([-co[0] * 3.5 + random.randint(800000, 1200000)+v*100, co[1] + random.randint(400, 1250)+v*300,
                         co[2]+ random.randint(1200000, 1800000)+v*100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])
        elif y > 25:
            iten.append([-co[0] * 3.5 + -random.randint(800000, 1200000)+v*100, co[1] + -random.randint(400, 1250)+v*300,
                         co[2]+ -random.randint(1200000, 1800000)+v*100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])

    estr.append([co[0] * 3.5, co[1], co[2], random.randint(25012,30000), [random.randint(25, 50) / 10, random.randint(25, 50) / 10, 0]])
    for v in range(random.randint(1, 8)):
        y = random.randint(0, 50)
        # iten.append([co[0]+random.randint(2000,6000),
        #              co[1]+random.randint(100,250),
        #              co[2] * 100+random.randint(4000,8000),random.randint(9012, 15000),
        #              [random.random(),random.random(),random.random()],
        #              random.randint(900,3000),
        #              float(random.randint(-10,10)),
        #              random.randint(0,50)])
        if y < 25:
            iten.append([co[0] * 3.5 + random.randint(800000, 1200000)+v*100, co[1] + random.randint(400, 1250)+v*300,
                         co[2] + random.randint(1200000, 1800000)+v*100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])
        elif y > 25:
            iten.append([co[0] * 3.5 + -random.randint(800000, 1200000)+v*100, co[1] + -random.randint(400, 1250)+v*300,
                         co[2] + -random.randint(1200000, 1800000)+v*100,
                         random.randint(9012, 15000), [random.random(), random.random(), random.random()],
                         random.randint(900, 3000), float(random.randint(-10, 10)),
                         random.randint(0, 50)])

def circuferencia(zl):
    vert = []
    for i in range(0, 50):
        ang = 0 + (i / float(50 - 1) * (360 - 0))
        rad = math.radians(ang)
        x2 = (160 * 2) * math.sin(rad)
        y2 = (160 * 2) * math.cos(rad)
        vert.append([x2,y2,zl])
    return vert

def cons():
    global vel,comb,cr,maxc,ship
    print('\033[35m---  CONSOLE  ---\033[m')
    print(f'\033[33mvelocidade:{vel}\033[m')
    print(f'\033[32mcombustível:{comb:.2f}\033[m')
    print(f'\033[34mcréditos:{cr}\033[m')
    print(f'\033[37mcarga/t:{maxc}\033[m')
    print(f'nave:{ship['nave']}')

def estr_colisao():
    global estr,x,y,z
    achou = False
    for c in estr:
        if math.sqrt((c[0]--x)**2+(c[1]--y)**2+(c[2]--z)**2) < c[3]+4000:
            achou = True
    return achou

def sater():
    global sate
    for c in sate:
        c[5] += c[6]

def satec():
    global sate,iten
    for c in iten:
        sate.append([c[0],c[1],c[2],random.randint(800,1600),(random.random(),0.5,0.5),0,
                     random.randint(2,9)/1000])

def crtprc():
    global estpreco,iten
    for c in iten:
        estpreco.append([['comida', random.randint(0, 20), random.randint(3, 9),random.randint(2,5)],
                         ['têxteis', random.randint(0,26), random.randint(15,25),random.randint(10,20)],
                         ['artigos de luxo',random.randint(0,10),random.randint(190,260),random.randint(190,210)],
                         ['artigos médicos',random.randint(0,25),random.randint(20,55),random.randint(20,30)],
                         ['minérios', random.randint(0, 12), random.randint(20, 80),random.randint(15,60)],
                         ['armas',random.randint(0,8),random.randint(100,170),random.randint(90,130)],
                         ['computadores',random.randint(0,25),random.randint(150,230),random.randint(150,200)],
                         ['robôs',random.randint(0,28),random.randint(180,240),random.randint(180,200)],
                         ['computador para pulo hypespacial',random.randint(0,1),random.randint(350,370)]])
# (sate[pos][0]-math.sin(math.radians(anglest))*c[3]*6)
#                      ,sate[pos][1]-math.cos(math.radians(anglest))*c[3],
#                      (sate[pos][2]+math.cos(math.radians(anglest))*c[3]*6))
def sate_colisao():
    global x,y,z,sate
    achou = False
    for pos,c in enumerate(sate):
        if math.sqrt(
                ((c[0]-math.sin(math.radians(c[5]))*iten[pos][3]*6)--x)**2+
                ((c[1]-math.cos(math.radians(c[5]))*iten[pos][3])--y)**2+
                ((c[2]+math.cos(math.radians(c[5]))*iten[pos][3]*6)--z)**2
                ) < c[3]:
            achou = True
    return achou

def preco_ships():
    global iten,pr_ships
    for c in iten:
        pr_ships.append([['tectel II',random.randint(0,4),random.randint(370,420),
                          {'max':20,'nave':'tectel II','pulo espacial':200000,'pulo hypespacial':2800000}],
                         ['tectel III',random.randint(0,4),random.randint(390,430),
                          {'max':25,'nave':'tectel III','pulo espacial':280000,'pulo hypespacial':3000000}],
                         ['cargo tec I',random.randint(0,4),random.randint(380,410),
                          {'max':10,'nave':'cargo tec I','pulo espacial':180000,'pulo hypespacial':1800000}],
                         ['cargo tec II',random.randint(0,4),random.randint(390,430),
                          {'max':13,'nave':'cargo tec II','pulo espacial':190000,'pulo hypespacial':1900000}],
                         ['cargo tec III',random.randint(0,4),random.randint(400,450),
                          {'max':16,'nave':'cargo tec III','pulo espacial':200000,'pulo hypespacial':2500000}]])

def comp(pos):
    global pr_ships,cr,ship,maxca
    while True:
        print(f'\033[31mtodas as naves começadas em cargo aumentam a capacidade\033[m')
        print(f'\033[33mcr:{cr}\033[m')
        for pos,c in enumerate(pr_ships[pos]):
            print(f'\033[34mseção:{pos}\033[m;\033[35mnave:{c[0]}\033[m;\033[33mquantidade:{c[1]}\033[m;\033[32mpreço:{c[2]}\033[m;\033[31mcarga máxima:{c[3]['max']}\033[m;\033[37mpulo espacial:{c[3]['pulo espacial']}\033[m;pulo hypespacial:{c[3]['pulo hypespacial']}')
        p = str(input('Deseja comprar qual nave,(se não NH): '))
        if p.upper() != 'NH':
            for c in pr_ships[pos]:
                if c[0] == p:
                    if cr >= c[2]:
                        cr -= c[2]
                        ship = c[3]
                        if c[0].startswith('cargo'):
                            if c[0].endswith('I'):
                                maxca = 15
                            if c[0].endswith('II'):
                                maxca = 20
                            if c[0].endswith('III'):
                                maxca = 25
                        print(f'\033[32mCOMPRADO, AGORA VOCÊ CONTROLA UMA {ship['nave'].upper()}\033[m')
                        time.sleep(2)
                        break
        else:
            break


def pouso(pos):
    global iten,np,x,y,z,mov,iten,comb,cr
    print(f'\033[35mPouso feito com sucesso\033[m')
    time.sleep(2.5)
    os.system('cls')
    print('\033[33m--- DADOS DO PLANETA ---\033[m')
    print(f'\033[33mtipo do planeta\033[m: {classif(iten[pos][4])}')
    print(f'\033[34mnome do planeta\033[m: {np[pos][0]}')
    print(f'\033[37mraio do planeta\033[m: {iten[pos][3]} km')
    if classif(iten[pos][4]) != 'GASOSO':
        print(f'\033[35mdados de vida\033[m: contém colônias de {np[pos][1]}')
        print(f'\033[31mpopulação\033[m:{np[pos][2]} bi')
    else:
        print('\033[35mdados de vida\033[m: não contém colônias')
    time.sleep(6)
    y2 = str(input('Deseja reabastecer o seu combustível,custo:5,(S/N): ')).upper()
    if y2 == 'S':
        if cr >= 5:
            comb = 500
            cr -= 5
        else:
            print('\033[31mCRÉDITOS INSUFICIENTES PARA REABASTECIMENTO DE COMBUSTÍVEL!\033[m')
    print('\033[33m- - - HANGAR DA BASE COLONIAL - - -\033[m')
    comp(pos)
    mov = False
    if math.sqrt((iten[pos][0]--(x+200))**2+(iten[pos][1]--y)**2+(iten[pos][2]--z)**2) < iten[pos][3]:
        x -= 400
    if math.sqrt((iten[pos][0]--(x-200))**2+(iten[pos][1]--y)**2+(iten[pos][2]--z)**2) < iten[pos][3]:
        x += 400
    os.system('cls')
    cons()

def planeta_colisao():
    global x,y,z,iten,vel
    achou = False
    for pos,c in enumerate(iten):
        if math.sqrt((c[0]--x)**2+(c[1]--y)**2+(c[2]--z)**2) < c[3] and vel > 0.5:
            achou = True
        elif math.sqrt((c[0]--x)**2+(c[1]--y)**2+(c[2]--z)**2) < c[3]+10 and vel == 0.5:
            pouso(pos)
    return achou

def classif(cor):
    resp = ''
    if max(cor) == cor[0]:
        resp = 'ROCHOSO'
    if max(cor) == cor[1]:
        resp = 'TÓXICO'
    if max(cor) == cor[2]:
        resp = 'GELADO'
    if cor[0] > cor[1] and cor[2] > cor[1]:
        resp = 'GASOSO'
    if cor[0] > cor[2] and cor[1] > cor[2]:
        resp = 'ÁRIDO'
    if cor[2] > cor[0] and cor[1] > cor[0]:
        resp = 'MARINHO'
    return resp

def visul_d(pos):
    global np
    print('\033[33m--- DADOS DA ESTAÇÃO ---\033[m')
    print('\033[31mtipo da estação\033[m: revenger')
    print(f'\033[34mnome do planeta\033[m: {np[pos][0]}')
    print(f'\033[37mraio do planeta\033[m: {iten[pos][3]} km')
    print(f'\033[33mtipo do planeta\033[m: {classif(iten[pos][4])}')
    if classif(iten[pos][4]) != 'GASOSO':
        print(f'\033[35mdados de vida\033[m: contém colônias de {np[pos][1]}')
        print(f'\033[31mpopulação\033[m:{np[pos][2]} bi')
    else:
        print('\033[35mdados de vida\033[m: não contém colônias')

def comerc(sell,pos):
    global iten,comb,maxc,cont,cr,x,y,z,mov,hyper
    os.system('cls')
    print(f'\033[35mAcoplação da nave feita com sucesso\033[m')
    time.sleep(2.5)
    os.system('cls')
    visul_d(pos)
    time.sleep(10)
    os.system('cls')
    y2 = str(input('Deseja reabastecer o seu combustível,custo:5,(S/N): ')).upper()
    if y2 == 'S':
        if cr >= 5:
            comb = 500
            cr -= 5
        else:
            print('\033[31mCRÉDITOS INSUFICIENTES PARA REABASTECIMENTO DE COMBUSTÍVEL!\033[m')
    # produto / quant  / preço
    while True:
        print('\033[33m- - - HANGAR DA ESTAÇÃO ESPACIAL - - -\033[m')
        for pos,v in enumerate(cont):
            print(f'Lote:{pos+1};Produto:{v[0]};quantidade:{v[1]}')
        print(f'\033[32mcréditos:{cr}\033[m')
        print('\033[37mProdutos a venda: \033[m')
        for pos, s in enumerate(sell):
            if s[0] != 'computador para pulo hypespacial':
                print(f'{pos + 1}    \033[33mproduto:{s[0]}    \033[35mquant:{s[1]}    \033[32mpreço/c:{s[2]}\033[m    \033[31mpreço/v:{s[3]}\033[m')
            else:
                print(f'{pos + 1}    \033[33mproduto:{s[0]}    \033[35mquant:{s[1]}    \033[32mpreço/c:{s[2]}\033[m')
        desejado = input('Qual produto você deseja(NH se não deseja comprar nada): ').strip()
        if desejado == 'NH':
            x += 200
            mov = False
            os.system('cls')
            cons()
            break
        quant = int(input('Quanto deseja?: '))
        for v in sell:
            if v[0] == desejado and v[1] >= quant and quant > 0 and quant + maxc <= maxca:
                if v[2] * quant < cr and quant <= maxca and maxc < maxca:
                    if 'computador para pulo hypespacial' == desejado and hyper == False:
                        hyper = True
                        v[1] -= quant
                        cr -= v[2] * quant
                        print('\033[32mCOMPRADO!\033[m')
                        time.sleep(1)
                        break
                    else:
                        v[1] -= quant
                        cr -= v[2] * quant
                        maxc += quant
                        cont.append([v[0], quant])
                        print('\033[32mCOMPRADO!\033[m')
                        time.sleep(1)
                        break
        os.system('cls')
        #VENDA
        print('\033[33m- - - HANGAR DA ESTAÇÃO ESPACIAL - - -\033[m')
        for pos,v in enumerate(cont):
            print(f'Lote:{pos+1};Produto:{v[0]};quantidade:{v[1]}')
        print(f'\033[32mcréditos:{cr}\033[m')
        desejado = input('Qual produto você deseja vender(NH se não deseja comprar nada): ').strip()
        if desejado == 'NH':
            x += 200
            mov = False
            os.system('cls')
            cons()
            break
        quant = int(input('Quanto deseja?: '))
        for v in cont:
            if v[0] == desejado and v[1] >= quant and quant > 0:#procura produto; verefica quantidade válida;verefica quantidade desejada
                maxc -= quant
                for j in sell:
                    #vende
                    if j[0] == desejado:
                        j[1] += quant
                        if quant == v[1]:
                            cont.remove(v)
                        else:
                            v[1] -= quant
                        cr += quant*j[3]
                        print('\033[33mVENDIDO!\033[m')
                        time.sleep(1)
                        break
        os.system('cls')

def colisao():
    global iten,comb,maxc,cont,cr,x,y,z,estpreco
    for pos,c in enumerate(iten):
        #c[0]+50,c[1]-22.5,c[2]-c[3]*4.05 glTranslatef(c[0]+50,c[1]-22.5,c[2]-c[3]*4.05)
        if math.sqrt((c[0]+50--x)**2 +  (c[1]-22.5--y)**2 +  (c[2]-c[3]*4.05--z)**2 ) < 90:
            comerc(estpreco[pos],pos)

def key_callback(window, key, scancode, action, mods):
    global x,y,z,angle,mov,vel,comb,cr,hyper,ship
    # if key == glfw.KEY_W:
    #      z += 0.5
    # if key == glfw.KEY_S:
    #      z -= 0.5
    # if key == glfw.KEY_A:
    #     angle -= 4
    #     print(angle)
    # elif key == glfw.KEY_D:
    #     angle += 4
    #     print(angle)
    if key == glfw.KEY_D:
        angle += 4
    elif key == glfw.KEY_A:
        angle -= 4
    elif key == glfw.KEY_W:
        y -= vel+1.5
    elif key == glfw.KEY_S:
        y += vel+1.5
    elif key == glfw.KEY_O and action == glfw.PRESS:
        mov = True
    elif key == glfw.KEY_P and action == glfw.PRESS:
        mov = False
    elif key == glfw.KEY_R and action == glfw.PRESS:
        if vel < float(ship['max']):
            vel += 0.5
        os.system('cls')
        cons()
    elif key == glfw.KEY_T and action == glfw.PRESS:
        if vel > 0:
            vel -= 0.5
        os.system('cls')
        cons()
    elif key == glfw.KEY_H and action == glfw.PRESS:
        z += math.cos(math.radians(angle)) * float(ship['pulo espacial'])
        x -= math.sin(math.radians(angle)) * float(ship['pulo espacial'])
        comb -= 150000/1000
        time.sleep(1)
        print('\033[31m1\033[m',end='  ')
        time.sleep(1)
        print('\033[32m2\033[m',end='  ')
        time.sleep(1)
        print('\033[35m3\033[m',end='  ')
        time.sleep(1)
        print('\033[36m4\033[m',end='  ')
        time.sleep(1)
        print('\033[37m5\033[m')
        print('\033[33mPULO ESPACIAL\033[m')
        time.sleep(2)
        os.system('cls')
        cons()
    elif key == glfw.KEY_I and action == glfw.PRESS and hyper == True:
        z += math.cos(math.radians(angle)) * float(ship['pulo hypespacial'])
        x -= math.sin(math.radians(angle)) * float(ship['pulo hypespacial'])
        comb -= 240000 / 1000
        time.sleep(1)
        print('\033[31m1\033[m', end='  ')
        time.sleep(1)
        print('\033[32m2\033[m', end='  ')
        time.sleep(1)
        print('\033[35m3\033[m', end='  ')
        time.sleep(1)
        print('\033[36m4\033[m', end='  ')
        time.sleep(1)
        print('\033[37m5\033[m')
        print('\033[33mPULO HYPESPACIAL\033[m')
        time.sleep(2)
        os.system('cls')
        cons()

def init():
    glClearColor(0,0,0.4,0)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 100, 5000000000000000000000000000000000000000)
    glMatrixMode(GL_MODELVIEW)
    glLineWidth(4)
    glPointSize(4)

def render():
    global x,y,z,iten,sate,estr
    glLoadIdentity()
    glRotatef(angle, 0, 2, 0)
    glTranslatef(x, y, z)
    # glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0,0,1)
    quad = gluNewQuadric()

    for pos,c in enumerate(estr):
        glColor3fv(c[4])
        glPushMatrix()
        glTranslatef(c[0],c[1],c[2])
        gluSphere(quad,c[3],30,30)
        glPopMatrix()

    for pos,c in enumerate(iten):
        if  math.sqrt(
                ((sate[pos][0]-math.sin(math.radians(sate[pos][5]))*sate[pos][3]*6)--x)**2+
                ((sate[pos][1]-math.cos(math.radians(sate[pos][5]))*sate[pos][3])--y)**2+
                ((sate[pos][2]+math.cos(math.radians(sate[pos][5]))*sate[pos][3]*6)--z)**2) < 2200000:
            glColor3fv(sate[pos][4])
            glPushMatrix()
            glTranslatef((sate[pos][0]-math.sin(math.radians(sate[pos][5]))*c[3]*6)
                         ,sate[pos][1]-math.cos(math.radians(sate[pos][5]))*c[3],
                         (sate[pos][2]+math.cos(math.radians(sate[pos][5]))*c[3]*6))
            gluSphere(quad,sate[pos][3],30,30)
            glPopMatrix()
            if math.sqrt(
                    ((sate[pos][0]-math.sin(math.radians(sate[pos][5]))*sate[pos][3]*6)--x)**2+
                    ((sate[pos][1]-math.cos(math.radians(sate[pos][5]))*sate[pos][3])--y)**2+
                    ((sate[pos][2]+math.cos(math.radians(sate[pos][5]))*sate[pos][3]*6)--z)**2) < 1800000:
                glLineWidth(2)
                glBegin(GL_LINE_STRIP)
                glColor3f(0.1,0.5,0.1)
                glVertex3f(sate[pos][0]-math.sin(math.radians(sate[pos][5]))*c[3]*6,
                           sate[pos][1]-math.cos(math.radians(sate[pos][5]))*c[3],
                           sate[pos][2]+math.cos(math.radians(sate[pos][5]))*c[3]*6)

                glVertex3f(sate[pos][0] - math.sin(math.radians(sate[pos][5])) * c[3] * 6,
                           sate[pos][1] - math.cos(math.radians(sate[pos][5])) * c[3]+32000.5,
                           sate[pos][2] + math.cos(math.radians(sate[pos][5])) * c[3] * 6)

                glVertex3f(sate[pos][0] - math.sin(math.radians(sate[pos][5])) * c[3] * 6,
                           sate[pos][1] - math.cos(math.radians(sate[pos][5])) * c[3] - 32000.5,
                           sate[pos][2] + math.cos(math.radians(sate[pos][5])) * c[3] * 6)
                glEnd()
            #
            # glVertex3f(sate[pos][0],sate[pos][1]+32000.5,sate[pos][2])
            # glVertex3f(sate[pos][0],sate[pos][1]-32000.5,sate[pos][2])
            glLineWidth(4)

    for pos, c in enumerate(sorted(iten)):
        if math.sqrt((c[0]+50--x)**2 +  (c[1]-22.5--y)**2 +  (c[2]-c[3]*4.05--z)**2 ) < 1800000:
            glColor3f(1,1,0.4)
            glPushMatrix()
            glTranslatef(c[0] + 65, c[1] - 22.5, c[2] - c[3] * 4.05)
            glLineWidth(2)
            vert1 = circuferencia(2)
            vert2 = circuferencia(-30)
            glBegin(GL_QUADS)
            for i in range(len(vert1)):
                p = (i+1)%len(vert1)

                glVertex3fv(vert1[i])
                glVertex3fv(vert1[p])
                glVertex3fv(vert2[p])
                glVertex3fv(vert2[i])
            glEnd()
            glLineWidth(4)
            glPopMatrix()
            glBegin(GL_QUADS)
            glColor3f(1, 0, 0)
            glVertex3f(c[0] + 65, c[1] - 22.5, c[2] - c[3] * 4.05)
            glVertex3f(c[0] + 65, c[1] - 22.5, c[2] - c[3] * 4.05 - 28)
            glVertex3f(c[0] + 65 + 325, c[1] - 22.5, c[2] - c[3] * 4.05 - 28)
            glVertex3f(c[0] + 65 + 325, c[1] - 22.5, c[2] - c[3] * 4.05)

            glVertex3f(c[0] + 65, c[1] - 22.5, c[2] - c[3] * 4.05)
            glVertex3f(c[0] + 65, c[1] - 22.5, c[2] - c[3] * 4.05 - 28)
            glVertex3f(c[0] + 65 - 325, c[1] - 22.5, c[2] - c[3] * 4.05 - 28)
            glVertex3f(c[0] + 65 - 325, c[1] - 22.5, c[2] - c[3] * 4.05)
            glEnd()
            glBegin(GL_LINES)
            glColor3f(1, 0, 0)
            glVertex3f(c[0],c[1],c[2]-c[3]*4)
            glVertex3f(c[0]+200,c[1],c[2]-c[3]*4)
            glVertex3f(c[0], c[1]-50, c[2]-c[3]*4)
            glVertex3f(c[0] + 200, c[1]-50, c[2]-c[3]*4)

            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)

            glVertex3f(c[0], c[1], c[2] - c[3] * 4)
            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)

            glVertex3f(c[0]+200,c[1],c[2]-c[3]*4)
            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)

            glVertex3f(c[0], c[1]-50, c[2]-c[3]*4)
            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)

            glVertex3f(c[0] + 200, c[1] - 50, c[2] - c[3] * 4)
            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)


            glVertex3f(c[0], c[1], c[2] - c[3] * 4)
            glVertex3f(c[0], c[1] - 50, c[2] - c[3] * 4)

            glVertex3f(c[0] + 200, c[1], c[2] - c[3] * 4)
            glVertex3f(c[0] + 200, c[1] - 50, c[2] - c[3] * 4)


            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)

            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)
            glEnd()
            glLineWidth(1)
            glBegin(GL_LINE_STRIP)
            glColor3f(1, 1, 0)
            glVertex3f(c[0] + 50, c[1] - 22.5, c[2] - c[3] * 4.05)
            glVertex3f(c[0] + 50, c[1] + 32000.5, c[2] - c[3] * 4.05)
            glVertex3f(c[0] + 50, c[1] - 32000.5, c[2] - c[3] * 4.05)
            glEnd()
            if math.sqrt((c[0] - -x) ** 2 + (c[1] - -y) ** 2 + (c[2] - -z) ** 2) < 1800000:
                glBegin(GL_LINE_STRIP)
                glColor3f(0,0.75,0)
                glVertex3f(c[0],c[1],c[2])
                glVertex3f(c[0]+c[5],c[1]+32000.5,c[2])
                glVertex3f(c[0]-c[5],c[1]-32000.5,c[2])
                glEnd()
                glLineWidth(4)
            glBegin(GL_QUADS)
            glColor3f(0.75, 0.5, 0)
            glVertex3f(c[0], c[1], c[2] - c[3] * 4)
            glVertex3f(c[0] + 200, c[1], c[2] - c[3] * 4)
            glVertex3f(c[0] + 200, c[1] - 50, c[2] - c[3] * 4)
            glVertex3f(c[0], c[1] - 50, c[2] - c[3] * 4)

            glColor3f(0.75,0.5,0)
            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)
            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)

            glColor3f(1,1,0)
            glVertex3f(c[0] + 200, c[1], c[2] - c[3] * 4)
            glVertex3f(c[0], c[1], c[2] - c[3] * 4)

            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)


            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)
            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)

            glVertex3f(c[0], c[1] - 50, c[2] - c[3] * 4)
            glVertex3f(c[0] + 200, c[1] - 50, c[2] - c[3] * 4)


            glVertex3f(c[0] + 200, c[1], c[2] - c[3] * 4)
            glVertex3f(c[0] + 200, c[1] - 50, c[2] - c[3] * 4)

            glVertex3f(c[0] + 100, c[1] - 25, c[2] - c[3] * 4.1)
            glVertex3f(c[0] + 100, c[1], c[2] - c[3] * 4.1)

            glVertex3f(c[0], c[1] - 25, c[2] - c[3] * 4.1)
            glVertex3f(c[0], c[1]-50, c[2]-c[3]*4)

            glVertex3f(c[0], c[1], c[2] - c[3] * 4)
            glVertex3f(c[0], c[1], c[2] - c[3] * 4.1)
            glEnd()

    for pos,c in enumerate(sorted(iten)):
        if c[0] != x and c[1] != y and c[2] != z:
            glPushMatrix()
            glColor3fv(c[4])


            glTranslatef(c[0], c[1], c[2])
            gluSphere(quad, c[3], 30, 30)
            glLineWidth(2)
            if c[7] < 18:
                glColor4f(c[4][0] + 0.25, c[4][1] + 0.25, c[4][2] + 0.25, 1)
                glBegin(GL_LINE_LOOP)
                for i in range(0, 50):
                    ang = 0 + (i / float(50 - 1) * (360 - 0))
                    rad = math.radians(ang)
                    x2 = (c[3] * 1.5) * math.cos(rad)
                    z2 = (c[3] * 1.5) * math.sin(rad)
                    y2 = 0
                    if c[6] != 0:
                        y2 = (c[3] * 1.5) * math.cos(rad) / c[6]
                    else:
                        y2 = (c[3] * 1.5) * math.cos(rad) / 2
                    glVertex3f(x2, y2, z2)
                glEnd()
                glBegin(GL_LINE_LOOP)
                for i in range(0, 50):
                    ang = 0 + (i / float(50 - 1) * (360 - 0))
                    rad = math.radians(ang)
                    x2 = (c[3] * 2) * math.cos(rad)
                    z2 = (c[3] * 2) * math.sin(rad)
                    y2 = 0
                    if c[6] != 0:
                        y2 = (c[3] * 2) * math.cos(rad) / c[6]
                    else:
                        y2 = (c[3] * 2) * math.cos(rad) / 2
                    glVertex3f(x2, y2, z2)
                glEnd()
                glBegin(GL_LINE_LOOP)
                for i in range(0, 50):
                    ang = 0 + (i / float(50 - 1) * (360 - 0))
                    rad = math.radians(ang)
                    x2 = (c[3] * 1.75) * math.cos(rad)
                    z2 = (c[3] * 1.75) * math.sin(rad)
                    y2 = 0
                    if c[6] != 0:
                        y2 = (c[3] * 1.75) * math.cos(rad) / c[6]
                    else:
                        y2 = (c[3] * 1.75) * math.cos(rad) / 2
                    glVertex3f(x2, y2, z2)
                glEnd()
                glLineWidth(4)
            glPopMatrix()
    for pos,c in enumerate(sorted(iten)):
        if c[0] != x and c[1] != y and c[2] != z:
            glPushMatrix()
            glTranslatef(c[0], c[1], c[2])
            if math.sqrt((c[0]--x)**2+(c[1]--y)**2+(c[2]--z)**2) < c[3]*5.5:
                glColor4f(1,0,1,0.04)
                gluSphere(quad, c[3]+190,30,30)
                glColor4f(0.001, 0.001, 1, 0.04)
                gluSphere(quad, c[3] + 290, 30, 30)
            if math.sqrt((c[0]--x)**2+(c[1]--y)**2+(c[2]--z)**2) < c[3]*4.2:
                glColor4f(1,0,1,0.08)
                gluSphere(quad, c[3]+190,30,30)
                glColor4f(0.001, 0.001, 1, 0.08)
                gluSphere(quad, c[3] + 290, 30, 30)
            glPopMatrix()

def tc():
    time.sleep(0.1)
    os.system('cls')
def m_consl():
    global vel,comb,cr,maxc,ship
    print('\033[31m---  CONSOLE  ---\033[m')
    tc()
    print('\033[32m---  CONSOLE  ---\033[m')
    tc()
    print('\033[33m---  CONSOLE  ---\033[m')
    tc()
    print('\033[34m---  CONSOLE  ---\033[m')
    tc()
    print('\033[35m---  CONSOLE  ---\033[m')
    print(f'\033[33mvelocidade:{vel}\033[m')
    print(f'\033[32mcombustível:{comb:.2f}\033[m')
    print(f'\033[34mcréditos:{cr}\033[m')
    print(f'\033[37mcarga/t:{maxc}\033[m')
    print(f'nave:{ship['nave']}')

def pcoli(coli):
    print(f'\033[31m- - - COLISÃO CONTRA {coli} - - -\033[m')
    time.sleep(1)
    os.system('cls')
    print(f'\033[33m- - - COLISÃO CONTRA {coli} - - -\033[m')
    time.sleep(1)
    os.system('cls')
    print(f'\033[31m- - - COLISÃO CONTRA {coli} - - -\033[m')
    time.sleep(1)

def line(quant):
    print((quant+4)*3*'-')

def apresent():
    global ship
    line(len(ship['nave']))
    print(f' Você está controlando uma {ship['nave']}')
    line(len(ship['nave']))
    time.sleep(4)
    os.system('cls')

def main():
    global x,y,z,angle,mov,iten,vel,comb
    create_world()
    create_name_planets()
    glfw.init()
    window = glfw.create_window(800,800,"SuperSpace 3",None,None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_pos(window,500,120)
    init()
    apresent()
    m_consl()
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    crtprc()
    satec()
    preco_ships()
    while not glfw.window_should_close(window):
        if mov == True:
            if comb > 0:
                z += math.cos(math.radians(angle)) * vel
                x -= math.sin(math.radians(angle)) * vel
            elif comb <= 0:
                print('\033[31mO COMBUSTÍVEL ACABOU!!!\033[m')
                break
        if comb <= 0:
            print('\033[31mO COMBUSTÍVEL ACABOU!!!\033[m')
            break
        if estr_colisao() == True:
            pcoli('ESTRELA')
            break
        sater()
        render()
        if sate_colisao() == True:
            pcoli('SATÉLITE')
            break
        colisao()
        if planeta_colisao() == True:
            pcoli('PLANETA')
            break
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()