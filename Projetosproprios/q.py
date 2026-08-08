import math
import time
import sys
import os

# ============================================================
# RENDERIZADOR 3D DE TERMINAL — PYTHON PURO (STDLIB ONLY)
# ============================================================

LARGURA = 80
ALTURA = 40
DISTANCIA_PROJECAO = 3.0       # distância do plano de projeção à câmera
OFFSET_Z = 4.0                 # afasta o cubo da câmera
VELOCIDADE = 0.04

# --- Cubo: 8 vértices --------------------------------------
vertices = [
    [-1, -1, -1], [ 1, -1, -1], [ 1,  1, -1], [-1,  1, -1],  # trás  (z = -1)
    [-1, -1,  1], [ 1, -1,  1], [ 1,  1,  1], [-1,  1,  1],  # frente (z =  1)
]

# --- Faces (4 vértices cada, sentido horário) --------------
faces = [
    [0, 1, 2, 3],   # trás   (z = -1)
    [4, 5, 6, 7],   # frente (z =  1)
    [0, 1, 5, 4],   # baixo  (y = -1)
    [2, 3, 7, 6],   # cima   (y =  1)
    [0, 3, 7, 4],   # esquerda (x = -1)
    [1, 2, 6, 5],   # direita  (x =  1)
]

cores_faces = [31, 32, 33, 34, 35, 36]   # vermelho, verde, amarelo, azul, magenta, ciano

# --- Funções de rotação 3D ---------------------------------
def rotacao_x(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [v[0], v[1]*c - v[2]*s, v[1]*s + v[2]*c]

def rotacao_y(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [v[0]*c + v[2]*s, v[1], -v[0]*s + v[2]*c]

def rotacao_z(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [v[0]*c - v[1]*s, v[0]*s + v[1]*c, v[2]]

# --- Projeção perspectiva ----------------------------------
def projecao(v):
    x, y, z = v
    # evita divisão por zero ou negativa
    denom = z + DISTANCIA_PROJECAO
    if denom < 0.2:
        denom = 0.2
    fator = 1.0 / denom
    # aspecto do terminal: caractere ~ 2x1 (largura x altura)
    px = int(x * fator * (LARGURA * 0.35) + LARGURA // 2)
    py = int(-y * fator * (ALTURA * 0.45) + ALTURA // 2)
    return [px, py, z]

# --- Bresenham ---------------------------------------------
def bresenham(x0, y0, x1, y1):
    pts = []
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return pts

# --- Desenha linha com interpolação de Z e z-buffer --------
def desenhar_linha(tela, zbuf, x0, y0, z0, x1, y1, z1, cor):
    pts = bresenham(int(x0), int(y0), int(x1), int(y1))
    n = len(pts)
    if n == 0:
        return
    for i, (x, y) in enumerate(pts):
        if 0 <= x < LARGURA and 0 <= y < ALTURA:
            t = i / max(n - 1, 1)
            z = z0 + (z1 - z0) * t
            # menor Z = mais perto da câmera (câmera em -Z olhando +Z)
            if z < zbuf[y][x]:
                zbuf[y][x] = z
                tela[y][x] = f"\033[{cor}m#\033[0m"

# --- Centroide Z de uma face (painter's algorithm) ---------
def centroide_z(verts, face):
    return sum(verts[i][2] for i in face) / len(face)

# --- Desenha uma face (wireframe) --------------------------
def desenhar_face(tela, zbuf, proj, face, cor):
    n = len(face)
    for i in range(n):
        v0 = proj[face[i]]
        v1 = proj[face[(i + 1) % n]]
        desenhar_linha(tela, zbuf, v0[0], v0[1], v0[2],
                       v1[0], v1[1], v1[2], cor)

# --- Main loop ---------------------------------------------
def main():
    ang_x = ang_y = ang_z = 0.0

    # limpa terminal uma vez
    # esconde cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            # 1) Rotaciona vértices
            verts_rot = []
            for v in vertices:
                v = rotacao_x(v, ang_x)
                v = rotacao_y(v, ang_y)
                v = rotacao_z(v, ang_z)
                v[2] += OFFSET_Z          # afasta da câmera
                verts_rot.append(v)

            # 2) Projeta
            proj = [projecao(v) for v in verts_rot]

            # 3) Ordena faces do mais longe ao mais perto
            faces_ord = sorted(range(len(faces)),
                               key=lambda i: centroide_z(verts_rot, faces[i]),
                               reverse=True)

            # 4) Buffers
            tela = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]
            zbuf = [[float("inf") for _ in range(LARGURA)] for _ in range(ALTURA)]

            # 5) Rasteriza
            for fi in faces_ord:
                desenhar_face(tela, zbuf, proj, faces[fi], cores_faces[fi])

            # limpa terminal
            sys.stdout.write("\033[H")
            sys.stdout.flush()
            # some o cursor de digitação
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            for linha in tela:
                for coluna in linha:
                    print(coluna,end=' ')
                print()

            # 7) Atualiza ângulos
            ang_x += VELOCIDADE
            ang_y += VELOCIDADE * 0.7
            ang_z += VELOCIDADE * 0.3

            time.sleep(0.03)

    except KeyboardInterrupt:
        sys.stdout.write("\033[0m\033[?25h")  # reseta cores + mostra cursor
        print("\nRenderizador encerrado.")

if __name__ == "__main__":
    main()