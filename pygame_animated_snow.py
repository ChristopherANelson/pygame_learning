"""
Pygame base template for opening a window
"""

import pygame
pygame.init()
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
    
snow_list = []
for i in range(50):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    snow_list.append([x,y])

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
    screen.fill(BLACK)

    # <- Drawing code here ->
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i],2)
        snow_list[i][1] +=1 # Move snow down

    # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 500:
            y = random.randrange(-50,-10)
            snow_list[i][1]=y
            x = random.randrange(0,700)
            snow_list[i][0]=x

    pygame.display.flip()
    # <- Limit to 60 frames ->
    clock.tick(60)

pygame.quit
