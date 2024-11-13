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
          self.rect.center = (randint(50, SCREEN_WIDTH-50), randint(50, SCREEN_HEIGHT-50))
          self.dx = randint(-3, 3)
          self.dy = randint(-3, 3)
 
      def move(self):
          # Muuda kiirust vähehaaval, et sujuvam liikumine
          if randint(0, 20) == 0:  # Väike võimalus suuna muutmiseks
              self.dx += randint(-1, 1)
              self.dy += randint(-1, 1)

          # Piira kiirus maksimaalselt 3-ga
          self.dx = max(-3, min(self.dx, 3))
          self.dy = max(-3, min(self.dy, 3))

          # Uuenda positsiooni
          self.rect.move_ip(self.dx, self.dy)

          # Kontrolli piire ja põrka tagasi, kui on servas
          if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
              self.dy *= -1
          if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
              self.dx *= -1
 
      def draw(self, surface):
          surface.blit(self.image, self.rect)

class Rock(pygame.sprite.Sprite):
      def __init__(self):
          super().__init__() 
          self.image = pygame.image.load("rock.png")
          self.rect = self.image.get_rect()
          self.rect.center = (randint(50, SCREEN_WIDTH-50), randint(50, SCREEN_HEIGHT-50))
          self.dx = randint(-3, 3)
          self.dy = randint(-3, 3)
 
      def move(self):
          if randint(0, 20) == 0:
              self.dx += randint(-1, 1)
              self.dy += randint(-1, 1)
          self.dx = max(-3, min(self.dx, 3))
          self.dy = max(-3, min(self.dy, 3))
          self.rect.move_ip(self.dx, self.dy)
          if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
              self.dy *= -1
          if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
              self.dx *= -1
 
      def draw(self, surface):
          surface.blit(self.image, self.rect)

class Scissors(pygame.sprite.Sprite):
      def __init__(self):
          super().__init__() 
          self.image = pygame.image.load("scissors.png")
          self.rect = self.image.get_rect()
          self.rect.center = (randint(50, SCREEN_WIDTH-50), randint(50, SCREEN_HEIGHT-50))
          self.dx = randint(-3, 3)
          self.dy = randint(-3, 3)
 
      def move(self):
          if randint(0, 20) == 0:
              self.dx += randint(-1, 1)
              self.dy += randint(-1, 1)
          self.dx = max(-3, min(self.dx, 3))
          self.dy = max(-3, min(self.dy, 3))
          self.rect.move_ip(self.dx, self.dy)
          if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
              self.dy *= -1
          if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
              self.dx *= -1
 
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

    # Objekti liigutamine ja joonistamine
    R.move()
    P.move()
    S.move()
     
    DISPLAYSURF.fill(valge)
    R.draw(DISPLAYSURF)
    P.draw(DISPLAYSURF)
    S.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
