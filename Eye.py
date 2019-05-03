from Interval import *
from Config import *
from Colors import *
from Animations import Animations
#from Anim import *


def enum(**enums):
    return type('Enum', (), enums)


eye_status = enum(setOpen=1, stayOpen=2, waiting=3, setClose=4, stayClose=5)


class Eye:
    def __init__(self, rect, color, center=(0, 0), x=0, y=0):
        self._rect = pygame.Rect(rect)
        self._default_rect = pygame.Rect(rect)
        self._rect.center = center
        self._color = color
        self._visible = False
        self.set_position(x, y)
        self._animations = Animations(self)

    def draw(self):
        if self._animations._is_play:
            self._animations.draw_frames()
            if self._visible:
                pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)
        else:
            if self._visible:
                pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)
            self._animations.play()

    def set_position(self, x, y):
        #self._rect.move_ip(x, y)
        self._rect.left = x
        self._rect.top = y

    def set_position_x(self, x):
        self._rect.left = x

    def set_position_y(self, y):
        self._rect.top = y

    def set_scale(self, w, h):
        #self._rect.move_ip(x, y)
        self._rect.width = w
        self._rect.height = h

    def set_scale_x(self, w):
        self._rect.width = w

    def set_scale_y(self, h):
        self._rect.height = h


