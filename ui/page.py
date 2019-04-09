from pygame.locals import *
from ui.container import *
from ui.locals import *
import pygame

# 0代表start页面1代表game页面
__current = 0


def getCurrent():
    '''获取当前要打开页面的值'''
    return __current


def setCurrent(value):
    global __current
    __current = value


class StartPage:
    """开始页面"""
    def __init__(self, surface):
        self.surface = surface


    def graphic(self):
        """渲染"""
        # self.surface.fill((0x00, 0xff, 0x00))
        img = pygame.image.load('img/timg1.jpg')
        font = pygame.font.Font('font/happy.ttf',40)
        text_font = font.render("按下ENTER开始游戏",True,(0,255,0))
        self.surface.blit(img,(0,0))
        self.surface.blit(text_font,(WINDOW_WIDTH/3,WINDOW_HEIGHT/4))

    def keydown(self, key):
        """按下事件"""

        #改变要进入游戏页面的值
        if key == K_RETURN:
            # 显示game
            setCurrent(1)

    def keypress(self, keys):
        """长按事件"""
        pass


class GamePage:
    '''游戏页面'''
    def __init__(self, surface):
        self.surface = surface
        self.gameSurface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.infoSurface = pygame.Surface((INFO_WIDTH, INFO_HEIGHT))

        self.gameContainer = GameContainer(self.gameSurface)
        self.infoContainer = InfoContainer(self.infoSurface)

    def graphic(self):
        """渲染"""
        self.surface.fill((0x77, 0x77, 0x77))

        # 渲染游戏区
        self.surface.blit(self.gameSurface, (WINDOW_PADDING, WINDOW_PADDING))
        self.gameContainer.graphic()

        # 渲染信息区
        self.surface.blit(self.infoSurface, (2 * WINDOW_PADDING + GAME_WIDTH, WINDOW_PADDING))
        self.infoContainer.graphic()

    def keydown(self, key):
        """按下事件"""
        self.gameContainer.keydown(key)

    def keypress(self, keys):
        """长按事件"""
        self.gameContainer.keypress(keys)
