import pygame
from pygame.locals import *
import shared

buttons = []

def win_setup(winner):
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    print(winner)
    
    button_x = (shared.SCREEN_WIDTH) / 2
    
    buttons.append(shared.Button(button_x, 500, 250, 60, shared.game_setup, "Restart"))
    buttons.append(shared.Button(button_x, 600, 250, 60, shared.start_setup, "Main Menu"))
    buttons.append(shared.Button(button_x, 700, 250, 60, pygame.quit, "Quit"))
    
    shared.current_tick = win_tick

def win_tick(events):
    for event in events:
        if event.type != MOUSEBUTTONDOWN: continue
    
        for button in buttons:
            if button.button.collidepoint(event.pos):
                button.function()

shared.win_setup = win_setup