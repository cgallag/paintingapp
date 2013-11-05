import pygame, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()
    
def waitForPlayerClick():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return
            

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
    
# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('KenPaints')
pygame.mouse.set_visible(True)

colorCircle = pygame.Rect(50, 50, 480, 480)
colorwheelImg = pygame.image.load('Color_circle_(hue-sat).png').convert()
windowSurface.blit(colorwheelImg, colorCircle)

pygame.display.update()

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            
            if event.type == MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                print x-50, y-50
