import time
import random
def m1():
    print("-=    Calculadora de x    =-")
    valor_igual = int(input('Qual valor será igual a multiplicação: '))
    print(f"{valor_igual} = ? . ?")
    valor_descoberto = int(input('Qual o primeiro fator o que se sabe o valor: '))
    print(f"{valor_igual} = {valor_descoberto} . x")
    print(f"=-   Calculando o valor de x ",end=' ')
    for c in range(0,3):
        time.sleep(1)
        print('.', end=' ')
    print('   -=')
    if valor_descoberto < valor_igual:
        print(f"   O valor de x é {valor_igual / valor_descoberto}")
    else:
        print(f"   O valor de x é {valor_descoberto / valor_igual}")
def m2():
    x = 4
    print("-=    Calculadora de dano    =-")
    for c in range(0, 20):
        valor_igual = random.randint(1,20)
        valor_descoberto = random.randint(1, 20)
        print(f"A força foi {valor_descoberto}, o dano foi {valor_descoberto*x}")
import os
import time
'''

def atualiza_tela():
    global tela
    global z
    chao = 6 - z
    print(chao)
    for pos, linha2 in enumerate(tela):
        if pos >= chao and z <= 3:
            tela[pos] = ['#', '#', '#', '#', '#', '#', '#']


def desenha_tela():
    global tela
    global z
    for linha in tela:
        for coluna in linha:
            if coluna == ' ':
                print(f'\033[0;0;44m{coluna}\033[m', end='\033[0;0;44m \033[m')
            elif coluna == '#':
                print(f'\033[32;0;42m{coluna}\033[m', end='\033[32;0;42m \033[m')
        print()
    for pos3, linha3 in enumerate(tela):
        tela[pos3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if z > 3:
        for pos, linha2 in enumerate(tela):
            if pos >= 3 and z > 3:
                tela[pos] = ['#', '#', '#', '#', '#', '#', '#']


def linha():
    print('-' * 30)


tela = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
z = 1
while True:
    atualiza_tela()
    linha()
    desenha_tela()
    linha()
    print(f'O eixo z e igual a: {z}')
    acao = input('Deseja fazer o que: subir(w), descer(s); ').strip()
    if z == 1 and acao == 's':
        print('\033[31mVocê já se encontra no chão\033[m')
    elif z > 1 and acao == 's':
        z -= 1
    elif acao == 'w':
        z += 1
    time.sleep(2)
    os.system('cls')'''
import pygame
import numpy as np
import math

pygame.init()
SIZE = 800
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("sSuperVisualv")

clock = pygame.time.Clock()

def smoothstep(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3.0 - 2.0 * x)

NUM_POINTS = 2000

phi = np.random.uniform(0, 2 * np.pi, NUM_POINTS)
costheta = np.random.uniform(-1, 1, NUM_POINTS)
theta = np.arccos(costheta)

r = 1.0
sphere_x = r * np.sin(theta) * np.cos(phi)
sphere_y = r * np.sin(theta) * np.sin(phi)
sphere_z = r * np.cos(theta)
shape_sphere = np.stack((sphere_x, sphere_y, sphere_z), axis=1)

cube_points = np.random.uniform(-0.8, 0.8, (NUM_POINTS, 3))
shape_cube = cube_points

targets = [shape_sphere, shape_cube]
shape_idx = 0
next_idx = 1
phase_t = 0.0
MORPH = 3.0
direction = 1

angle_y = 0.0
angle_x = 0.0

running = True
while running:
    dt = clock.tick(60) / 1000.0
    screen.fill((5, 5, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    phase_t += dt * direction
    if phase_t > MORPH:
        phase_t = MORPH
        direction = -1
        shape_idx, next_idx = next_idx, shape_idx  # troca as formas
    elif phase_t <= 0:
        phase_t = 0
        direction = 1
        shape_idx, next_idx = next_idx, shape_idx  # troca as formas

    u = smoothstep(phase_t / MORPH)
    a = targets[shape_idx]
    b = targets[next_idx]
    pos = a * (1.0 - u) + b * u

    # Efeito "respirar" — com proteção contra divisão por zero
    norms = np.linalg.norm(pos, axis=1, keepdims=True)
    norms[norms == 0] = 1.0  # evita divisão por zero
    breathe = math.sin(u * math.pi / 2) * 0.22
    pos = pos + (pos / norms) * breathe

    angle_x += 0.005
    angle_y += 0.01

    cy, sy = math.cos(angle_y), math.sin(angle_y)
    cp, sp = math.cos(angle_x), math.sin(angle_x)

    x0, y0, z0 = pos[:, 0], pos[:, 1], pos[:, 2]
    x1 = x0 * cy - z0 * sy
    z1 = x0 * sy + z0 * cy
    y1 = y0 * cp - z1 * sp
    z2 = y0 * sp + z1 * cp

    depth = np.clip(z2 + 2.55, 0.4, None)
    sx = (SIZE * 0.5) + (x1 / depth) * 660.0
    sy = (SIZE * 0.5) - (y1 / depth) * 660.0

    # DESENHA TODOS OS PONTOS
    for i in range(NUM_POINTS):
        if 0 <= sx[i] < SIZE and 0 <= sy[i] < SIZE:
            brightness = int(np.clip((3.5 - depth[i]) * 100, 50, 255))
            color = (0, brightness, 255)
            pygame.draw.rect(screen, color, (int(sx[i]), int(sy[i]), 2, 2))

    # ATUALIZA A TELA UMA VEZ POR FRAME — fora do loop de pontos!
    pygame.display.flip()

pygame.quit()