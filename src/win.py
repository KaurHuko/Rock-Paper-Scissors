import pygame
from pygame.locals import *
import shared
from pygame_widgets.button import Button
import pygame_widgets

def add_button(y, onClick, text):
    button_w = 250
    button_x = (shared.SCREEN_WIDTH - button_w) / 2
    
    button = Button(shared.display_surf,
                    button_x, y, button_w, 60,
                    onClick=onClick,
                    text=text, font=shared.font(),
                    radius=15,
    )
    shared.widgets.append(button)

def win_setup(winner):
    shared.uireset()
    
    winnerimg = pygame.image.load(winner.image())
    winnerimg = pygame.transform.scale(winnerimg, (200, 200))
    shared.display_surf.blit(winnerimg, (200, 225))
    
    winnername = winner.id[0].upper() + winner.id[1:]
    winnertext = (winnername + " wins!")
    font = shared.font(80)
    winnertext = font.render(winnertext, True, (0, 0, 0))
    text_rect = winnertext.get_rect(center=(300, 100))
    shared.display_surf.blit(winnertext, text_rect)
    
    add_button(500, shared.game_setup, "Restart")
    add_button(600, shared.start_setup, "Main Menu")
    add_button(700, pygame.quit, "Quit")
    
    shared.current_tick = win_tick

def win_tick(events):
    pass

shared.win_setup = win_setup