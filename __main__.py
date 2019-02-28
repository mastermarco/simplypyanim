import pygame
import os
from pygame import *
from Config import *


from Colors import *
from Eye import *

from pprint import pprint


os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.mouse.set_visible(False)
pygame.init()
pygame.display.update()

pygame.font.init()
clock = pygame.time.Clock()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

#pygame.display.set_caption("My Game")

eye_right = None


def main():
    global eye_right
    r = pygame.Rect(0, 0, 30, 1)
    r.center = (WIDTH/2, HEIGHT/2)
    print(WIDTH/2, HEIGHT/2)
    eye_right = Eye(r, 2.5, AQUA, True, screen, padding=[20, 0, 0, 0])

    fps = ""
    #canvas = luma.core.render.canvas(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                eye_right._interval.stop()
                return True

        screen.fill(BLACK)
        eye_right.draw()
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
    return False


if __name__ == '__main__':
    try:
        #device = get_device()
        main()
    except KeyboardInterrupt:
        pass
