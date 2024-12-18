################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Kivi-Paber-Käärid simulatsioon
#
# Autorid: Maria Jansons, Kaur Huko Käämbre
#
# Eeskuju: https://rock0n.itch.io/rock-paper-scissors-simulator
#
# Programmi (mäng.py) käivitamiseks on tarvis teeki pygame (https://www.pygame.org/wiki/GettingStarted)
#
##################################################

import pygame, sys
from pygame.locals import *
from random import *
import shared
from game import game_setup

def check_for_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def tick():
    check_for_quit()
    
    shared.current_tick()
    
    pygame.time.Clock().tick(shared.FPS)

def setup():
    pygame.display.set_caption("rock-paper-scissors")
    
    pygame.init()
    shared.display_surf = pygame.display.set_mode((shared.SCREEN_WIDTH, shared.SCREEN_HEIGHT))
    print(shared.display_surf)
    
    game_setup()
    
    while True:
        tick()
    
setup()
