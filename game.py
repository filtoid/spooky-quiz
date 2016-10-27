import pygame
from menu import Menu
from victory import Victory

class Game(object):

    def __init__(self):
        self.cur_screen = Menu()
        pass

    def update(self, keys):
        if self.cur_screen.update(keys):
            if self.cur_screen.next() is None:
                self.cur_screen = Victory()
            else:
                self.cur_screen = self.cur_screen.next()

    def draw(self, screen):
        self.cur_screen.draw(screen)
