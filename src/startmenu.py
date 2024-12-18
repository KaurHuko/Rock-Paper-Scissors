import pygame
from pygame.locals import *
import shared

buttons = []

def start_setup():
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    button_width = 200
    button_x = (shared.SCREEN_WIDTH - button_width) / 2
    
    buttons.append(shared.Button(button_x, 300, button_width, 60, shared.game_setup, "Start Game"))
    buttons.append(shared.Button(button_x, 400, button_width, 60, pygame.quit, "Quit"))
    
    shared.current_tick = start_tick

def start_tick(events):
    for event in events:
        if event.type != MOUSEBUTTONDOWN: continue
    
        for button in buttons:
            if button.button.collidepoint(event.pos):
                button.function()

shared.start_setup = start_setup