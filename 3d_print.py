import pygame, math, sys

square_vertex = ((1, 1, 1),
                 (-1, 1, 1),
                 (1, -1, 1),
                 (-1, -1, 1),
                 (1, 1, -1),
                 (-1, 1, -1),
                 (1, -1, -1),
                 (-1, -1, -1),)
square_edge = ((0, 4),
               (1, 5),
               (2, 6),
               (3, 7),
               (0, 1),
               (2, 3),
               (4, 5),
               (6, 7),
               (0, 2),
               (1, 3),
               (4, 6),
               (5, 7),)


def d2_set(x, y, a):
    ox = math.cos(math.radians(deg(x, y) + a)) * math.sqrt(x ** 2 + y ** 2)
    oy = math.sin(math.radians(deg(x, y) + a)) * math.sqrt(x ** 2 + y ** 2)
    return ox, oy


def deg(a, b):
    if b == 0:
        return 0
    else:
        return math.degrees(math.acos(a / math.sqrt(a ** 2 + b ** 2)) * b / abs(b))


def square_printing(cx, cy, cz, ax, ay, az, a, b):
    graphic_vertex = []
    for point in square_vertex:
        graphic_vertex.append((point[0] * ax / 2 + cx, point[1] * ay / 2 + cy, point[2] * az / 2 + cz))
    for point in square_edge:
        points = []
        for i in point:
            x,y,z = graphic_vertex[i]
            x, z = d2_set(x,z,fa)
            f = 400/z
            x = x * f
            y = y * f
            points.append((x+400,y+300))
        pygame.draw.lines(screen, 'white', False, points, width=3)


def play():
    screen.fill(background_colour)
    square_printing(0, 0, 20, 10, 10, 10, 0, 0)
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()  # 使用pygame之前必须初始化
    ScreenX, ScreenY = 800, 600
    screen = pygame.display.set_mode((ScreenX, ScreenY))  # 设置主屏窗口
    background_colour = (0, 0, 0)
    screen.fill(background_colour)  # 背景颜色
    clock = pygame.time.Clock()
    pygame.display.set_caption('hello world')  # 设置窗口的标题，即游戏名称
    pygame.display.flip()

    cax, cay, caz = 0, 0, 0
    fa, fb = 0, 0
    FOV = 60
    SPACENOW = True
    pause = False
    mouse_pos = []
    while True:
        fa = fa % 360
        fb = fb % 360
        clock.tick(60)
        play()
        fa += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判断用户是否点了"X"关闭按钮,并执行if代码段
                pygame.quit()  # 卸载所有模块
                sys.exit()  # 终止程序，确保退出程序

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            cax += 0.6
        if keys[pygame.K_a]:
            cax -= 0.6
        if keys[pygame.K_w]:
            caz += 0.6
        if keys[pygame.K_s]:
            caz -= 0.6
        if keys[pygame.K_SPACE]:
            if SPACENOW:
                pause = not pause
                SPACENOW = False
        else:
            SPACENOW = True
        if pause:
            pygame.mouse.set_visible(True)
            mouse_pos = []
        else:
            pygame.mouse.set_visible(False)
            mouse_pos.append(pygame.mouse.get_pos())
        if len(mouse_pos) >= 2:
            fa -= mouse_pos[-2][0] - mouse_pos[-1][0]  # + shun
            fb += mouse_pos[-2][1] - mouse_pos[-1][1]
            mouse_pos = []
            pygame.mouse.set_pos((ScreenX / 2, ScreenY / 2))
