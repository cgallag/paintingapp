'''
Created on Jul 26, 2013

@author: cagallagher
'''
import pygame, sys, colorsys, draw_utils
from pygame.locals import *
#from pygame.surfarray import *
from draw_utils import *

def make_cpicker(windowSurface, cptopleftx, cptoplefty, cpwidth, cpheight):
    cpSurface = pygame.surface.Surface((cpwidth, cpheight))
    for i in range(1,10):
        for j in range (1, 10):
            cpSurface.set_at((i,j), (255,0,0))
    windowSurface.blit(cpSurface, (cptopleftx, cptoplefty))
    pygame.display.update()
    return cpSurface

def use_cpicker():
    WINDOWWIDTH = 600
    WINDOWHEIGHT = 600
    cptopleftx, cptoplefty = 500, 50
    cpwidth, cpheight = 300, 50
    windowSurface = drawCanvas(WINDOWWIDTH, WINDOWHEIGHT, 'Painter', (255, 255, 255))
    make_cpicker(windowSurface, cptopleftx, cptoplefty, cpwidth, cpheight)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
            if event.type == MOUSEBUTTONDOWN:
                (xclick, yclick) = pygame.mouse.get_pos()
                if (xclick >= cptopleftx and xclick <= cptopleftx + cpwidth 
                and yclick >= cptoplefty and yclick <= cptoplefty + cpheight):
                    print xclick, yclick, windowSurface.get_at((xclick, yclick))     
                    
if __name__ == "__main__":
    use_cpicker()    


    
