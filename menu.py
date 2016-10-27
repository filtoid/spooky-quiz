import pygame
from screen1 import Screen1

class Menu(object):
    def __init__(self):
        self.last_answer = None
        self.last_answer_value = None
        self.MAX_TIMER = 20
        self.cooldown_timer = self.MAX_TIMER

    def draw(self, screen):
        #If last_answer is False then print the error message
        font = pygame.font.Font(None, 36)
        text = font.render("Spooky Quiz", 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.left = 200
        screen.blit(text, textpos)

        question = font.render("Press A, B, C or D to start", 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.top = 65
        screen.blit(question, q_pos)


    def update(self, keys):

        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return

        #If we answered correctly then return True otherwise false
        if keys[pygame.K_b] or keys[pygame.K_a] or keys[pygame.K_c] or keys[pygame.K_d]:
            return True
        # elif keys[pygame.K_a] or keys[pygame.K_c] or keys[pygame.K_d]:
        #     self.last_answer = False
        #     self.cooldown_timer = self.MAX_TIMER
        #     if keys[pygame.K_b]:
        #         self.last_answer_value = 'a'
        #     elif keys[pygame.K_c]:
        #         self.last_answer_value = 'c'
        #     elif keys[pygame.K_d]:
        #         self.last_answer_value = 'd'

        return False

    def next(self):
        return Screen1()

    def get_error_message(self):
        return "That is incorrect try again"
