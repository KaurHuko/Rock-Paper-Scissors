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

VALGE = (255, 255, 255)

FPS = 30
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

ENTITY_COUNT = 8

class EntityType:
    def __init__(self, id, image_source):
        self.id = id
        self.image_source = image_source

ENTITY_TYPES = [
    EntityType("rock", "assets/rock.png"),
    EntityType("paper", "assets/paper.png"),
    EntityType("scissors", "assets/scissors.png")
]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
current_tick = None
all_entities = []

class Entity(pygame.sprite.Sprite): # Entity on kas kivi/paber/käärid

    def __init__(self, type):
        super().__init__()
        
        self.set_type(type)
        
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, SCREEN_WIDTH-50), randint(50, SCREEN_HEIGHT-50))
        
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)

    def set_type(self, type):
        self.type = type
        self.image = pygame.image.load(type.image_source)
    
    def tick(self):
        self.move()
        self.collide_with_others()
        self.draw()

    def move(self):
        # Muuda kiirust vähehaaval, et sujuvam liikumine
        if randint(0, 20) == 0:  # Väike võimalus suuna muutmiseks
            self.dx += randint(-1, 1)
            self.dy += randint(-1, 1)

        # Piira kiirus maksimaalselt 3-ga
        self.dx = max(-3, min(self.dx, 3))
        self.dy = max(-3, min(self.dy, 3))

        # Kontrolli piire ja põrka tagasi, kui on servas
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy *= -1
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
        
        # Uuenda positsiooni
        self.rect.move_ip(self.dx, self.dy)
        
    def collide_with_others(self):
        for other in all_entities:
            if (not pygame.sprite.collide_rect(self, other)):
                continue
            
            if (self.is_weaker_than(other)):
                self.set_type(other.type)
    
    def is_weaker_than(self, other):
        self_type = self.type.id
        other_type = other.type.id
        
        if (other_type == "rock" and self_type == "scissors"): return True
        if (other_type == "scissors" and self_type == "paper"): return True
        if (other_type == "paper" and self_type == "rock"): return True
        
        return False
        
    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

def check_for_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def find_winner():
    potential_winner = all_entities[0].type.id
    for entity in all_entities:
        if (entity.type.id != potential_winner):
            return None
    return potential_winner

def game_tick():
    DISPLAYSURF.fill(VALGE)
    
    for entity in all_entities:
        entity.tick()
        
    pygame.display.update()
    
    potential_winner = find_winner()
    if (potential_winner != None):
        print(potential_winner + " won")
        global current_tick
        current_tick = win_menu_tick
    
def win_menu_tick():
    pass

def tick():
    check_for_quit()
    
    global current_tick
    current_tick()
    
    pygame.time.Clock().tick(FPS)

def setup():
    pygame.display.set_caption("rock-paper-scissors")
    
    DISPLAYSURF.fill(VALGE)
    
    for i in range(ENTITY_COUNT):
        for entity_type in ENTITY_TYPES:
            new_entity = Entity(entity_type)
            all_entities.append(new_entity)
    
    global current_tick
    current_tick = game_tick
    
    while True:
        tick()
    
setup()