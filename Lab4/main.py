import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Vertices for a cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Edges for a cube
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (6, 3),
    (7, 2),
    (0, 4),
    (1, 5),
    (7, 6),
    (4, 6)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialization
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

rotation_enabled = False
rotate_x = True
rotate_speed = 1.0

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button
                    glColor3fv((random.random(), random.random(), random.random()))
                elif event.button == 3:  # right mouse button
                    global rotation_enabled
                    rotation_enabled = not rotation_enabled
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    global rotate_speed
                    rotate_speed *= 1.2
                elif event.key == pygame.K_DOWN:
                    rotate_speed /= 1.2
                elif event.key == pygame.K_SPACE:
                    global rotate_x
                    rotate_x = not rotate_x

        if rotation_enabled:
            if rotate_x:
                glRotatef(rotate_speed, 1, 0, 0)
            else:
                glRotatef(rotate_speed, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
