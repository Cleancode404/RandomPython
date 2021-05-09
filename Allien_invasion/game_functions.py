import sys
import pygame

def check_events():
    """respond to keypressses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()