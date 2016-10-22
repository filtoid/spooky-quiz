import pygame

class Screen2(object):
    def __init__(self):
        self.last_answer = None
        self.last_answer_value = None
        pass

    def draw(self, screen):
        #If last_answer is False then print the error message
        pass

    def update(self, keys):
        #If we answered correctly then return True otherwise false
        return False

    def next(self):
        return None

    def get_error_message(self):
        return "That is incorrect try again"
