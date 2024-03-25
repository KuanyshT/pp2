import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

img_bg = pygame.image.load("mickey.jpeg")
img_lg = pygame.image.load("clocklogo.webp")

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_icon(img_lg)
pygame.display.set_caption("Mickey clock")

img_min = pygame.image.load("minutes.png").convert_alpha()
img_sec = pygame.image.load("seconds.png").convert_alpha()

img_min = pygame.transform.scale(img_min, (50, 550))
img_sec = pygame.transform.scale(img_sec, (50, 600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(img_bg, (-200, -100))
    
    t = datetime.datetime.now()
    mnang = -t.minute * 6  # Minute hand angle calculation
    scang = -t.second * 6  # Second hand angle calculation
    
    mnarr = pygame.transform.rotate(img_min, mnang)
    scarr = pygame.transform.rotate(img_sec, scang)
    
    screen.blit(mnarr, (474, 150))
    screen.blit(scarr, (474, 120))
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
