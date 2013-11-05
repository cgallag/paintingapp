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
    
def getrgb(hue):
    (r,g,b) = colorsys.hls_to_rgb(hue, 0.5, 0.5)
    return (round(r*255), round(g*255), round(b*255))