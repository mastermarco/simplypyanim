from Config import *
from AnimationSequence import AnimationSequence


def enum(**enums):
    return type('Enum', (), enums)


eye_status = enum(setOpen=1, stayOpen=2, blink=3, setClose=4, stayClose=5)


class Eye:
    def __init__(self, rect, radius, color, isright, padding):
        self._rect = rect
        self._padding = padding
        self.set_rect(self._rect)
        self._radius = radius
        self._color = color
        self._frame = 0
        self._is_right = isright
        self._anim = AnimationSequence()
        self._status = eye_status.setOpen

    def start_new_animation(self):
        self.frame = 0

    def set_rect(self, r):
        self._rect.left = r[0] + self._padding
        self._rect.top = r[1]
        self._rect.width = r[2]
        self._rect.height = r[3]

    def draw(self):
        if self._status == eye_status.setOpen:
            if not self._anim.is_play():
                self._anim.set_current_animation_by_name(eye_status.setOpen)
                self._anim.get_current_animation().play()
            if self._anim.is_play():
                self._anim.get_current_animation().play()
            if self._anim.get_current_animation()._is_play:
                pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)

