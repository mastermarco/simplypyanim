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
    r = pygame.Rect(0, 0, 30, 1)
    r.center = (WIDTH/2, HEIGHT/2)
    eye_right = Eye(r, 2.5, AQUA, True, screen, padding=[30, 0, 0, 0])
    eye_right.set_up_sequence([0, 1, 2, 3, 4, 10, 12, 14])

    r = pygame.Rect(0, 0, 30, 1)
    r.center = (WIDTH / 2, HEIGHT / 2)
    eye_left = Eye(r, 2.5, AQUA, False, screen, padding=[-20, 0, 0, 0])
    eye_left.set_up_sequence([0, 1, 2, 3, 4, 11, 13, 15])

    r = pygame.Rect(0, 0, 30, 1)
    r.center = (WIDTH / 2, HEIGHT / 2)
    central = Eye(r, 2.5, AQUA, True, screen, visible=False)
    central.set_up_sequence([8, 9])

    eye_right.play_sequence()
    eye_right.set_up_blinking()

    eye_left.play_sequence()
    eye_left.set_up_blinking()

    fps = ""
    #canvas = luma.core.render.canvas(screen)

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

        if eye_left._visible:
            eye_left.draw()

        if central._visible:
            central.draw()

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
