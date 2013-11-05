'''
Created on Jul 24, 2013

@author: cagallagher
'''

import pygame, sys, colorsys, draw_utils
from pygame.locals import *
from draw_utils import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def drawaaline(windowSurface, linecolor, (x1, y1), (x2, y2), thickness):
    pygame.draw.aaline(windowSurface, linecolor, (x1, y1), (x2, y2), thickness)
    pygame.display.update()
        
def drawrainbowline():
    # Set up pygame, the window, and the mouse cursor
    windowSurface = drawCanvas(WINDOWWIDTH, WINDOWHEIGHT, 'Painter', WHITE)
    
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
                    drawaaline(windowSurface, getrgb(hue), (xclick, yclick), (xclick, yclick), linethickness)
                    hue += 0.01
                    mousedrawing = True
                     
                if event.type == MOUSEMOTION:
                    if mousedrawing:
                        (xcurr,ycurr) = pygame.mouse.get_pos()
                        drawaaline(windowSurface, getrgb(hue), (xprev,yprev), (xcurr, ycurr), linethickness)
                        hue += 0.01
                        xprev = xcurr
                        yprev = ycurr
                        
                if event.type == MOUSEBUTTONUP:
                    if mousedrawing:
                        (xfinal, yfinal) = pygame.mouse.get_pos()
                        drawaaline(windowSurface, getrgb(hue), (xprev, yprev), (xfinal, yfinal), linethickness)
                        hue += 0.01
                        mousedrawing = False
                
                if event.type == KEYDOWN:                        
                    if event.key == ord('c'):
                        windowSurface.fill(WHITE)
                        pygame.display.update()
            
if __name__ == "__main__":
    drawrainbowline()               

