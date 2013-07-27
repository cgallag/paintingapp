'''
Created on Jul 27, 2013

@author: cagallagher
'''

import pygame, sys, colorsys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()
    
def drawCanvas(windowwidth, windowheight, caption, bgcolor):
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.set_caption(caption)
    pygame.mouse.set_visible(True)

    windowSurface.fill(bgcolor)
    pygame.display.update()
    return windowSurface
    
