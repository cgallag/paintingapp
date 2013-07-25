'''
Created on Jul 24, 2013

@author: cagallagher
'''

import pygame, sys, colorsys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()
    
def drawaaline(linecolor, (x1, y1), (x2, y2), thickness):
    pygame.draw.aaline(windowSurface, linecolor, (x1, y1), (x2, y2), thickness)
    pygame.display.update()
    
def getrgb(hue):
    (r,g,b) = colorsys.hls_to_rgb(hue, 0.5, 0.5)
    # print round(r*255), round(g*255), round(b*255)
    return (round(r*255), round(g*255), round(b*255))
    
WINDOWWIDTH = 600
WINDOWHEIGHT = 600

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
    
# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('KenPaints')
pygame.mouse.set_visible(True)

windowSurface.fill(WHITE)
pygame.display.update()

hue = 0.0
mousedrawing = False
linethickness = 30

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            
            if event.type == MOUSEBUTTONDOWN:
                (xclick,yclick) = pygame.mouse.get_pos()
                xprev = xclick
                yprev = yclick 
                drawaaline(getrgb(hue), (xclick, yclick), (xclick, yclick), linethickness)
                hue += 0.01
                mousedrawing = True
                 
            if event.type == MOUSEMOTION:
                if mousedrawing:
                    (xcurr,ycurr) = pygame.mouse.get_pos()
                    drawaaline(getrgb(hue), (xprev,yprev), (xcurr, ycurr), linethickness)
                    hue += 0.01
                    xprev = xcurr
                    yprev = ycurr
                    
            if event.type == MOUSEBUTTONUP:
                if mousedrawing:
                    (xfinal, yfinal) = pygame.mouse.get_pos()
                    drawaaline(getrgb(hue), (xprev, yprev), (xfinal, yfinal), linethickness)
                    hue += 0.01
                    mousedrawing = False
            
            if event.type == KEYDOWN:                        
                if event.key == ord('c'):
                    windowSurface.fill(WHITE)
                    pygame.display.update()
            
               

