import sys
import pygame

def run_game():
    #initialize game and create a screen object

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Allien Invasion")

    #set background color
    bg_color = (230, 230, 230)

    #start the main loop for the game
    while True:

        #watch for keyboard adn mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #make th emost recently drawn screen visible

        pygame.display.flip()

run_game()