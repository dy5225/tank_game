from ui.view import *
from pygame.locals import *


class GameContainer:
    """

    """

    # 1. 可以通过列表去管理所有的显示元素
    # 2.

    def __init__(self, surface):
        self.surface = surface
        self.views = []

        # 通过读文件来加载元素
        file = open("map/1.map", "r", encoding="utf-8")

        # row = 0
        # for line in file:
        #     print(line)
        #     row += 1

        for row, line in enumerate(file):
            # 去掉换行符
            texts = line.strip()
            for column, text in enumerate(texts):
                # print("row:{} column:{} text:{}".format(row, column, text))
                x = column * BLOCK
                y = row * BLOCK
                if text == "砖":
                    self.views.append(Wall(surface=self.surface, x=x, y=y))
                if text == "铁":
                    self.views.append(Steel(surface=self.surface, x=x, y=y))
                if text == "水":
                    self.views.append(Water(surface=self.surface, x=x, y=y))
                # if text == "草":
                #     self.views.append(Grass(surface=self.surface, x=x, y=y))
                if text == "主":
                    self.player = PlayerTank(surface=self.surface, x=x, y=y)
                    self.views.append(self.player)

        file.close()

    def __sort(self, view):
        # if isinstance(view, Order):
        #     return view.get_order()
        # else:
        #     return 0
        return view.get_order() if isinstance(view, Order) else 0

    def graphic(self):
        """渲染"""
        # 清屏
        self.surface.fill((0x00, 0x00, 0x00))

        # 对列表进行排序，排序的标准
        # self.views.sort(key=lambda view: view.get_order() if isinstance(view, Order) else 0)
        self.views.sort(key=self.__sort)
        # self.views = sorted(self.views,key=self.__sort)
        l = []
        # 遍历列表，让所有的元素显示
        for view in self.views:
            view.display()



        # 判断墙和坦克是否发生碰撞
        # 判断 可移动的物体 是否和 可阻挡移动的物体 发生了碰撞
        # for view in self.views:
        #     if isinstance(view, Wall):
        #         # 墙
        #         if self.player.is_blocked(view):
        #             # 墙和坦克碰撞
        #             break

        # for block in self.views:
        #     # 找出所有可阻塞移动的物体
        #     if isinstance(block, Block):
        #         for move in self.views:
        #             if isinstance(move, Move):
        #                 if move.is_blocked(block):
        #                     # 移动的物体被阻塞的物体挡住了
        #                     break

        for move in self.views:
            if isinstance(move, Move):
                for block in self.views:
                    # 找出所有可阻塞移动的物体
                    if isinstance(block, Block):
                        if move.is_blocked(block):
                            # 移动的物体被阻塞的物体挡住了
                            break

    def keydown(self, key):
        """按下事件"""
        pass

    def keypress(self, keys):
        """长按事件"""
        if keys[K_a]:
            # 向左移动
            self.player.move(Direction.LEFT)
        if keys[K_d]:
            # 向右移动
            self.player.move(Direction.RIGHT)
        if keys[K_w]:
            self.player.move(Direction.UP)
        if keys[K_s]:
            self.player.move(Direction.DOWN)


class InfoContainer:
    def __init__(self, surface):
        self.surface = surface

    def graphic(self):
        """渲染"""
        self.surface.fill((0x00, 0x00, 0xff))
