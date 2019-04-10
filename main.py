"""
创建窗体
"""
import pygame
import sys
from pygame.locals import *
from ui.locals import *
from ui.page import *

if __name__ == '__main__':
    pygame.init()

    # 窗体
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("坦克大战")

    # 两个页面
    start = StartPage(window)
    game = GamePage(window)

    while True:
        # 获取当前要打开页面的值
        current = getCurrent()

        # 判断页面
        page = None
        if current == 0:
            page = start
        elif current == 1:
            page = game

        # 渲染页面
        page.graphic()
        # 刷新
        pygame.display.flip()

        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                # 为页面传递事件
                page.keydown(event.key)

        keys = pygame.key.get_pressed()
        # 为页面传递事件
        page.keypress(keys)
