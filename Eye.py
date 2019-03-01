from Interval import *
from Config import *
from Colors import *
from AnimationSequence import AnimationSequence
from Anim import *


def enum(**enums):
    return type('Enum', (), enums)


eye_status = enum(setOpen=1, stayOpen=2, waiting=3, setClose=4, stayClose=5)


class Eye:
    def __init__(self, rect, radius, color, isright, screen, visible=False, padding=[0,0,0,0], status=""):
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
        self._anim = AnimationSequence(self)
        self._status = status
        self._interval = None
        self._visible = visible
        self._font = self.set_font_size(1)

        self.set_up_animations()

    def start_new_animation(self):
        self.frame = 0

    def set_font_size(self, fntsize):
        return pygame.font.SysFont('Comic Sans MS', fntsize)

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
        an = Anim(self, 0, 1, "waiting", r_def)
        an.scaleX(5, 4)
        an.scaleY(4, 4)
        self._anim.add_animation_sequence(an)

        # Animation 8
        r_def = None
        r_def = pygame.Rect(0, 0, 1, 1)
        #r_def.center = (WIDTH / 2, HEIGHT / 2)
        an = Anim(self, 0, 3, "scale XY up for text", r_def, on_start={"_visible": True}, shape="text", text="3", text_color=AQUA, scale_text_end=55)
        an.scaleX(30, 4)
        an.scaleY(28, 4)
        self._anim.add_animation_sequence(an)

        # Animation 9
        r_def = None
        r_def = pygame.Rect(self._rect.left, self._rect.top, 1, 1)
        an = Anim(self, 0, 1, "forbice", r_def, shape="image", image_file_name="forbice.png")
        an.scaleX(84, 4)
        an.scaleY(84, 4)
        self._anim.add_animation_sequence(an)


    def set_up_blinking(self):
        self._interval = Interval(5, self.make_blink, args=[])
        self._interval.start()

    def set_up_sequence(self, sequence):
        # self._anim.set_current_animation_sequence([8])
        self._anim.set_current_animation_sequence(sequence)

    def play_sequence(self):
        self._visible = True
        self._anim.get_current_animation().play()

    def load_image(self, image_path):
        return pygame.image.load(image_path).convert_alpha()

    def set_image_size(self, image_surface, size):
        return pygame.transform.scale(image_surface, size)

    def make_blink(self):
        if self._status == eye_status.waiting:
            self._anim.set_current_animation_sequence([1, 2, 3, 4])
            self._status = eye_status.setOpen
            self._anim.get_current_animation().play()

    def draw(self):
        if self._anim.is_play():
            if self._anim.get_current_animation()._is_ended:
                # ended
                self._anim.handle_next_animation()
            else:
                # continue to play the current animation because is no eneded
                self._anim.get_current_animation().play()
        else:
            self._anim.handle_next_animation()

        if self._visible:
            if self._anim.get_current_animation()._shape == "rect":
                pygame.draw.rect(DISPLAYSURFACE, self._color, self._rect, 0)
            elif self._anim.get_current_animation()._shape == "text":
                self._screen.blit(self._anim.get_current_animation()._textsurface, (self._rect.left, self._rect.top))
            elif self._anim.get_current_animation()._shape == "image":
                tmp = self.set_image_size(self._anim.get_current_animation()._image_surface, (self._rect.width, self._rect.height))
                self._screen.blit(tmp, self._rect)


    def animation_sequence_ends(self):
        # all sequences end
        self._status = eye_status.waiting

