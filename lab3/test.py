import pygame
from pygame.draw import *

pygame.init()

FPS = 30

#create window
screen = pygame.display.set_mode((600, 800))

#space for drawing
# ...
rect(screen, (0, 0, 0), (0, 0, 600, 800))
rect(screen, (110, 110, 110), (0, 0, 600, 300))

# moon
circle(screen,(255, 255, 255),(544, 63), 45, width=0)

# chimneys below
rect(screen, (40, 40, 40), (87, 85, 8, 60))
rect(screen, (40, 40, 40), (200, 80, 8, 60))
 
# clouds
ellipse(screen, (70, 70, 70), (25, 70, 490, 55))
ellipse(screen, (90, 90, 90), (280, 50, 330, 50))
ellipse(screen, (90, 90, 90), (400, 106, 330, 45))
ellipse(screen, (40, 40, 40), (310, 165, 350, 45))

# roof
polygon(screen, (0, 0, 0), [(0, 170), (40, 140), (320, 140), (360, 170), (0, 170)], width=0)

# wall
rect(screen, (61, 45, 9), (30, 170, 300, 400))

# windows
rect(screen, (56, 10, 5), (60, 430, 60, 90))
rect(screen, (54, 10, 5), (150, 430, 60, 90))
rect(screen, (240, 190, 26), (240, 430, 60, 90))

# planks
rect(screen, (125, 106, 104), (60, 170, 30, 120))
rect(screen, (125, 106, 104), (120, 170, 30, 120))
rect(screen, (125, 106, 104), (210, 170, 30, 120))
rect(screen, (125, 106, 104), (270, 170, 30, 120))

# balcony
rect(screen, (50, 50, 50), (0, 300, 360, 30))
rect(screen, (50, 50, 50), (5, 260, 10, 40))
rect(screen, (50, 50, 50), (15, 250, 330, 10))
rect(screen, (50, 50, 50), (345, 260, 10, 40))
rect(screen, (50, 50, 50), (53, 260, 20, 40))
rect(screen, (50, 50, 50), (111, 260, 20, 40))
rect(screen, (50, 50, 50), (170, 260, 20, 40))
rect(screen, (50, 50, 50), (228, 260, 20, 40))
rect(screen, (50, 50, 50), (286, 260, 20, 40))

# chimneys above
rect(screen, (40, 40, 40), (100, 70, 15, 80))
rect(screen, (40, 40, 40), (292, 100, 8, 60))

# ghost
def draw_head(surface, x, y, size, color):
    circle(surface, color, (x, y), size, width=0)
    
def draw_iris(surface, x, y, size, color):
    # left iris
    circle(surface, color, (x-size//4, y), size//5, width=0)
    # right iris
    circle(surface, color, (x+size//3, y-size//10), size//5, width=0)

def draw_eye(surface, x, y, size, color):    
    circle(surface, color, (x-size//4, y), size//20, width=0)
    circle(surface, color, (x+size//3, y-size//10), size//20, width=0)
    
def draw_squirrel(surface, x, y, size, color):
    ellipse(surface, color, (x-size//4, y-size//20, size//8, size//10))
    ellipse(surface, color, (x+size//3, y-size//8, size//8, size//10))
    
def draw_body(surface, x, y, size, color):
    x_start = x-size//2**0.5
    y_start = y+size//2**0.5
    polygon(surface, color, [(x_start, y_start), (x_start - 50, y_start + 86), (x_start - 10, y_start + 61), (x_start + 20, y_start + 100), (x_start + 45, y_start + 70), 
            (x_start + 60, y_start + 90), (x_start + 85, y_start + 70), (x_start + 130, y_start + 95), (x+size//2**0.5, y-size//2**0.5), (x_start, y_start) ], width=0)

draw_body(screen, 450, 600, 30, (176, 171, 171))
draw_head(screen,450, 600, 30,(176, 171, 171))
draw_iris(screen, 450, 600, 40, (51, 163, 212))
draw_eye(screen, 450, 600, 40, (0, 0, 0))
draw_squirrel(screen, 450, 600, 40, (255, 255, 255)) 
   
# after that, updating screen
pygame.display.update()

# repeat after changes

# loop, which manages proceeding events 
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
