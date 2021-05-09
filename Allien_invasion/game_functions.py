import sys
import pygame

def check_keydown_events(ship):
    """respond to keypressses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_evnet(event, ship)
            
            if event.key == pygame.K_Right:
                #move the ship to the right
                #ship.rect.centerx += 1
                ship.moving_right = True
            
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            
        elif event.type == pygame.KEYUP:
            check_keydown_evnet(event, ship)
            
            if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                    ship.moving_right = False

def check_keyup_event(event, ship):
    """respond to keypressses and mouse events"""

def update_screen(ai_settings, screen, ship):
    """update images on the screen and flip to the new screen"""
    #draw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #make the most recent drawn screen visible
    pygame.display.flip()
