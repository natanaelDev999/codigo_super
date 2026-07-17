
import pygame
import random
import time
# inicializando o pygame e criando  uma janela
pygame.init()
tela = pygame.display.set_mode([700, 400])
pygame.display.set_caption('=-=jogo 1 =-=')
font = pygame.font.SysFont('arial', 20, True, False)
fonte = pygame.font.SysFont('arial', 20, True, False)
fonte3 = pygame.font.SysFont('arial', 20, True, False)
nivel = 1
pontos = 0
p = True
xp = random.randint(30, 600)
yp = random .randint(30, 400)
x = 50
y = 50
vel = 10
vida = 3
if pontos == 5:
        nivel = 1
if nivel == 2:
    vida = vida + 2
objeto = True
h = True
c = 600
vel2 = 1
xw = 50
yw = 50
xx = 600
yy = 190
xxx = 600
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if pygame.key.get_pressed()[pygame.K_a]:
            x = x - vel
        if pygame.key.get_pressed()[pygame.K_d]:
            x = x + vel
        if pygame.key.get_pressed()[pygame.K_w]:
            y = y - vel
        if pygame.key.get_pressed()[pygame.K_s]:
            y = y + vel
    # desenhando na tela
    tela.fill((50, 131, 70))
    mensagem = f'nivel:{nivel}'
    mensagen = f'pontos: {pontos}'
    mensagem3 = f'vida: {vida}'
    texto = font.render(mensagen, False, (243, 214, 47))
    text = font.render(mensagem, False, (232, 96, 46))
    texto2 = font.render(mensagem3, False, (232, 127, 128))
    player = pygame.Rect(x, y, 20,20)
    p = pygame.draw.rect(tela, [153, 252, 7, 200], player)
    p2 = pygame.draw.rect(tela, [197, 87, 75, 200],(xp,yp,20,20))
    pygame.draw.rect(tela, (117, 62, 14, 200), (0, 0, 700,40))
    if p.colliderect(p2):
        xp = random.randint(40, 300)
        yp = random.randint(20, 300)
        pontos = pontos + 1
    if pontos > nivel * 5:
        nivel += 1
    if nivel == 2:
        boss = font.render('boss!!!', False, (154, 46, 47))
        tela.blit(boss, (600, 140))
        xx = xx - 1
        p4 = pygame.draw.rect(tela, (254, 205, 7, 200), (xx, yy, 20, 30))
        if p.colliderect(p4):
            c = True
            if c == True:
                vida -= 1
                c = False
        if h:
            b = pygame.draw.rect(tela, (128, 20, 20, 200), (600, 190, 60, 60))
            if p.colliderect(b):
                h = False
                vida += 1
                pontos = pontos + 5
    if nivel == 4:
        xxx = xxx - vel2
        p7 = pygame.draw.rect(tela, (254, 205, 7), (xxx, 190, 30, 30))
        p8 =  pygame.draw.rect(tela, (254, 205, 7), (xxx, 260, 30, 30))
        if p.colliderect(p7):
            c1 = True
            if c1 == True:
                vida -= 1
                c1 = False
        if p.colliderect(p8):
            c2 = True
            if c2 == True:
                vida -= 1
                c2 = False
        if objeto:
            boss = font.render('boss!!!', False, (154, 46, 47))
            tela.blit(boss, (600, 140))
            b = pygame.draw.rect(tela, (128, 205, 7), (600, 190, 60, 60))
            if p.colliderect(b):
                c = True
                if c == True:
                    if p.colliderect(b):
                        objeto = False
                        vida += 1
                        pontos += 10
    if nivel == 10:
        c = c - vel2
        z = pygame.draw.rect(tela, (254, 205, 7), (c, 300, 30, 30 ))
        zz = pygame.draw.rect(tela, (254, 205, 7), (c ,190, 30, 30 ))
        zzz = pygame.draw.rect(tela, (254, 205, 7), (c, 50, 30, 30))
        if p.colliderect(z or zz or zzz):
            c = True
            if c == True:
                vida -= 1
                c = False
        if p:
            bb = pygame.draw.rect(tela, (25, 121, 125),(600, 190, 60, 60))
            if p.colliderect(bb):
                pontos += 10
                p = False
                vida +=1

    if pontos == 60:
        fim = font.render('fim voce chegou ao nivel maximo!', False, (185,147,90))
        tela.blit(fim, (350,200 ))
        time.sleep(5)
        loop = False
    if vida == 0:
        loop = False
    tela.blit(texto2,(100, 10) )
    tela.blit(texto, (590, 10))
    tela.blit(text,(3, 10))
    pygame.display.update()