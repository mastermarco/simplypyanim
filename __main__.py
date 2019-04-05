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


def main():
    eye_right = Eye([0, 0, 30, 30], AQUA, (0, 0), WIDTH/2+25, HEIGHT/2)
    eye_right._visible = True

    '''eye_left = Eye([0, 0, 30, 30], AQUA, (0, 0), WIDTH/2 - 20, HEIGHT/2)
    eye_left._visible = True'''

    fps = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not eye_right._interval is None:
                    eye_right._interval.stop()
                if not eye_left._interval is None:
                    eye_left._interval.stop()
                return True

        screen.fill(BLACK)

        if eye_right._visible:
            eye_right.draw()
        '''if eye_left._visible:
            eye_left.draw()'''

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
