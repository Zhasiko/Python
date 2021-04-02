import pygame
import math
from settings import SIZE,WHITE,RED,BLUE,BLACK,GREEN
pygame.init()
screen = pygame.display.set_mode(SIZE)

play = True
PI = math.pi
cnt = 0

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)  # Borders
    
    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3)  # X-Axis
    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3)  # Y-Axis

    pygame.draw.line(screen, BLACK, (70, 40), (730, 40))  # H_line 1

    pygame.draw.line(screen, BLACK, (70, 520), (730, 520))  # H_line 2
    pygame.draw.line(screen, BLACK, (100, 10), (100, 550))  # V_line 1
    pygame.draw.line(screen, BLACK, (700, 10), (700, 550))  # V_line 2
    

    for x in range(100, 701, 100):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 550))
        
    for x in range(100, 701, 50):

        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))
        
        pygame.draw.line(screen, BLACK, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 540))
        

    for y in range(40, 521, 60):
        pygame.draw.line(screen, BLACK, (70, y), (730, y))
        
    for y in range(40, 521, 30):
        pygame.draw.line(screen, BLACK, (70, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (730, y))
        
    for y in range(40, 521, 15):
        pygame.draw.line(screen, BLACK, (70, y), (80, y))
        pygame.draw.line(screen, BLACK, (720, y), (730, y))
        

    for x in range(100, 700):

        cos_y1 = 240 * math.cos((x - 100) / 100 * PI)
        cos_y2 = 240 * math.cos((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, BLUE, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])


        sin_y1 = 240 * math.sin((x - 100) / 100 * PI)
        sin_y2 = 240 * math.sin((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, RED, False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])


    pygame.display.flip()
pygame.quit()
