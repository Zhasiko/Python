import pygame
import sys
import time
from settings import SIZE,WHITE,BLACK,WIDTH,HEIGHT
from game_objects import Player,Background,Enemy,Fuel

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("NFS")
SCORE = 0
 


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)       #Шрифты для записи
game_over = font.render("Game Over", True, WHITE)


music = pygame.mixer.Sound("C:\pythonn\TSIS8\Materials\\lamb.mp3")    #фоновая музыка
music.play(-1)

#GAME OBJECTS
player = Player()
background = Background()

#GROUPS
all_objects = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fuels = pygame.sprite.Group()

all_objects.add(background)
all_objects.add(player)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(WHITE)
    Enemy.process(clock,enemies)
    Fuel.process(clock,fuels)

    all_objects.update()
    enemies.update()
    fuels.update()



    player_and_enemies_collided = pygame.sprite.spritecollide(player,enemies,True)
    player_and_fuels_collided = pygame.sprite.spritecollide(player,fuels,True)


    if player_and_enemies_collided:
          pygame.mixer.Sound('C:\pythonn\TSIS8\Materials\crash.wav').play()
          pygame.mixer.Sound('C:\pythonn\TSIS8\Materials\\fail.wav').play()
          time.sleep(0.5)

          music.stop()         
          screen.fill(BLACK)
          screen.blit(game_over, (WIDTH/4-30,HEIGHT/4))
          screen.blit(scores, (250,200))
           
          pygame.display.update()
          for entity in all_objects:
                entity.kill() 
          time.sleep(5)
          pygame.quit()
          sys.exit() 

    if player_and_fuels_collided:
        pygame.mixer.Sound("C:\pythonn\TSIS8\Materials\coin.wav").play()
        SCORE += 1
    

    all_objects.draw(screen)
    enemies.draw(screen)
    fuels.draw(screen)
    scores = font_small.render('Score:' + str(SCORE), True, WHITE)
    screen.blit(scores, (20,10))

    pygame.display.flip()
    clock.tick(30)