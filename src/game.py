import pygame
from pygame.locals import *
from random import *
import shared

all_entities = None

class EntityType:
    def __init__(self, id, image_source):
        self.id = id
        self.image_source = image_source

ENTITY_TYPES = [
    EntityType("rock", "src/assets/rock.png"),
    EntityType("paper", "src/assets/paper.png"),
    EntityType("scissors", "src/assets/scissors.png")
]

class Entity(pygame.sprite.Sprite): # Entity on kas kivi/paber/käärid

    def __init__(self, type):
        super().__init__()
        
        self.set_type(type)
        
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, shared.SCREEN_WIDTH-50), randint(50, shared.SCREEN_HEIGHT-50))
        
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
        if self.rect.top < 0 or self.rect.bottom > shared.SCREEN_HEIGHT:
            self.dy *= -1
        if self.rect.left < 0 or self.rect.right > shared.SCREEN_WIDTH:
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
        shared.display_surf.blit(self.image, self.rect)

def find_winner():
    potential_winner = all_entities[0]
    for entity in all_entities:
        if (entity.type.id != potential_winner.type.id):
            return None
    return potential_winner

def game_tick(events):
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    for entity in all_entities:
        entity.tick()
        
    potential_winner = find_winner()
    if (potential_winner != None):
        shared.win_setup(potential_winner.type)
    
def game_setup():
    shared.display_surf.fill(shared.VALTER_VALGE)
    
    global all_entities
    all_entities = []
    
    for i in range(shared.ENTITY_COUNT):
        for entity_type in ENTITY_TYPES:
            new_entity = Entity(entity_type)
            all_entities.append(new_entity)
    
    shared.current_tick = game_tick

shared.game_setup = game_setup