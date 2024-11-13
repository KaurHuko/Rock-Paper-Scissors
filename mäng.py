import pygame, sys
from pygame.locals import *
from random import *

pygame.init()
 
FPS = 30
FramePerSec = pygame.time.Clock()

valge = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(valge)
pygame.display.set_caption("rock-paper-scissors")

class Paper(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("paper.png")
        self.rect = self.image.get_rect()
        self.rect.center=(randint(50,SCREEN_WIDTH-50),randint(50, SCREEN_HEIGHT-50)) 
 
      def move(self):
        self.rect.move_ip(randint(-10,10),randint(-10, 10))
        if (self.rect.top <= 0):
            self.rect.move_ip(randint(-10,10), randint(0, 10))
        if (self.rect.right >= 400):
            self.rect.move_ip(randint(-10,0),randint(-5, 5))
        if (self.rect.left <= 0):
            self.rect.move_ip(randint(0,10),randint(-5, 5))
        if (self.rect.bottom >= 600):
            self.rect.move_ip(randint(-10,10),randint(-10, 0))
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
        
class Rock(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect()
        self.rect.center=(randint(50,SCREEN_WIDTH-50),randint(50, SCREEN_HEIGHT-50)) 
 
      def move(self):
        self.rect.move_ip(randint(-10,10),randint(-10, 10))
        if (self.rect.top <= 0):
            self.rect.move_ip(randint(-10,10), randint(0, 10))
        if (self.rect.right >= 400):
            self.rect.move_ip(randint(-10,0),randint(-5, 5))
        if (self.rect.left <= 0):
            self.rect.move_ip(randint(0,10),randint(-5, 5))
        if (self.rect.bottom >= 600):
            self.rect.move_ip(randint(-10,10),randint(-10, 0))
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)   
class Scissors(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("scissors.png")
        self.rect = self.image.get_rect()
        self.rect.center=(randint(50,SCREEN_WIDTH-50),randint(50, SCREEN_HEIGHT-50)) 
 
      def move(self):
        self.rect.move_ip(randint(-10,10),randint(-10, 10))
        if (self.rect.top <= 0):
            self.rect.move_ip(randint(-10,10), randint(0, 10))
        if (self.rect.right >= 400):
            self.rect.move_ip(randint(-10,0),randint(-5, 5))
        if (self.rect.left <= 0):
            self.rect.move_ip(randint(0,10),randint(-5, 5))
        if (self.rect.bottom >= 600):
            self.rect.move_ip(randint(-10,10),randint(-10, 0))
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)   
 
         
R = Rock()
P = Paper()
S = Scissors()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    R.move()
    P.move()
    S.move()
     
    DISPLAYSURF.fill(valge)
    R.draw(DISPLAYSURF)
    P.draw(DISPLAYSURF)
    S.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)