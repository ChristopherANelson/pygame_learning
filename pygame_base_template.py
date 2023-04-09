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
    screen.fill(BLUE)

    # <- Drawing code here ->
    pygame.draw.rect(screen, WHITE, [100,150,500,150])

    # --- Diplay text --- #

    text = font.render("Hello World!", True,BLACK)
    screen.blit(text, [250,200])

    # --- Diplay text --- #



    pygame.display.flip()
    # <- Limit to 60 frames ->
    clock.tick(60)

pygame.quit
