import pygame

FONT = None

VALTER_VALGE = (255, 255, 255)
GANDALF_HALL = (140, 140, 140)

FPS = 600
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

ENTITY_COUNT = 8

current_tick = None
display_surf = None

game_setup = None
start_setup = None
win_setup = None

class Button:
    def __init__(self, x, y, w, h, fun, text = None, image_path = None):
        left_x = x - w/2
        left_y = y - h/2
        
        self.button = pygame.Rect(left_x, left_y, w, h)
        self.function = fun
        
        if image_path == None:
            pygame.draw.rect(display_surf, GANDALF_HALL, self.button)
        
        if (text != None):
            font = pygame.font.SysFont("Comic Sans MS", 40)
            text = font.render(text, True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            display_surf.blit(text, text_rect)