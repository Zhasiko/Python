import pygame
from pygame.locals import *

screenWidth = 600
screenHeight = 600

pygame.init()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Diamond")

clock = pygame.time.Clock()
MAXFPS = 30

# define the diamond points as described above
diamondWidth = 80
diamondHeight = 100

pos1 = (screenWidth/2, screenHeight/2 - diamondHeight/2)
pos2 = (pos1[0] - diamondWidth/2, pos1[1] + diamondHeight/2)
pos3 = (pos1[0], pos1[1]+diamondHeight)
pos4 = (pos2[0]+diamondWidth, pos2[1])

# points for the first diamond
points = [pos1, pos2, pos3, pos4]

# points for the second diamond, which are exactly like the first except their
# Y value is incremented over the original points so it does not appear over
# it, but rather to it left
secondPoints = [(p[0]+diamondWidth+10, p[1]) for p in points]

stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == QUIT:
            stop = True

    window.fill((255, 255, 255))

    # DRAWING THE DIAMOND:
    # Here is where we connect all the points in the [points] array, and
    # draw them as a shape with a certain color (used cian because it's
    # a diamond-dy color lol)

    # Draw filled diamond
    pygame.draw.polygon(window, (0, 255, 255), points, 0)

    # Draw empty diamond with lines of thickness 4
    pygame.draw.polygon(window, (0, 255, 255), secondPoints , 4)

    pygame.display.flip()
    clock.tick(MAXFPS)

pygame.quit()