import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.flip()

    pygame.draw.rect(win, (0,0,255), pygame.Rect(30, 30, 60, 60),5)




