from Interval import *
from Config import *
from Colors import *
from AnimationSequence import AnimationSequence
from Anim import *


def enum(**enums):
    return type('Enum', (), enums)


eye_status = enum(setOpen=1, stayOpen=2, waiting=3, setClose=4, stayClose=5)


class Eye:
    def __init__(self, rect, radius, color, isright, screen, padding=[], status=""):
        self._screen = screen
        self._padding = list(padding)
        # Object Rect
        self._rect = rect
        # Array
        self._rect.left = rect[0] + self._padding[0]
        self._rect.top = rect[1]
        self._rect.width = rect[2]
        self._rect.height = rect[3]
        self._radius = radius
        self._color = color
        self._frame = 0
        self._is_right = isright
        self._anim = AnimationSequence()
        self._status = status
        self._interval = None
        self.set_up_animations()
        self._visible = True

    def start_new_animation(self):
        self.frame = 0

    def set_rect(self, r):
        self._rect.left = r[0]
        self._rect.top = r[1]
        self._rect.width = r[2]
        self._rect.height = r[3]

    def set_up_animations(self):
        # Animation 0
        r_def = pygame.Rect(self._rect.left, self._rect.top, 30, 2)
        an = Anim(self, 0, 2, "set open", r_def)  # eye_status.setOpen
        an.scaleY(28, 4)
        self._anim.add_animation_sequence(an)

        # Animation 1
        an = Anim(self, 0, 0, "scale Y down 1", r_def)  # Openeye_status.blink
        an.scaleY(2, 4)
        self._anim.add_animation_sequence(an)

        # Animation 2
        an = Anim(self, 0, 0, "scale Y up 2", r_def)
        an.scaleY(28, 4)
        self._anim.add_animation_sequence(an)

        # Animation 3
        an = Anim(self, 0, 0, "scale Y down 3", r_def)
        an.scaleY(2, 4)
        self._anim.add_animation_sequence(an)

        # Animation 4
        an = Anim(self, 0, 0, "scale Y up 4", r_def)
        an.scaleY(28, 4)
        self._anim.add_animation_sequence(an)

        # Animation 5
        an = Anim(self, 0, 0, "stay open", r_def)  # eye_status.stayOpen
        an.stay()
        self._anim.add_animation_sequence(an)

        # Animation 6
        an = Anim(self, 0, 0, "scale Y down 5", r_def, on_end={"_visible": False})
        an.scaleX(1, 4)
        an.scaleY(1, 4)
        self._anim.add_animation_sequence(an)

        # Animation 7
        an = Anim(self, 0, 4, "waiting", r_def)
        an.scaleX(5, 4)
        an.scaleY(4, 4)
        self._anim.add_animation_sequence(an)

        # Animation 8
        r_def = pygame.Rect(0, 0, 5, 4)
        r_def.center = (WIDTH / 2, HEIGHT / 2)
        an = Anim(self, 0, 0, "scale Y up 4", r_def, on_start={"_visible": True}, shape="3")
        an.scaleX(30, 4)
        an.scaleY(28, 4)
        self._anim.add_animation_sequence(an)

        self._interval = Interval(5, self.make_blink, args=[])
        self._interval.start()

        self._anim.set_current_animation_sequence([0, 1, 2, 3, 4, 6, 7, 8])
        self._anim.get_current_animation().play()


    def make_blink(self):
        if self._status == eye_status.waiting:
            self._anim.set_current_animation_sequence([1, 2, 3, 4, 5])
            self._status = eye_status.setOpen
            self._anim.get_current_animation().play()

    def draw(self):
        if self._anim.is_play():
            if self._anim.get_current_animation()._is_ended:
                self._anim.handle_next_animation()
            else:
                self._anim.get_current_animation().play()
        else:
            self._anim.handle_next_animation()

        if self._visible:
            if self._anim.get_current_animation()._shape == "rect":
                pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)
            elif self._anim.get_current_animation()._shape == "3":
                myfont = pygame.font.SysFont('Comic Sans MS', 20)
                textsurface = myfont.render('3', False, AQUA)
                print(self._rect)
                self._screen.blit(textsurface, (self._rect.left, self._rect.height))

