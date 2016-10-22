import pygame
from screen1 import Screen1

class Game(object):

    def __init__(self):
        self.cur_screen = Screen1()
        pass

    def update(self, keys):
        if self.cur_screen.update(keys):
            self.cur_screen = self.cur_screen.next()
        pass

    def draw(self, screen):
        self.cur_screen.draw(screen)
