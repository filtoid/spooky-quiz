import pygame
from game import Game

def draw(screen, game):
    screen.fill((0, 0, 0))
    game.draw(screen)
    pygame.display.flip()
    pass

def main(game):

    size = width, height = (600, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Poke-man')

    quit = False
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            quit = True
        game.update(keys)
        draw(screen, game)
    pass

if __name__ == '__main__':
    pygame.init()
    game = Game()
    main(game)
