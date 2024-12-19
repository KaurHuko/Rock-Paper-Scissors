import pygame
from pygame.locals import *
import shared
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

sliders = []
outputs = []

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

def draw_option_title(y, text):
    title = TextBox(shared.display_surf,
                     60, y, 30, 30,
                     font=shared.font(40), borderThickness=0, colour=(255, 255, 255, 0))
    title.setText(text)
    shared.widgets.append(title)

def on_icon_choose(button, index):
    entitytype = shared.ENTITY_TYPES[index]
    
    entitytype.image_index = (entitytype.image_index + 1) % len(entitytype.images)
    
    button_image = pygame.image.load(entitytype.image())
    button.setImage(button_image)

def add_icon_choice(y, index):
    button_image = pygame.image.load(shared.ENTITY_TYPES[index].image())
    button = Button(shared.display_surf,
                    420, y + 12, 60, 60,
                    onClick=lambda: on_icon_choose(button, index),
                    image=button_image,
                    inactiveColour=(225, 225, 225),
                    radius=15
    )
    shared.widgets.append(button)
    
    click_tutorial = TextBox(shared.display_surf,
                     395, y - 5, 20, 20,
                     font=shared.font(15), borderThickness=0, colour=(255, 255, 255, 0))
    click_tutorial.setText("(choose icon)")
    shared.widgets.append(click_tutorial)

def add_slider(y):
    index = len(sliders)
    button_w = shared.SCREEN_WIDTH - 150
    button_x = (shared.SCREEN_WIDTH - button_w - 50) / 2
    
    slider = Slider(shared.display_surf,
                    button_x, y, button_w, 15,
                    min=1, max=100, step=1,
                    initial=shared.ENTITY_TYPES[index].count,
                    handleRadius=10
                    
    )
    sliders.append(slider)
    shared.widgets.append(slider)
    
    output = TextBox(shared.display_surf,
                     button_x + button_w + 30, y, 30, 30,
                     font=shared.font(30), borderThickness=0, colour=(255, 255, 255, 0))
    
    output.disable()
    outputs.append(output)
    shared.widgets.append(output)
    
def start_setup():
    shared.uireset()
    
    sliders.clear()
    outputs.clear()
    
    draw_option_title(290, "Rock:")
    add_icon_choice(250, 0)
    add_slider(330)
    
    draw_option_title(420, "Paper:")
    add_icon_choice(370, 1)
    add_slider(450)
    
    draw_option_title(540, "Scissors:")
    add_icon_choice(490, 2)
    add_slider(570)
    
    add_button(650, shared.game_setup, "Start Game")
    add_button(725, pygame.quit, "Quit")
    
    shared.current_tick = start_tick

def draw_tick():
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    logo = pygame.image.load("src/assets/logo.png")
    logo = pygame.transform.scale(logo, (600, 268))
    logo_rect = logo.get_rect(center=(300, 150))
    shared.display_surf.blit(logo, logo_rect)
    
    for widget in shared.widgets:
        widget.draw()
    
    for i in range(len(sliders)):
        outputs[i].setText(sliders[i].getValue())
        pass

def start_tick(events):
    draw_tick()
    
    for i in range(len(sliders)):
        slider = sliders[i]
        shared.ENTITY_TYPES[i].count = slider.getValue()

        
    
shared.start_setup = start_setup