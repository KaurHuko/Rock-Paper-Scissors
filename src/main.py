import pygame, sys
from pygame.locals import *
from random import *
import pygame_widgets

import shared

# Import to load start event functions
import game
import startmenu
import win

def check_for_quit(events):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def check_for_buttons(events):
    pygame_widgets.update(events)

def tick():
    events = pygame.event.get()
    check_for_quit(events)
    check_for_buttons(events)
    shared.current_tick(events)
    
    pygame.display.update()
    
    pygame.time.Clock().tick(shared.FPS)

def setup():
    pygame.display.set_caption("rock-paper-scissors")
    
    pygame.init()
    pygame.font.init()
    shared.display_surf = pygame.display.set_mode((shared.SCREEN_WIDTH, shared.SCREEN_HEIGHT))
        
    shared.start_setup()
    
    while True:
        tick()
    
setup()
