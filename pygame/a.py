import pygame
import datetime

pygame.init()

#IMAGES
img_icon = pygame.image.load("clocklogo.webp")
img_clock = pygame.image.load("mickey.jpeg")
img_min = pygame.image.load("minutes.png")
img_sec = pygame.image.load("seconds.png")

#DISPLAY
pygame.display.set_icon(img_icon)
pygame.display.set_caption("mickey's clock")
screen = pygame.display.set_mode((1000, 800))

#ARROWS
img_min = pygame.transform.scale(img_min, (50, 600))
img_sec = pygame.transform.scale(img_sec, (50, 650))

clock = pygame.time.Clock()

#LOOP
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    t = datetime.datetime.now()
    mn = t.minute
    sc = t.second
    
    mnang = mn * 6
    scang = sc * 6
    
    screen.blit(img_clock, (-200, -110))
    # screen.blit(mnarr, (474, 130))
    # screen.blit(scarr, (474, 90))
    
    rmn = pygame.transform.rotate(img_min, mnang)
    rsc = pygame.transform.rotate(img_sec, scang)
    
    mnrc = img_min.get_rect(center = (237, 65))
    mnsc = img_sec.get_rect(center = (237, 45))
    
    screen.blit(rmn, (499, 130))
    screen.blit(rsc, (474, 90))
    
    
    
    
    pygame.display.flip()

    clock.tick(60)
    
    
pygame.quit()
    
    
    
    