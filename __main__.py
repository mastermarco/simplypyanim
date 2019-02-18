import pygame
from pygame import *
from Config import *

from Colors import *
from Eye import *
from Anim import *

pygame.init()
clock = pygame.time.Clock()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


def main():
    r = pygame.Rect(10, 0, 30, 1)
    r.center = (WIDTH/2, HEIGHT/2)
    eye_right = Eye(r, 2.5, AQUA, True)

    # Animation 1
    an = Anim(eye_right, 2, 0, eye_status.setOpen)
    #an.moveX(30, 1)
    #an.moveY(40, 1)
    #an.translate(100, 20, 1)
    #an.scaleX(2, 1)
    an.scaleY(28, 1)
    #an.scale(50, 28, 1)
    eye_right._anim.add_animation_sequence(an)

    # Animation 2
    an2 = Anim(eye_right, 0, 3, eye_status.blink)
    an2.moveX(WIDTH/2+30, 1)
    eye_right._anim.add_animation_sequence(an2)

    # Animation 3
    an3 = Anim(eye_right, 0, 0, eye_status.stayOpen)
    print(WIDTH/2 + 30)
    print(WIDTH/2 - 40)
    an3.moveX(WIDTH/2, 1)
    eye_right._anim.add_animation_sequence(an3)


    eye_right._anim.set_current_animation_by_name(eye_status.setOpen)
    eye_right._anim.get_current_animation().play()

    fps = ""
    #canvas = luma.core.render.canvas(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
