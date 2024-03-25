import pygame 
pygame.init()
import datetime

screen = pygame.display.set_mode((1000, 800))

done = False

chasi = pygame.image.load("mickey.jpeg")
minuta = pygame.image.load("minutes.png")
secunda = pygame.image.load("seconds.png")
black = (0, 0, 0)


minuta = pygame.transform.scale(minuta, (45, 550))
secunda = pygame.transform.scale(secunda, (50, 500))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    vremya = datetime.datetime.now()    
    minYgl = vremya.minute / 60 * 360
    secYgl = vremya.second / 60 * 360
    
    screen.blit(pygame.transform.scale(chasi, (1000, 800)), (0, 0))
  
    minuta1 = pygame.transform.rotate(minuta, -minYgl)
    secunda1 = pygame.transform.rotate(secunda, -secYgl)
   
    minutaRect = minuta1.get_rect(center=(500, 390))
    secundaRect = secunda1.get_rect(center=(500, 400))

    
    screen.blit(minuta1, minutaRect)
    screen.blit(secunda1, secundaRect)
    pygame.draw.circle(screen, black, (500, 400), 20)
    pygame.display.flip()
pygame.quit()