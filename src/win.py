import pygame
from pygame.locals import *
import shared

buttons = []

def win_setup(winner):
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    winnerimg = pygame.image.load(winner.image_source)
    winnerimg = pygame.transform.scale(winnerimg, (200, 200))
    shared.display_surf.blit(winnerimg, (200, 225))
    winnername = winner.id[0].upper() + winner.id[1:]
    winnertext = (winnername + " wins!")
    font = pygame.font.SysFont("Comic Sans MS", 80)
    winnertext = font.render(winnertext, True, (0, 0, 0))
    text_rect = winnertext.get_rect(center=(300, 100))
    shared.display_surf.blit(winnertext, text_rect)
    
    print(winner.id)
    
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