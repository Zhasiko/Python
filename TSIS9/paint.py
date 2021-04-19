import pygame
import sys
import os

SIZE = (WIDTH, HEIGHT) = (620,480)
WHITE = (255,255,255)
BLACK = (0, 0, 0) # 1
RED = (255,0,0) #2
ORANGE = (255, 165, 0) #3
YELLOW = (255,239,0) #4
GREEN = (0,255,0) #5
BLUE = (0,0,255) #6
PURPLE = (255,0,196) #7

pygame.init()

screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
pygame.display.set_caption("PAINT")

isPressed = False
prevPos = (pygame.mouse.get_pos())
curPos = (pygame.mouse.get_pos())

# 0 - 
curTool = 0
toolCount = 5
color = WHITE

while 1:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                curTool = (curTool + 1) % toolCount

            if event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = ORANGE
            elif event.key == pygame.K_4:
                color = YELLOW
            elif event.key == pygame.K_5:
                color = GREEN
            elif event.key == pygame.K_6:
                color = BLUE
            elif event.key == pygame.K_7:
                color = PURPLE
            if event.key == pygame.K_s:
                pygame.image.save(screen, 'C:\pythonn\TSIS9\images\image.png')
            

        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            x,y = pygame.mouse.get_pos()
            prevPos = curPos
            curPos = pygame.mouse.get_pos()
    
    def DrawCircle(screen,x,y):
        pygame.draw.circle(screen,color,(x,y),10)

    def Drawcircle(screen,x,y):
        pygame.draw.circle(screen,color,(x,y),40,2)

    def DrawLine(screen,prevPos,curPos):
        pygame.draw.line(screen,color,prevPos,curPos,2)

    def DrawRectangle(screen, x,y, w, h):
        pygame.draw.rect(screen, color, [x, y, w, h],5)

    def Eraser(screen,prevPos,curPos):
        pygame.draw.line(screen,WHITE,prevPos,curPos,30)
    
         

    if curTool == 0:
        DrawLine(screen,prevPos,curPos)
    elif curTool == 1:
        DrawCircle(screen,x,y)
    elif curTool == 2:
        DrawRectangle(screen, curPos[0],curPos[1],100,100)
    elif curTool == 3:
        Drawcircle(screen,x,y)
    elif curTool == 4:
        Eraser(screen,prevPos,curPos)


    pygame.display.update()

