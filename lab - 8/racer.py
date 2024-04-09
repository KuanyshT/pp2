import pygame
import random

pygame.init()
clock = pygame.time.Clock()

#VARIABLES-------------------------------
hard = 200
coincollision = False
gameover = False
level = 1
twcoin = 20
font = pygame.font.Font('freesansbold.ttf', 16)

#COINS----------------------------------
coin_list = []
coin_x = 0
coin_y = 0 
coins_counter = 0

#SOUNDS----------------------------------
bgmusic = pygame.mixer.music.load("")

#IMAGES----------------------------------
player_img = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/Player.png")
enemy_img = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/Enemy.png")
background_img = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/AnimatedStreet.png")
icon_img = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/racericon.png")
coin_img = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/tenge.png")
pygame.transform.scale(coin_img, (20, 20))

#PLAYER-----------------------------------
player_x = 150
player_y = 500
player_speed = 7

#ENEMY------------------------------------
enemy_x = 0
enemy_y = 0
enemy_speed = 5
enemy_list = []

#RESTART-----------------------------------
def restart():
    global enemy_list, coin_list, hard, level, twcoin, gameover, coins_counter, enemy_speed
    enemy_list = []
    coin_list = []
    hard = 200
    level = 1
    gameover = False
    coins_counter = 0
    enemy_speed = 5



#DISPLAY---------------------------------
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
pygame.display.set_icon(icon_img)

#LOOP--------------------------------------
done = False
while not done:
    pygame.transform.scale(coin_img, (20, 20))
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if not gameover:
        #MOVING--------------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        
        #BLIT BACKGROUND-----------------------
        screen.blit(background_img, (0, 0))
        
        #BLIT PLAYER----------------------------
        screen.blit(player_img, (player_x, player_y))
        
        #BLIT ENEMY----------------------------
        if random.randint(0, hard) < 2:
            enemy_x = random.randint(50, 350)
            enemy_list.append([enemy_x, enemy_y])
            
        for coord in enemy_list:
            screen.blit(enemy_img, (coord[0], coord[1]))
            if coord[1] > 600:
                del enemy_list[0]
            coord[1] += enemy_speed
    
            # COLLISION WITH ENEMY DETECTING--------------------------------
            if coord[0] + 40 >= player_x and coord[0] - 40 <= player_x and coord[1] + 83 >= player_y and coord[1] - 83 <=player_y:
                gameover = True  
                
        #BLIT COINS-------------------------------
        if random.randint(0, 250) < 2:
            coin_x = random.randint(50,350)
            coin_list.append([coin_x, coin_y])
            
        for coord in coin_list:
            screen.blit(pygame.transform.scale(coin_img, (80, 40)), (coord[0], coord[1]))
            coord[1] += 5
            
            # COLLISION WITH COIN DETECTING--------------------------------
            if coord[0] + 40 >= player_x and coord[0] - 40 <= player_x and coord[1] + 40 >= player_y and coord[1] - 40 <=player_y:
                coin_list.remove(coord)
                coincollision = True
        
        #COINS COUNTER---------------------------------
        if coincollision == True:
            coins_counter += 1
            coincollision = False
        #MAKE HARDER---------------------------------
        if coins_counter >= twcoin:
            enemy_speed += 1
            level += 1
            hard -= 5
            twcoin += 20
            
        #BLIT COINS COUNTER and LEVEL---------------------------------
        coin_text = font.render(f"Coins: {coins_counter} Level: {level}", True, (0, 0, 0))
        screen.blit(coin_text, (200, 0))
        

    else:
        screen.fill((0, 0, 0))
        text = font.render('Game over, press space to restart', True, (0, 255, 0))
        screen.blit(text, (65, 300))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart()
            
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
        
        
    
        
        