import pygame, sys
from pygame.locals import *
from random import *

pygame.init()
 
FPS = 30
FramePerSec = pygame.time.Clock()

valge = (255, 255, 255)

object_types = [
    ("rock", "assets/rock.png"),
    ("paper", "assets/paper.png"),
    ("scissors", "assets/scissors.png")
]

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(valge)
pygame.display.set_caption("rock-paper-scissors")

class GameObject(pygame.sprite.Sprite):

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

    def move(self):
        # Muuda kiirust vähehaaval, et sujuvam liikumine
        if randint(0, 20) == 0:  # Väike võimalus suuna muutmiseks
            self.dx += randint(-1, 1)
            self.dy += randint(-1, 1)

        # Piira kiirus maksimaalselt 3-ga
        self.dx = max(-3, min(self.dx, 3))
        self.dy = max(-3, min(self.dy, 3))

        # Kontrolli piire ja põrka tagasi, kui on servas
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy *= -1
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx *= -1
        
        # Uuenda positsiooni
        self.rect.move_ip(self.dx, self.dy)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

rock = GameObject(object_types[0])
paper = GameObject(object_types[1])
scissors = GameObject(object_types[2])
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Objekti liigutamine ja joonistamine
    rock.tick()
    paper.tick()
    scissors.tick()
     
    DISPLAYSURF.fill(valge)
    rock.draw(DISPLAYSURF)
    paper.draw(DISPLAYSURF)
    scissors.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
