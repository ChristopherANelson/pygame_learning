"""
Pygame base template for opening a window
"""

import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BROWN=(250,100,100)

def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x,400+y,30,45])
    pygame.draw.polygon(screen, GREEN, [[150+x,400+y],[75+x,250+y],[x,400+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,350+y],[75+x,230+y],[10+x,350+y]])

def print_instructions():
    print()

# Font (Font name, size, bold, italics)
font = pygame.font.SysFont('Calibri',35,True,False)

# Screen width and height
size = (700,500)
screen = pygame.display.set_mode(size)

# TITLE
pygame.display.set_caption("My game")

# Loop until close button is pressed
done = False

# Manage how fast the screen updates
clock = pygame.time.Clock()


# ------ MAIN PROGRAM LOOP ------ #
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    # <- Game Logic here ->

    # <- Screen-clearing code here ->
    screen.fill(WHITE)

    # <- Drawing code here ->
    draw_tree(screen, 0,30)
    draw_tree(screen, 200,30)
    draw_tree(screen, 400,30)
    draw_tree(screen, 600,30)


    pygame.display.flip()
    # <- Limit to 60 frames ->
    clock.tick(60)

pygame.quit
