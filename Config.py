import pygame
from pygame import *
import os
os.putenv('SDL_FBDEV', '/dev/fb1')
#os.putenv('FBDEV', '/dev/fb1')

WIDTH = 160
HEIGHT = 128

#DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
#DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT))