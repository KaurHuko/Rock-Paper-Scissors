import pygame

class EntityType:
    def __init__(self, id, count, images):
        self.id = id
        self.count = count
        self.images = images
        self.image_index = 0
    
    def image(self):
        return self.images[self.image_index]

ENTITY_TYPES = [
    EntityType("rock", 10, ["src/assets/rock/rock.png", "src/assets/rock/kivirähk.png", "src/assets/rock/classic_rock.png", "src/assets/rock/hand-o-rock.png"]),
    EntityType("paper", 10, ["src/assets/paper/paper.png", "src/assets/paper/hand-o-stop.png"]),
    EntityType("scissors", 10, ["src/assets/scissors/scissors.png", "src/assets/scissors/hand-o-scissors.png"])
]

VALTER_VALGE = (255, 255, 255)
GANDALF_HALL = (140, 140, 140)

FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

def font(font_size=40):
    return pygame.font.SysFont("Comic Sans MS", font_size)

def uireset():
    display_surf.fill(VALTER_VALGE)
    for button in widgets:
        button.hide()
    button = []

current_tick = None
display_surf = None

game_setup = None
start_setup = None
win_setup = None

widgets = []