import pygame
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((800, 500))

def lerp_num(a, b, x):
    return round(a + (b - a) * x)

def lerp_pos(a, b, x):
    return [lerp_num(a[0], b[0], x), lerp_num(a[1], b[1], x)]

def lerp_color(a, b, x):
    return [lerp_num(a[0], b[0], x), lerp_num(a[1], b[1], x), lerp_num(a[2], b[2], x)]

running = True
clock = pygame.time.Clock()
p1 = [100, 200]
p2 = [200, 250]
p3 = [150, 150]
p4 = [250, 400]
c1 = [250, 250, 250]
c2 = [250, 100, 100]
c3 = [100, 100, 250]
c4 = [100, 100, 100]
x_now = 0
x_speed = 0
controlling = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                x_speed = 1
            if event.key == K_DOWN:
                x_speed = -1
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                x_speed = 0
        if event.type == MOUSEMOTION:
            if controlling == 1:
                p1 = event.pos
            if controlling == 2:
                p2 = event.pos
            if controlling == 3:
                p3 = event.pos
            if controlling == 4:
                p4 = event.pos
        if event.type == MOUSEBUTTONDOWN:
            if math.sqrt((event.pos[0] - p1[0]) ** 2 + (event.pos[1] - p1[1]) ** 2) <= 12:
                controlling = 1
            if math.sqrt((event.pos[0] - p2[0]) ** 2 + (event.pos[1] - p2[1]) ** 2) <= 12:
                controlling = 2
            if math.sqrt((event.pos[0] - p3[0]) ** 2 + (event.pos[1] - p3[1]) ** 2) <= 12:
                controlling = 3
            if math.sqrt((event.pos[0] - p4[0]) ** 2 + (event.pos[1] - p4[1]) ** 2) <= 12:
                controlling = 4
        if event.type == MOUSEBUTTONUP:
            controlling = 0

    x_now = max(0, min(1, x_now + 0.01 * x_speed))
    screen.fill((35, 30, 40))

    for x_line in range(1001):
        if x_line % 150 >= 75:
            screen.set_at(lerp_pos(p1, p2, x_line / 1000), lerp_color(c1, c2, x_line / 1000))
        else:
            screen.set_at(lerp_pos(p3, p4, x_line / 1000), lerp_color(c3, c4, x_line / 1000))
        if x_line % 150 >= 140:
            screen.set_at(lerp_pos(p2, p3, x_line / 1000), lerp_color(c2, c3, x_line / 1000))
        screen.set_at(
            lerp_pos(
                lerp_pos(
                    lerp_pos(p1, p2, x_line / 1000),
                    lerp_pos(p2, p3, x_line / 1000),
                    x_line / 1000
                ),
                lerp_pos(
                    lerp_pos(p2, p3, x_line / 1000),
                    lerp_pos(p3, p4, x_line / 1000),
                    x_line / 1000
                ),
                x_line / 1000
            ), lerp_color(c1, c4, x_line / 1000))

    pygame.draw.circle(screen, (230, 230, 230), p1, 12)
    pygame.draw.circle(screen, (230, 230, 230), p2, 12)
    pygame.draw.circle(screen, (230, 230, 230), p3, 12)
    pygame.draw.circle(screen, (230, 230, 230), p4, 12)

    pygame.draw.circle(screen, c1, p1, 10)
    pygame.draw.circle(screen, c2, p2, 10)
    pygame.draw.circle(screen, c3, p3, 10)
    pygame.draw.circle(screen, c4, p4, 10)
    
    pb = lerp_pos(
        lerp_pos(
            lerp_pos(p1, p2, x_now),
            lerp_pos(p2, p3, x_now),
            x_now
        ),
        lerp_pos(
            lerp_pos(p2, p3, x_now),
            lerp_pos(p3, p4, x_now),
            x_now
        ),
        x_now
    )
    pygame.draw.circle(screen, (230, 230, 230), pb, 12)
    pygame.draw.circle(screen, lerp_color(c1, c4, x_now), pb, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
