import pygame, math, sys

cax, cay, caz = 0, 0, 0


def d3_set(x, y, z, a, b):
    ix = math.cos(math.radians(deg(x, z) + a)) * math.sqrt(x ** 2 + z ** 2)
    oz = math.sin(math.radians(deg(x, z) + a)) * math.sqrt(x ** 2 + z ** 2)
    iy = math.sin(math.radians(deg(oz, y) + b)) * math.sqrt(y ** 2 + oz ** 2)
    oz = math.cos(math.radians(deg(oz, y) + b)) * math.sqrt(y ** 2 + oz ** 2)
    return ix, iy, oz


def format_deg(a,b):
    if b == 0:
        return 0
    else:
        return math.degrees(math.acos(a / math.sqrt(a ** 2 + b ** 2)) * b / abs(b))-360*(b / abs(b)-1)/2


def deg(a, b):
    if b == 0:
        return 0
    else:
        return math.degrees(math.acos(a / math.sqrt(a ** 2 + b ** 2)) * b / abs(b))


def play():
    screen.fill(background_colour)
    square_draw1(0,0,3000, 100, 100, 100, 0, 0)
    square_draw1(3000,0,0, 100, 100, 100, 0, 0)
    print_text(f'fa:{fa}', 30, (100, 400), 'midleft')
    print_text(
        f'{deg(float(format(((0 + cax) ** 2 + (100 - caz) ** 2) ** 0.5 * math.cos(math.radians(fa)), ".2f")), float(format(((0 + cax) ** 2 + (100 - caz) ** 2) ** 0.5 * math.sin(math.radians(fa)), ".2f")))}  {format(cay, ".2f")}',
        30, (100, 430), 'midleft')
    print_text(
        f'caxyz {format(cax, ".2f")}  {format(cay, ".2f")}  {format(caz, ".2f")}',
        30, (100, 460), 'midleft')
    pygame.display.flip()
    # print(d3_set(-10,10,10,0,0))


def print_text(in_text, size, place, method, background=(0, 0, 0), color=(255, 255, 255)):
    in_text = str(in_text)
    f = pygame.font.Font('D:\World\words pack\汉仪文黑-85W Heavy.ttf', size)
    if background != (0, 0, 0):
        text = f.render(in_text, True, color, background)
    else:
        text = f.render(in_text, True, color)
    # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
    # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
    textRect = text.get_rect()  # 获得显示对象的rect区域坐标
    exec(f'textRect.{method} = place')
    screen.blit(text, textRect)  # 将准备好的文本信息，绘制到主屏幕 Screen 上。


def square_draw1(cx, cy, cz, ex, ey, ez, a, b):
    # square_draw2(((cx-cax)**2+(cz-caz)**2)**0.5*math.cos(math.radians(fa+deg((cx-cax),(cz-caz)))),
    #              cy,
    #              ((cx-cax)**2+(cz-caz)**2)**0.5*math.sin(math.radians(fa+deg((cx-cax),(cz-caz)))), ex, ey, ez,
    #              deg((cx-cax),(cz-caz))+a, b)
    square_draw2(cx-cax,
                 cy,
                 cz-caz, ex, ey, ez,
                 fa + a, b)
    print_text(f'{deg((cx-cax),(cz-caz))}', 30, (100, 490), 'midleft')
def square_draw2(cx, cy, cz, ex, ey, ez, a, b):
    xx = 0
    for xi in [-1, 1]:
        for zi in [-1, 1]:
            points = []
            for yi in [-1, 1]:
                points.append(d3_set(ex * xi, ey * yi, ez * zi, a, b))
                points[-1] = (((float(format(points[-1][0] + cx, '.3f')) * ((3 ** 0.5) * 400) / (
                             ((3 ** 0.5) * 400) + ((cz + points[-1][2] - caz)**2+(cx + points[-1][0] - cax)**2)**0.5*math.cos(math.radians(deg((caz - cz + points[-1][2]),(cax - cx + points[-1][0]))+0))) + ScreenX / 2)),
                             ((float(format(points[-1][1] + cy, '.3f')) * ((3 ** 0.5) * 400) / (
                             ((3 ** 0.5) * 400) + ((cz + points[-1][2] - caz)**2+(cx + points[-1][0] - cax)**2)**0.5*math.cos(math.radians(deg((caz - cz + points[-1][2]),(cax - cx + points[-1][0]))+0))) + ScreenY / 2)))
            pygame.draw.lines(screen, 'white', False, points, width=3)


    for xi in [-1, 1]:
        for yi in [-1, 1]:
            points = []
            for zi in [-1, 1]:
                points.append(d3_set(ex * xi, ey * yi, ez * zi, a, b))
                points[-1] = (((float(format(points[-1][0] + cx, '.3f')) * ((3 ** 0.5) * 400) / (
                        ((3 ** 0.5) * 400) + (
                            (cz + points[-1][2] - caz) ** 2 + (cx + points[-1][0] - cax) ** 2) ** 0.5 * math.cos(
                    math.radians(deg((caz - cz + points[-1][2]), (cax - cx + points[-1][0])) + 0))) + ScreenX / 2)),
                              ((float(format(points[-1][1] + cy, '.3f')) * ((3 ** 0.5) * 400) / (
                                      ((3 ** 0.5) * 400) + ((cz + points[-1][2] - caz) ** 2 + (
                                          cx + points[-1][0] - cax) ** 2) ** 0.5 * math.cos(math.radians(
                                  deg((caz - cz + points[-1][2]), (cax - cx + points[-1][0])) + 0))) + ScreenY / 2)))
            pygame.draw.lines(screen, 'white', False, points, width=3)
    for yi in [-1, 1]:
        for zi in [-1, 1]:
            points = []
            for xi in [1, -1]:
                points.append(d3_set(ex * xi, ey * yi, ez * zi, a, b))
                points[-1] = (((float(format(points[-1][0] + cx, '.3f')) * ((3 ** 0.5) * 400) / (
                        ((3 ** 0.5) * 400) + (
                            (cz + points[-1][2] - caz) ** 2 + (cx + points[-1][0] - cax) ** 2) ** 0.5 * math.cos(
                    math.radians(deg((caz - cz + points[-1][2]), (cax - cx + points[-1][0])) + 0))) + ScreenX / 2)),
                              ((float(format(points[-1][1] + cy, '.3f')) * ((3 ** 0.5) * 400) / (
                                      ((3 ** 0.5) * 400) + ((cz + points[-1][2] - caz) ** 2 + (
                                          cx + points[-1][0] - cax) ** 2) ** 0.5 * math.cos(math.radians(
                                  deg((caz - cz + points[-1][2]), (cax - cx + points[-1][0])) + 0))) + ScreenY / 2)))
            pygame.draw.lines(screen, 'white', False, points, width=3)


# (ScreenX/2)/(math.cos(math.radians(deg((cx+ex*xi-nx),(cz+ez*zi-nz))-fa))*(((cx+ex*xi-nx)**2+(cz+ez*zi-nz)**2)**0.5)*math.tan(math.radians(FOV/2)))
# *(((cx-nx+ex*xi)**2+(cy-ny+ey*yi)**2+(cz-nz+ez*zi)**2)**(1/2))
# points.append(d3_set(cx + ex * xi, cy + ey * yi, cz + ez * zi, a, b))
# points[-1] = ((float(format(points[-1][0], '.3f')) + ScreenX / 2) * -(zi-1.4),
#               (float(format(points[-1][1], '.3f')) + ScreenY / 2) * -(zi-1.4))


pygame.init()  # 使用pygame之前必须初始化
ScreenX, ScreenY = 800, 600
screen = pygame.display.set_mode((ScreenX, ScreenY))  # 设置主屏窗口
background_colour = (0, 0, 0)
screen.fill(background_colour)  # 背景颜色
clock = pygame.time.Clock()
pygame.display.set_caption('hello world')  # 设置窗口的标题，即游戏名称
pygame.display.flip()

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
