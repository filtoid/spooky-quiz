import pygame
from menu import Menu

class Victory(object):
    def __init__(self):
        self.last_answer = None
        self.last_answer_value = None
        self.MAX_TIMER = 20
        self.cooldown_timer = self.MAX_TIMER

    def draw(self, screen):
        #If last_answer is False then print the error message
        font = pygame.font.Font(None, 36)
        text = font.render("Congratulations", 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.left = 200
        screen.blit(text, textpos)

        question = font.render("You have finished the quiz", 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.top = 65
        screen.blit(question, q_pos)

        q2 = font.render("Press A, B, C or D to start again", 1, (255, 255,0))
        q2_pos = q2.get_rect()
        q2_pos.top = q_pos.top + 35
        screen.blit(q2, q2_pos)

    def update(self, keys):

        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return

        #If we answered correctly then return True otherwise false
        if keys[pygame.K_c] or keys[pygame.K_b] or keys[pygame.K_d] or keys[pygame.K_a]:
            return True

        return False

    def next(self):
        return Menu()

    def get_error_message(self):
        return "That is incorrect try again"
