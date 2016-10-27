import pygame
from screen2 import Screen2

class Screen1(object):
    def __init__(self):
        self.last_answer = None
        self.last_answer_value = None

	self.MAX_TIMER = 20
	self.cooldown_timer = self.MAX_TIMER 

    def draw(self, screen):
        #If last_answer is False then print the error message
        font = pygame.font.Font(None, 36)
        text = font.render("Question 1", 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.left = 200
        screen.blit(text, textpos)

        question = font.render("Which famous vampire was played by actor Bela", 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.top = 65
        screen.blit(question, q_pos)

	q2 = font.render("Lugosi in a 1931 film?", 1, (255, 255,0))
	q2_pos = q2.get_rect()
	q2_pos.top = q_pos.top + 35
	screen.blit(q2, q2_pos)

        a1 = font.render("a. Alucard", 1, (255, 255, 0))
        a1_pos = a1.get_rect()
        a1_pos.top = q2_pos.top + 45
        screen.blit(a1, a1_pos)

        a2 = font.render("b. Dracula", 1, (255, 255, 0))
        a2_pos = a2.get_rect()
        a2_pos.top = a1_pos.top + 35
        screen.blit(a2, a2_pos)

        a3 = font.render("c. Edward Cullen", 1, (255, 255, 0))
        a3_pos = a3.get_rect()
        a3_pos.top = a2_pos.top + 35
        screen.blit(a3, a3_pos)

        a4 = font.render("d. Orlok", 1, (255, 255, 0))
        a4_pos = a4.get_rect()
        a4_pos.top = a3_pos.top + 35
        screen.blit(a4, a4_pos)

        if self.last_answer is False:
            bad = font.render("That is incorrect. Please try again", 1, (255, 0, 0))
            bad_pos = bad.get_rect()
            bad_pos.top = a4_pos.top + 35
            screen.blit(bad, bad_pos)


    def update(self, keys):

        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return

        #If we answered correctly then return True otherwise false
        if keys[pygame.K_b]:
            return True
        elif keys[pygame.K_a] or keys[pygame.K_c] or keys[pygame.K_d]:
            self.last_answer = False
            self.cooldown_timer = self.MAX_TIMER 
            if keys[pygame.K_b]:
                self.last_answer_value = 'a'
            elif keys[pygame.K_c]:
                self.last_answer_value = 'c'
            elif keys[pygame.K_d]:
                self.last_answer_value = 'd'

        return False

    def next(self):
        return Screen2()

    def get_error_message(self):
        return "That is incorrect try again"
