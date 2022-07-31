import pygame
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))

def lerp_num(a, b, x):
    return round(a + (b - a) * x)

def lerp_pos(a, b, x):
    return [lerp_num(a[0], b[0], x), lerp_num(a[1], b[1], x)]

def lerp_color(a, b, x):
    return [lerp_num(a[0], b[0], x), lerp_num(a[1], b[1], x), lerp_num(a[2], b[2], x)]

running = True
clock = pygame.time.Clock()
p1 = [1180, 100]
p2 = [1180, 620]
p3 = [100, 620]
p4 = [100, 100]

c1 = [250, 250, 250]
c2 = [250, 50, 50]
c3 = [50, 50, 250]
c4 = [50, 50, 50]
"""
p1 = [1180, 100]
p2 = [1180, 620]
p3 = [100, 620]
p4 = [100, 620]

c1 = [255, 0, 0]
c2 = [0, 255, 0]
c3 = [0, 0, 255]
c4 = [0, 0, 255]
"""
x_now = 0
x_speed = 0
controlling = 0
no_cycle = False
draw_mode = False
while running:
    if not draw_mode:
        screen.fill((35, 30, 40))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_UP:          # 上下键切换移动方向
                x_speed += 1
            if event.key == K_DOWN:
                x_speed -= 1
            if event.key == K_SPACE:       # 空格键切换移动方式
                no_cycle = not no_cycle
            if event.key == K_r:           # R键刷新
                screen.fill((35, 30, 40))
            if event.key == K_d:           # D切换观赏模式
                draw_mode = not draw_mode

        if event.type == KEYUP:
            if event.key == K_UP:
                x_speed -= 1
            if event.key == K_DOWN:
                x_speed += 1

        if not draw_mode:
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

    if draw_mode:
        x_now += 0.0005 * x_speed
    else:
        x_now += 0.01 * x_speed
    if no_cycle:
        x_now = min(max(x_now, 0), 1)
    if x_now > 1:
        x_now -= 1
    if x_now < 0:
        x_now += 1
    
    pb12 = lerp_pos(p1, p2, x_now)
    pb23 = lerp_pos(p2, p3, x_now)
    pb34 = lerp_pos(p3, p4, x_now)
    pb13 = lerp_pos(
        pb12,
        pb23,
        x_now
    )
    pb24 = lerp_pos(
        pb23,
        pb34,
        x_now
    )
    pb = lerp_pos(pb13, pb24, x_now)

    cb12 = lerp_color(c1, c2, x_now)
    cb23 = lerp_color(c2, c3, x_now)
    cb34 = lerp_color(c3, c4, x_now)
    cb13 = lerp_color(cb12, cb23, x_now)
    cb24 = lerp_color(cb23, cb34, x_now)
    cb = lerp_color(cb13, cb24, x_now)
    
    for x_line in range(1501):
        l12 = lerp_pos(p1, p2, x_line / 1500)
        l23 = lerp_pos(p2, p3, x_line / 1500)
        l34 = lerp_pos(p3, p4, x_line / 1500)
        c12 = lerp_color(c1, c2, x_line / 1500)
        c23 = lerp_color(c2, c3, x_line / 1500)
        c34 = lerp_color(c3, c4, x_line / 1500)
        l13 = lerp_pos(
            l12,
            l23,
            x_line / 1500
        )
        l24 = lerp_pos(
            l23,
            l34,
            x_line / 1500
        )

        if not draw_mode:
            c13 = lerp_color(c12, c23, x_line / 1500)
            c24 = lerp_color(c23, c34, x_line / 1500)
            screen.set_at(lerp_pos(l13, l24, x_line / 1500), lerp_color(c13, c24, x_line / 1500))
            if x_line % 150 >= 75:
                screen.set_at(lerp_pos(p1, p2, x_line / 1500), lerp_color(c1, c2, x_line / 1500))
                screen.set_at(lerp_pos(p3, p4, x_line / 1500), lerp_color(c3, c4, x_line / 1500))
                screen.set_at(lerp_pos(p2, p3, x_line / 1500), lerp_color(c2, c3, x_line / 1500))
            if x_line % 70 >= 35:
                screen.set_at(l13, c13)
                screen.set_at(l24, c24)
                screen.set_at(lerp_pos(pb13, pb24, x_line / 1500), lerp_color(cb13, cb24, x_line / 1500))
                screen.set_at(lerp_pos(pb12, pb23, x_line / 1500), lerp_color(cb12, cb23, x_line / 1500))
                screen.set_at(lerp_pos(pb23, pb34, x_line / 1500), lerp_color(cb23, cb34, x_line / 1500))
        else:
            screen.set_at(lerp_pos(pb13, pb24, x_line / 1500), lerp_color(cb13, cb24, x_line / 1500))
            screen.set_at(lerp_pos(pb12, pb23, x_line / 1500), lerp_color(cb12, cb23, x_line / 1500))
            screen.set_at(lerp_pos(pb23, pb34, x_line / 1500), lerp_color(cb23, cb34, x_line / 1500))
    
    if not draw_mode:
        pygame.draw.circle(screen, (200, 200, 200), p1, 12)
        pygame.draw.circle(screen, c1, p1, 10)
        pygame.draw.circle(screen, (200, 200, 200), p2, 12)
        pygame.draw.circle(screen, c2, p2, 10)
        pygame.draw.circle(screen, (200, 200, 200), p3, 12)
        pygame.draw.circle(screen, c3, p3, 10)
        pygame.draw.circle(screen, (200, 200, 200), p4, 12)
        pygame.draw.circle(screen, c4, p4, 10)
        pygame.draw.circle(screen, (255, 20, 150), pb12, 12)
        pygame.draw.circle(screen, cb12, pb12, 10)
        pygame.draw.circle(screen, (255, 20, 150), pb23, 12)
        pygame.draw.circle(screen, cb23, pb23, 10)
        pygame.draw.circle(screen, (255, 20, 150), pb34, 12)
        pygame.draw.circle(screen, cb34, pb34, 10)
        pygame.draw.circle(screen, (20, 255, 150), pb13, 12)
        pygame.draw.circle(screen, cb13, pb13, 10)
        pygame.draw.circle(screen, (20, 255, 150), pb24, 12)
        pygame.draw.circle(screen, cb24, pb24, 10)
        pygame.draw.circle(screen, (20, 150, 255), pb, 12)
        pygame.draw.circle(screen, cb, pb, 10)

    pygame.display.update()
    # clock.tick(60)

pygame.quit()
