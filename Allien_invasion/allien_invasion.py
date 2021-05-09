import sys
import pygame
from settings import Settings 
from ship import Ship
import game_functions as gf 


def run_game():
    #initialize game and create a screen object

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Allien Invasion")

    #creat a ship
    ship = Ship(ai_settings, screen)
    

    #set background color
    bg_color = (230, 230, 230)

    #start the main loop for the game
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        #watch for keyboard and mouse events.
        #redraw the screen during each pass through th eloop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #sys.exit()
        
        #make the most recently drawn screen visible

        pygame.display.flip()

run_game()