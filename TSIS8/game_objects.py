import pygame
import random
from settings import WIDTH,HEIGHT,SIZE

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background,self).__init__()

        self.image = pygame.image.load('C:\pythonn\TSIS8\Materials\\Background.jpg')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT

    def update(self):
        self.rect.bottom += 5
                                                      #движение фона
        if self.rect.bottom >= self.rect.height :
            self.rect.bottom = HEIGHT

        
            
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('C:\pythonn\TSIS8\Materials\Player.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH/2          
        self.rect.bottom = HEIGHT - 50


    def update(self):
        keys = pygame.key.get_pressed()

        
        if self.rect.left > 0:
              if keys[pygame.K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < WIDTH:        
              if keys[pygame.K_RIGHT]:
                  self.rect.move_ip(10, 0)
        

class Enemy(pygame.sprite.Sprite):
    cooldown = 1000
    current_cooldown = 0

    def __init__(self):
        super(Enemy,self).__init__()

        image_name = 'C:\pythonn\TSIS8\Materials\Enemy.png'
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

        self.rect.midbottom = (random.randint(40,WIDTH-40),0)  #рандомный спавн врагов

    def update(self):
        self.speed = 5
        self.rect.move_ip(0,self.speed)

    @staticmethod
    def process(clock,enemies):
        if Enemy.current_cooldown <= 0:
            enemies.add(Enemy())
            Enemy.current_cooldown = Enemy.cooldown
        else:
            Enemy.current_cooldown -= clock.get_time()

        for e in list(enemies):
            if e.rect.right < 0 or e.rect.left > WIDTH or e.rect.top > HEIGHT:
               enemies.remove(e)

class Fuel(pygame.sprite.Sprite):
    cooldown = 2000
    current_cooldown = 0
    speed = 5

    def __init__(self):
        super(Fuel,self).__init__()

        self.image = pygame.image.load('C:\pythonn\TSIS8\Materials\\fuel.PNG')
        self.image = pygame.transform.scale(self.image,(50,50))

        
        
        self.rect = self.image.get_rect()

        self.rect.midbottom = (random.randint(50,WIDTH-60),0)

    def update(self):
        self.rect.move_ip(0,self.speed)

    @staticmethod
    def process(clock,fuels):
        if Fuel.current_cooldown <= 0:
            fuels.add(Fuel())
            Fuel.current_cooldown = Fuel.cooldown
        else:
            Fuel.current_cooldown -= clock.get_time()

        for e in list(fuels):
            if e.rect.right < 0 or e.rect.left > WIDTH or e.rect.top > HEIGHT:
               fuels.remove(e)