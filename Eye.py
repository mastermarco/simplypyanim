from Config import *
from AnimationSequence import AnimationSequence


def enum(**enums):
    return type('Enum', (), enums)


eye_status = enum(setOpen=1, stayOpen=2, blink=3, setClose=4, stayClose=5)


class Eye:
    def __init__(self, rect, radius, color, isright, padding=[]):
        self._padding = list(padding)
        # Object Rect
        self._rect = rect
        # Array
        self._rect.left = rect[0] + self._padding[0]
        self._rect.top = rect[1]
        self._rect.width = rect[2]
        self._rect.height = rect[3]
        #self.set_rect(self._rect)
        self._radius = radius
        self._color = color
        self._frame = 0
        self._is_right = isright
        self._anim = AnimationSequence()
        self._status = eye_status.setOpen

    def start_new_animation(self):
        self.frame = 0

    def set_rect(self, r):
        self._rect.left = r[0]
        self._rect.top = r[1]
        self._rect.width = r[2]
        self._rect.height = r[3]

    def draw(self):
        if self._anim.is_play():
            if self._anim.get_current_animation()._is_ended:
                self._anim.get_current_animation()._is_play = False
                #if self._anim.go_next_animation():
                    #self._anim.get_current_animation().play()
            else:
                self._anim.get_current_animation().play()

        if self._anim.get_current_animation()._is_play:
            print(self._status)
            pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)

