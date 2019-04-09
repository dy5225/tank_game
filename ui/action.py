from abc import *


# abstract class


class Display(metaclass=ABCMeta):
    """
    抽象类：规范显示行为
    """
    @abstractmethod
    def display(self):
        """显示"""
        pass


class Move(metaclass=ABCMeta):
    """移动的规范"""

    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def is_blocked(self, block):
        pass


class Block(metaclass=ABCMeta):
    """阻塞的规范"""
    pass


class Order(metaclass=ABCMeta):
    """排序显示"""

    @abstractmethod
    def get_order(self):
        pass