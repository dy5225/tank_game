import pygame
from ui.locals import *
from ui.action import *
import time


class PlayerTank(Display, Move):

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.images = [
            pygame.image.load("img/p1tankU.gif"),
            pygame.image.load("img/p1tankD.gif"),
            pygame.image.load("img/p1tankL.gif"),
            pygame.image.load("img/p1tankR.gif")
        ]
        self.direction = Direction.UP
        # surface
        self.surface = kwargs["surface"]
        # speed
        self.speed = 2
        # 错误的方向
        self.bad_direction = Direction.NONE
        # width,height
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        # 飞机的子弹属性
        self.bullets = []

        # 开火时间间隔
        self.__fire_start = 0
        self.__fire_time = 0.4

    def display(self):
        image = None
        if self.direction == Direction.UP:
            image = self.images[0]
        elif self.direction == Direction.DOWN:
            image = self.images[1]
        elif self.direction == Direction.LEFT:
            image = self.images[2]
        elif self.direction == Direction.RIGHT:
            image = self.images[3]
        self.surface.blit(image, (self.x, self.y))
        Bullet


    def move(self, direction):
        """移动"""

        if direction == self.bad_direction:
            return
        '''==================== 换成了转方向+移动??????? ===================='''

        if self.direction != direction:
            self.direction = direction



        else:
            # 方向相同
            if direction == Direction.UP:
                self.y -= self.speed
                if self.y < 0:
                    self.y = 0
            elif direction == Direction.DOWN:
                self.y += self.speed
                if self.y > GAME_HEIGHT - self.height:
                    self.y = GAME_HEIGHT - self.height
            elif direction == Direction.LEFT:
                self.x -= self.speed
                if self.x < 0:
                    self.x = 0
            elif direction == Direction.RIGHT:
                self.x += self.speed
                if self.x > GAME_WIDTH - self.width:
                    self.x = GAME_WIDTH - self.width

    def fire(self):

        print("开火")
        now = time.time()
        if now - self.__fire_start < self.__fire_time:
            return
        self.__fire_start = now

        bullet = Bullet(self.x, self.y, self.surface)
        self.bullets.append(bullet)
        for ele in self.bullets:
            ele.display()


    def is_blocked(self, block):
        # 判断坦克和墙是否碰撞

        # 判断坦克下一步的矩形和现在的墙是否碰撞
        next_x = self.x
        next_y = self.y

        if self.direction == Direction.UP:
            next_y -= self.speed
            if next_y < 0:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.DOWN:
            next_y += self.speed
            if next_y > GAME_HEIGHT - self.height:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.LEFT:
            next_x -= self.speed
            if next_x < 0:
                self.bad_direction = self.direction
                return True
        elif self.direction == Direction.RIGHT:
            next_x += self.speed
            if next_x > GAME_WIDTH - self.width:
                self.bad_direction = self.direction
                return True

        # 矩形和矩形的碰撞, 当前矩形
        rect_self = pygame.Rect(next_x, next_y, self.width, self.height)
        rect_wall = pygame.Rect(block.x, block.y, block.width, block.height)

        collide = pygame.Rect.colliderect(rect_self, rect_wall)
        if collide:
            # 如果发生了碰撞，说明当前方向是错误的
            self.bad_direction = self.direction
            return True
        else:
            # 没有错误方向
            self.bad_direction = Direction.NONE
            return False


class Wall(Display, Block):

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/walls.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def destroy(self):
        pass


class Steel(Display, Block):
    """铁墙"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/steels.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))


class Water(Display, Block):
    """水"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/water.gif")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))


class Grass(Display, Order):
    """丛林"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/grass.png")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def get_order(self):
        return 100


class Bullet:
    def __init__(self, x, y, surface):
        self.surface = surface
        self.image = pygame.image.load('img/tankmissile.gif')
        self.bullet_width = self.image.get_width()
        self.bullet_height = self.image.get_height()
        self.x = x + BLOCK / 2 - self.bullet_width / 2
        self.y = y - BLOCK

    def move(self):
        '''子弹移动'''
        self.y -= 1

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))
