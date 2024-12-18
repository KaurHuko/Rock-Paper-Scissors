import pygame
from pygame.locals import *
import shared
from game import game_setup

buttons = []

def start_setup():
    
    print("a")
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    button = pygame.Rect(80, 300, 100, 50)
    pygame.draw.rect(shared.display_surf, shared.GANDALF_HALL, button)
    buttons.append((button, game_setup))
    
    shared.current_tick = start_tick

def start_tick(events):
    for event in events:
        if event.type != MOUSEBUTTONDOWN: continue
    
        for (button, event_func) in buttons:
            if button.collidepoint(event.pos):
                event_func()