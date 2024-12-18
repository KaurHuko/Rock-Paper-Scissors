import pygame

VALTER_VALGE = (255, 255, 255)
GANDALF_HALL = (140, 140, 140)

FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

ENTITY_COUNT = 8

current_tick = None
display_surf = None

class Button:
    def __init__(self, x, y, w, h, fun, text = None, image_path = None):
        self.button = pygame.Rect(x, y, w, h)
        if image_path == None:
            pygame.draw.rect(display_surf, GANDALF_HALL, self.button)
        self.function = fun