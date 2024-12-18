import pygame
from pygame.locals import *
import shared
from game import game_setup

buttons = []

def start_setup():
    
    print("a")
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    button = shared.Button(80, 300, 100, 50, game_setup)
    buttons.append(button)
    
    shared.current_tick = start_tick

def start_tick(events):
    for event in events:
        if event.type != MOUSEBUTTONDOWN: continue
    
        for button in buttons:
            if button.button.collidepoint(event.pos):
                button.function()