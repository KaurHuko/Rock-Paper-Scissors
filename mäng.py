################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Kivi-Paber-Käärid simulatsioon
#
# Autorid: Maria Jansons, Kaur Huko Käämbre
#
# mõningane eeskuju: https://rock0n.itch.io/rock-paper-scissors-simulator
##################################################

import pygame, sys
from pygame.locals import *
from random import *

VALGE = (255, 255, 255)

FPS = 30
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

OBJECT_COUNT = 8
OBJECT_TYPES = [
    ("rock", "assets/rock.png"),
    ("paper", "assets/paper.png"),
    ("scissors", "assets/scissors.png")
]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_objects = []


def is_type1_weaker(type1, type2): # Muuda nõrgem tüüp tugevamaks, kui tüübid on erinevad
    if (type1[0] == "rock" and type2[0] == "scissors"): return (type1, type1)
    if (type1[0] == "scissors" and type2[0] == "paper"): return (type1, type1)
    if (type1[0] == "paper" and type2[0] == "rock"): return (type1, type1)
    
    if (type2[0] == "rock" and type1[0] == "scissors"): return (type2, type2)
    if (type2[0] == "scissors" and type1[0] == "paper"): return (type2, type2)
    if (type2[0] == "paper" and type1[0] == "rock"): return (type2, type2)
    
    return (type1, type2)

class GameObject(pygame.sprite.Sprite): # Game objekt on kas kivi/paber/käärid

    def __init__(self, type):
        super().__init__()
        
        self.set_type(type)
        
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, SCREEN_WIDTH-50), randint(50, SCREEN_HEIGHT-50))
        
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)

    def set_type(self, type):
        self.type = type
        self.image = pygame.image.load(type[1])
    
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
        for other in game_objects:
            if (not pygame.sprite.collide_rect(self, other)):
                continue
            
            if (self.is_weaker_than(other)):
                self.set_type(other.type)
    
    def is_weaker_than(self, other):
        self_type = self.type[0]
        other_type = other.type[0]
        
        if (other_type == "rock" and self_type == "scissors"): return True
        if (other_type == "scissors" and self_type == "paper"): return True
        if (other_type == "paper" and self_type == "rock"): return True
        
        return False
        
    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

def tick():
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(VALGE)
    
    # Objekti liigutamine ja joonistamine
    for game_object in game_objects:
        game_object.tick()
        
    pygame.display.update()

def setup():
    pygame.display.set_caption("rock-paper-scissors")
    DISPLAYSURF.fill(VALGE)
    
    for type_id in range(3):
        for i in range(OBJECT_COUNT):
            new_object = GameObject(OBJECT_TYPES[type_id])
            game_objects.append(new_object)
    
    while True:
        tick()
        pygame.time.Clock().tick(FPS)
    
setup()