import pygame, sys
from pygame.locals import *
from random import *

pygame.init()
 
FPS = 30
FramePerSec = pygame.time.Clock()

valge = (255, 255, 255)
must = (0, 0, 0)
hall = (200, 200, 200)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(valge)
pygame.display.set_caption("rock-paper-scissors")

# Tekstide jaoks font
font = pygame.font.SysFont("Arial", 24)

# Defineerime klassid
class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = "Paper"
        self.image = pygame.image.load("assets/paper.png")
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

    def transform_to(self, new_type):
        """Muudab objekti tüüpi (pilt ja tüüp)."""
        if new_type == "Rock":
            self.image = pygame.image.load("assets/rock.png")
            self.type = "Rock"
        elif new_type == "Scissors":
            self.image = pygame.image.load("assets/scissors.png")
            self.type = "Scissors"
        elif new_type == "Paper":
            self.image = pygame.image.load("assets/paper.png")
            self.type = "Paper"

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Rock(Paper):  # Pärib omadused Paper klassilt
    def __init__(self):
        super().__init__()
        self.type = "Rock"
        self.image = pygame.image.load("assets/rock.png")

class Scissors(Paper):  # Pärib omadused Paper klassilt
    def __init__(self):
        super().__init__()
        self.type = "Scissors"
        self.image = pygame.image.load("assets/scissors.png")

# Funktsioon kollisioonide kontrolliks ja muundamiseks
def check_collision(obj1, obj2):
    if pygame.sprite.collide_rect(obj1, obj2):
        if obj1.type == "Rock" and obj2.type == "Scissors":
            obj2.transform_to("Rock")
        elif obj2.type == "Rock" and obj1.type == "Scissors":
            obj1.transform_to("Rock")
        elif obj1.type == "Scissors" and obj2.type == "Paper":
            obj2.transform_to("Scissors")
        elif obj2.type == "Scissors" and obj1.type == "Paper":
            obj1.transform_to("Scissors")
        elif obj1.type == "Paper" and obj2.type == "Rock":
            obj2.transform_to("Paper")
        elif obj2.type == "Paper" and obj1.type == "Rock":
            obj1.transform_to("Paper")

# Algseadistuse funktsioon
def setup_game():
    global objects
    objects = pygame.sprite.Group()
    for _ in range(3):
        objects.add(Rock(), Paper(), Scissors())

def check_game_over():
    types = {obj.type for obj in objects}
    if len(types) == 1:
        return types.pop()
    return None

# Nuppude ja mängu uuendamise funktsioonid
def show_end_screen(winner):
    end_text = font.render(f"{winner} won!", True, must)
    DISPLAYSURF.blit(end_text, (150, 250))

    # Loome kaks nuppu
    close_button = pygame.Rect(80, 300, 100, 50)
    reset_button = pygame.Rect(220, 300, 100, 50)

    pygame.draw.rect(DISPLAYSURF, hall, close_button)
    pygame.draw.rect(DISPLAYSURF, hall, reset_button)

    close_text = font.render("     Quit", True, must)
    reset_text = font.render("   Restart", True, must)
    DISPLAYSURF.blit(close_text, (85, 315))
    DISPLAYSURF.blit(reset_text, (225, 315))

    pygame.display.update()

    # Nuppude kontroll
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if close_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif reset_button.collidepoint(event.pos):
                    setup_game()
                    return

# Mängu algseadistus
setup_game()

# Peamine mängutsükkel
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Liiguta objekte ja kontrolli kokkupõrkeid
    for obj1 in objects:
        obj1.move()
        for obj2 in objects:
            if obj1 != obj2:
                check_collision(obj1, obj2)

    # Kontrolli, kas mäng on läbi
    winner = check_game_over()
    if winner:
        show_end_screen(winner)

    # Mängu joonistamine
    DISPLAYSURF.fill(valge)
    for obj in objects:
        obj.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
