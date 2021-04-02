import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.flip()

    pygame.draw.circle (win, (0,0,255), (100, 100), 50)
