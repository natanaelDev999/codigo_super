import os
import glfw
import math
import time
import random
from OpenGL.GL import *
from OpenGL.GLU import *

iten = [(random.randint(900, 6000), random.randint(-10, 20),40000,
         random.randint(5012, 6000),[random.random(),random.random(),random.random()]),

        (random.randint(-3200, 3000), random.randint(-10, 20), 180000,
         random.randint(5012, 6000),[random.random(),random.random(),random.random()]),

        (random.randint(-164000,3000), random.randint(-10,10), 340000,
         random.randint(5012,6000),[random.random(),random.random(),random.random()]),

        (random.randint(5000,6000), random.randint(-10,20),-84000,
         random.randint(5012,6000),[random.random(),random.random(),random.random()]),

        (random.randint(-6500,9000), random.randint(-10,10), -360000,
         random.randint(5012,6000),[random.random(),random.random(),random.random()])
        ]

est = []
x = 0
y = 0
z = -3
angle = 0
mov = False
vel = 1.5
def estc():
    global est,iten
    for c in iten:
        est.append([(c[0]+120,c[1]+40,c[2]+125),
                    (c[0] + 280, c[1] + 40, c[2] + 125),
                    (c[0] + 280, c[1] + 100, c[2] + 125),
                    (c[0] + 120,c[1] + 100, c[2] + 125 ),

                    (c[0]+60,c[1]+50,c[2]+480),
                    (c[0]+140,c[1]+50,c[2]+480),
                    (c[0]+140,c[1]+90,c[2]+480),
                    (c[0]+60,c[1]+90,c[2]+480),

                    (c[0]+120,c[1]+40,c[2]+125),
                    (c[0]+60,c[1]+50,c[2]+480),

                    (c[0] + 280, c[1] + 40, c[2] + 125),
                    (c[0]+140,c[1]+50,c[2]+480),

                    (c[0] + 280, c[1] + 100, c[2] + 125),
                    (c[0]+140,c[1]+90,c[2]+480),

                    (c[0] + 120, c[1] + 100, c[2] + 125),
                    (c[0]+60,c[1]+90,c[2]+480),

                    (c[0]+160,c[1]+60,c[2]+125),
                    (c[0] + 240, c[1] + 60, c[2] + 125),
                    (c[0] + 240, c[1] + 80, c[2] + 125),
                    (c[0] + 160,c[1] + 80, c[2] + 125 )])

def colisao():
    global x,y,z,est
    for c in est:
        # math.sqrt((v[0]-x)**2+(v[1]-y)**2+(v[2]-z)**2):
        m_x = (c[0][0]+c[1][0])/2
        m_y = (c[0][1]+c[1][1])/2
        m_z = (c[0][2]+c[4][2])/2
        if math.sqrt((m_x-x)**2+(m_y-y)**2+(m_z-z)**2) < 10000:
            print(f'A distância da estação espacial mais próxima é:{math.sqrt((m_x-x)**2+(m_y-y)**2+(m_z-z)**2)}')

def key_callback(window, key, scancode, action, mods):
    global x,y,z,angle,mov,vel
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
        y += vel + 1.5
    elif key == glfw.KEY_O:
        mov = True
    elif key == glfw.KEY_P:
        mov = False
    elif key == glfw.KEY_R and action == glfw.PRESS:
        if vel < 10:
            vel += 0.5
        os.system('cls')
        print('\033[35m---  CONSOLE  ---\033[m')
        print(f'\033[33mvelocidade:{vel}\033[m')
    elif key == glfw.KEY_T and action == glfw.PRESS:
        if vel > 0:
            vel -= 0.5
        os.system('cls')
        print('\033[35m---  CONSOLE  ---\033[m')
        print(f'\033[33mvelocidade:{vel}\033[m')
    elif key == glfw.KEY_H and action == glfw.PRESS:
        z += math.cos(math.radians(angle)) * 150000
        x -= math.sin(math.radians(angle)) * 150000
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
        print('\033[35m---  CONSOLE  ---\033[m')
        print(f'\033[33mvelocidade:{vel}\033[m')

def init():
    glClearColor(0,0,0.4,0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000001, 5000000)
    glMatrixMode(GL_MODELVIEW)
    glLineWidth(4)

def render():
    global x,y,z,iten,est
    glLoadIdentity()
    glRotatef(angle, 0, 2, 0)
    glTranslatef(x, y, z)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)

    for pos,c in enumerate(sorted(iten)):
        if c[0] != x and c[1] != y and c[2] != z:
            glColor3fv(c[4])
            glPushMatrix()

            quad = gluNewQuadric()

            glTranslatef(c[0], c[1], c[2])
            gluSphere(quad, c[3], 30, 30)

            glBegin(GL_LINE_LOOP)
            for pos1,d in enumerate(est[pos]):
                if pos1 <= 3:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()
            glBegin(GL_LINE_LOOP)
            for pos1,d in enumerate(est[pos]):
                if pos1 > 3 and pos1 < 8:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()

            glBegin(GL_LINE_STRIP)
            for pos1,d in enumerate(est[pos]):
                if pos1 >= 8 and pos1 < 10:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()


            glBegin(GL_LINE_STRIP)
            for pos1,d in enumerate(est[pos]):
                if pos1 >= 10 and pos1 < 12:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()


            glBegin(GL_LINE_STRIP)
            for pos1,d in enumerate(est[pos]):
                if pos1 >= 12 and pos1 < 14:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()


            glBegin(GL_LINE_STRIP)
            for pos1,d in enumerate(est[pos]):
                if pos1 >= 14 and pos1 < 16:
                    glColor3f(0.5,0,0)
                    glVertex3fv(d)
            glEnd()

            glBegin(GL_LINE_LOOP)

            for pos1,d in enumerate(est[pos]):
                if pos1 >= 16:
                    glColor3f(0.75,0.75,0)
                    glVertex3fv(d)
            glEnd()
            glPopMatrix()

def tc():
    time.sleep(0.1)
    os.system('cls')
def m_consl():
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

def main():
    global x,z,angle,mov,iten,vel
    glfw.init()
    window = glfw.create_window(800,800,"SuperSpace 3",None,None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    init()
    m_consl()
    estc()
    while not glfw.window_should_close(window):
        if mov == True:
            z += math.cos(math.radians(angle)) * vel
            x -= math.sin(math.radians(angle)) * vel
        render()
        colisao()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()
