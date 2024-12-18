import pygame
from pygame.locals import *
import shared
from pygame_widgets.button import Button
import pygame_widgets

buttons = []

def add_button(y, onClick, text):
    button_w = 250
    button_x = (shared.SCREEN_WIDTH - button_w) / 2
    
    button = Button(shared.display_surf,
                    button_x, y, button_w, 60,
                    onClick=onClick,
                    text=text, font=shared.FONT,
                    radius=15,
    )
    buttons.append(button)


def start_setup():
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    add_button(300, shared.game_setup, "Start Game")
    add_button(400, pygame.quit, "Quit")
    
    logo = pygame.image.load("src/assets/logo.png")
    logo = pygame.transform.scale(logo, (600, 268))
    logo_rect = logo.get_rect(center=(300, 150))
    shared.display_surf.blit(logo, logo_rect)
    shared.current_tick = start_tick

def start_tick(events):
    pygame_widgets.update(events)
    
    for button in buttons:
        button.draw()
        button.listen(events)
    
    for event in events:
        if event.type != MOUSEBUTTONDOWN: continue
    
shared.start_setup = start_setup