import pygame
from pygame import *
from Config import *

from Interval import *
from Colors import *
from Eye import *
from Anim import *

pygame.init()
clock = pygame.time.Clock()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

eye_right = None


def make_blink():
    global eye_right
    if not eye_right is None:
        eye_right._anim.set_current_animation_sequence(1, 5)
        eye_right._status = eye_status.blink
        eye_right._anim.get_current_animation().play()
        print("blinking")

def main():
    global eye_right
    r = pygame.Rect(0, 0, 30, 1)
    r.center = (WIDTH/2, HEIGHT/2)
    eye_right = Eye(r, 2.5, AQUA, True, padding=[20, 0, 0, 0])

    # Animation 1
    an = Anim(eye_right, 0, 2, eye_status.setOpen)
    an.scaleY(28, 4)
    eye_right._anim.add_animation_sequence(an)

    # Animation 2
    an = Anim(eye_right, 0, 0, eye_status.blink)
    an.scaleY(2, 4)
    eye_right._anim.add_animation_sequence(an)

    # Animation 3
    an = Anim(eye_right, 0, 0, eye_status.blink)
    an.scaleY(28, 4)
    eye_right._anim.add_animation_sequence(an)

    # Animation 4
    an = Anim(eye_right, 0, 0, eye_status.blink)
    an.scaleY(2, 4)
    eye_right._anim.add_animation_sequence(an)

    # Animation 5
    an = Anim(eye_right, 0, 0, eye_status.blink)
    an.scaleY(28, 4)
    eye_right._anim.add_animation_sequence(an)

    # Animation 6
    an = Anim(eye_right, 0, 0, eye_status.stayOpen)
    an.stay()
    eye_right._anim.add_animation_sequence(an)

    interval = Interval(5, make_blink, args=[])
    interval.start()

    eye_right._anim.set_current_animation_by_name(eye_status.setOpen)
    #eye_right._anim.get_current_animation().play()

    fps = ""
    #canvas = luma.core.render.canvas(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                interval.stop()
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
