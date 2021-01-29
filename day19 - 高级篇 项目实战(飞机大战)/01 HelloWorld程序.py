"""游戏的入口"""

import pygame
import sys


def run_game():
    """运行游戏"""
    # 初始化pygame库
    pygame.init()

    # 创建指定尺寸的窗口(游戏画面的所有元素都将在创建的这个窗口中绘制)
    windows = pygame.display.set_mode((700, 900))

    # 设置窗口的标题
    pygame.display.set_caption("飞机大战")
    # 加载窗口图标
    windows_icon = pygame.image.load("images/my_plane.png")
    # 设置窗口图标
    pygame.display.set_icon(windows_icon)
    # 加载飞机图片
    my_plane = pygame.image.load("images/my_plane.png")
    # 飞起的初始y坐标
    pos_y = 774

    # 让创建窗口一直显示
    while True:
        # 从事件队列中将所有事件全部取出并逐个进行处理
        for event in pygame.event.get():
            # 如果某个事件是退出程序

            # 退出程序
            if event.type == pygame.QUIT:
                # 卸载pygame库
                pygame.quit()
                # 退出程序
                sys.exit()
        # 设置窗口的背景色
        windows.fill(pygame.Color("lightskyblue"))
        # 在窗口的指定位置绘制一架飞机
        windows.blit(my_plane, (299, pos_y))
        # 将内存中的窗口对象绘制到屏幕上以更新屏幕

        pygame.display.flip()

        # 创建一个用于跟踪时间的时钟对象

        clock = pygame.time.Clock()

        # 设置while循环体在一秒内执行的最大次数(设置动画的最大帧率)
        clock.tick(30)

        # 减少飞机的y坐标以向上移动
        pos_y -= 20


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    run_game()
