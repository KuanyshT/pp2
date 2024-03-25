import pygame
import random

pygame.init()

#SCREEN-------------------------------------
pygame.display.set_mode((800,600))
pygame.display.set_caption("Racer")

#LOOP---------------------------------------
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True
    
    