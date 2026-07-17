'''import pygame
import sys
import random

pygame.init()
largura = 600
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('cosmic game')

cor_tela = (73, 72, 119)
cor_player = (131, 148, 37)

jogador = pygame.Rect(300, 600, 50, 30)
vel_j = 5
projeteis = []
vel_p = 10

inimigos = [pygame.Rect(random.randint(0, largura-40), -40 * i, 40, 40) for i in range(5)]
vel_i = 3

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    tela.fill(cor_tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and jogador.left > 0:
        jogador.x -= vel_j
    if teclas[pygame.K_d] and jogador.right < largura:
        jogador.x += vel_j
    if teclas[pygame.K_SPACE]:
        if len(projeteis) < 10:
            projeteis.append(pygame.Rect(jogador.centerx - 5, jogador.top, 10, 20))

    # Atualizar projéteis
    for proj in projeteis[:]:
        proj.y -= vel_p
        if proj.bottom < 0:
            projeteis.remove(proj)

    # Atualizar inimigos
    for inimigo in inimigos:
        inimigo.y += vel_i
        if inimigo.top > altura:
            inimigo.x = random.randint(0, largura - 40)
            inimigo.y = -40

    # Colisão projétil x inimigo
    for p in projeteis[:]:
        for inimigo in inimigos[:]:
            if p.colliderect(inimigo):
                projeteis.remove(p)
                inimigos.remove(inimigo)
                inimigos.append(pygame.Rect(random.randint(0, largura - 40), -40, 40, 40))
                break

    # Desenhar
    pygame.draw.rect(tela, cor_player, jogador)
    for proj in projeteis:
        pygame.draw.rect(tela, (201, 130, 22), proj)
    for inimigo in inimigos:
        pygame.draw.rect(tela, (128, 128, 128), inimigo)

    pygame.display.update()'''
import pygame
import sys
import random
pygame.init()
largura = 600
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('cosmic game')
cor_tela= (73, 72,119)
cor_player = (131, 148, 37)
jogador = pygame.Rect(300,600,50,30)
vel_j = 5
projeteis = []
vel_p = 10
inimigos = [pygame.Rect(random.randint(0,360), -40 * i, 40, 40)for i in range(5)]
vel_i = 3
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    tela.fill(cor_tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and jogador.left > 0:
        jogador.x -= vel_j
    if teclas[pygame.K_d] and jogador.right < largura:
        jogador.x += vel_j
    if teclas[pygame.K_SPACE]:
        if len(projeteis) < 10:
            projeteis.append(pygame.Rect(jogador.centery - 5, jogador.top, 10, 20))
    for proj in projeteis[:]:
        proj.y -= 10
        if proj.bottom < 0:
            projeteis.remove(proj)

    for inimigo in inimigos:
        inimigo.y += vel_i
        if inimigo.top > 600:
            inimigo.x = random.randint(0, 360)
            inimigo.y = -40

    for p in projeteis[:]:
        for inimigo in inimigos[:]:
            if p.colliderect(inimigo):
                projeteis.remove(p)
                inimigos.remove(inimigo)
                inimigos.append(pygame.Rect(random.randint(0, 360), -40, 40,40))
                break

    pygame.draw.rect(tela, cor_player, jogador)
    for proj in projeteis:
        pygame.draw.rect(tela, (201, 130, 22), proj)
    for inimigo in inimigos:
        pygame.draw.rect(tela, (128, 128, 128), inimigo)
    pygame.display.update()

