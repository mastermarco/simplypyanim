from datetime import datetime
from Config import *

class Anim:
    def __init__(self, obj, loops, wait, name, rect, shape="rect", text="", on_start={}, on_end={}, text_color=""):
        self._shape = shape
        self._text = text
        self._textsurface = None
        self._text_color = text_color
        self._obj = obj
        self._obj_rect = None
        self._obj_rect_backup = None
        self._text_rect = list(rect)
        self._loops = loops
        self._loops_step = 0
        self._wait = wait * 1000
        self._wait_steps = 0
        self._waiting = False
        self._end_wait = False
        self._is_play = False
        self._is_ended = False
        self._name = name

        self._movex = False
        self._movex_vel = None
        self._finalX = None
        self._movex_end = None
        self._movex_vel_tmp = None

        self._movey = False
        self._movey_vel = None
        self._finalY = None
        self._movey_end = None
        self._movey_vel_tmp = None

        self._translate = False

        self._scalex = False
        self._scalex_vel = None
        self._finalScaleX = None
        self._scalex_end = None
        self._scalex_vel_tmp = None

        self._scaley = False
        self._scaley_vel = None
        self._finalScaleY = None
        self._scaley_end = None
        self._scaley_vel_tmp = None

        self._scale = False

        self._stay = False
        self._stay_backup = None

        self._total_animations = 0
        self._total_animations_backup = 0

        self._on_start = dict(on_start)
        self._on_end = dict(on_end)

    def play(self):
        if not self._is_ended:
            if self._obj_rect is None:
                self.resetRect()
                self.onStart()
            self._is_play = True
            if not self._stay:
                if self._movex and not self._movex_end:
                    if self._movex_vel is None:
                        self._movex_vel = self._movex_vel_tmp if self._finalX > self._obj._rect[0] else -self._movex_vel_tmp
                    self._obj_rect[0] += self._movex_vel
                    if (self._movex_vel > 0 and self._obj_rect[0] >= self._finalX) or \
                            (self._movex_vel < 0 and self._obj_rect[0] <= self._finalX):
                        self._obj_rect[0] = self._finalX
                        self._total_animations -= 1
                        self._movex_end = True
                if self._movey and not self._movey_end:
                    if self._movey_vel is None:
                        self._movey_vel = self._movey_vel_tmp if self._finalY > self._obj._rect[1] else -self._movey_vel_tmp
                    self._obj_rect[1] += self._movey_vel
                    if (self._movey_vel > 0 and self._obj_rect[1] >= self._finalY) or \
                            (self._movey_vel < 0 and self._obj_rect[1] <= self._finalY):
                        self._obj_rect[1] = self._finalY
                        self._total_animations -= 1
                        self._movey_end = True
                if self._scalex and not self._scalex_end:
                    if self._scalex_vel is None:
                        self._scalex_vel = self._scalex_vel_tmp if self._finalScaleX > self._obj._rect[2] else -self._scalex_vel_tmp
                    self._obj_rect[2] += self._scalex_vel
                    self._obj_rect[0] -= self._scalex_vel/2
                    if (self._scalex_vel > 0 and self._obj_rect[2] >= self._finalScaleX) or \
                            (self._scalex_vel < 0 and self._obj_rect[2] <= self._finalScaleX):
                        self._obj_rect[2] = self._finalScaleX
                        self._total_animations -= 1
                        self._scalex_end = True
                if self._scaley and not self._scaley_end:
                    if self._scaley_vel is None:
                        self._scaley_vel = self._scaley_vel_tmp if self._finalScaleY > self._obj._rect[3] else -self._scaley_vel_tmp
                    self._obj_rect[3] += self._scaley_vel
                    self._obj_rect[1] -= self._scaley_vel/2

                    if (self._scaley_vel > 0 and self._obj_rect[3] >= self._finalScaleY) or \
                            (self._scaley_vel < 0 and self._obj_rect[3] <= self._finalScaleY):
                        self._obj_rect[3] = self._finalScaleY
                        self._total_animations -= 1
                        self._scaley_end = True
            #else:
                #print("stay")
            self._obj.set_rect(self._obj_rect)
        if self._total_animations == 0 and not self._stay:
            # handle if need to wait or loop or it's ended
            if not self._is_ended and self._wait > 0 and self._wait_steps == 0:
                self._wait_steps = datetime.now()
            elif not self._is_ended and self._wait > 0 and self.millis() < self._wait:
                self._waiting = True
            elif not self._is_ended and self._wait > 0 and self._waiting and self.millis() >= self._wait:
                self._waiting = False
                self._end_wait = True
            elif not self._is_ended and self._loops > 0 and self._loops_step < self._loops:
                self._loops_step += 1
                self.resetObj()
                self.resetAnim()
            else:
                self.endAnimation()
                self.resetAnim()

    def onStart(self):
        if len(self._on_start):
            for x in self._on_start:
                setattr(self._obj, x, self._on_start[x])

    def endAnimation(self):
        self._obj_rect = None
        self._is_ended = True
        self._total_animations = self._total_animations_backup = 0
        self._wait_step = 0
        self._waiting = False
        self._end_wait = False
        self._loops_step = 0
        if len(self._on_end):
            for x in self._on_end:
                setattr(self._obj, x, self._on_end[x])

    def resetAnim(self, holdon=False):
        self._total_animations = self._total_animations_backup = 0
        self._movex_vel = None
        self._movey_vel = None
        self._scalex_vel = None
        self._scaley_vel = None
        self._movex_end = False
        self._movey_end = False
        self._scalex_end = False
        self._scaley_end = False
        self._stay = self._stay_backup
        self._is_ended = not holdon
        #self._is_play = False
        if not self._finalX is None:
            self.moveX(self._finalX, self._movex_vel_tmp)
        if not self._finalY is None:
            self.moveY(self._finalY, self._movey_vel_tmp)
        if not self._finalScaleX is None:
            self.scaleX(self._finalScaleX, self._scalex_vel_tmp)
        if not self._finalScaleY is None:
            self.scaleY(self._finalScaleY, self._scaley_vel_tmp)

    def resetRect(self):
        if self._shape == "rect":
            self._obj_rect = [self._obj._rect.left, self._obj._rect.top, self._obj._rect.width, self._obj._rect.height]
            self._obj_rect_backup = list(self._obj_rect)
        elif self._shape == "text":
            self._textsurface = self._obj._font.render(self._text, False, self._text_color)
            print(self._textsurface.get_width(), self._textsurface.get_height())
            self._obj_rect_backup = [self._obj._rect.left, self._obj._rect.top, self._obj._rect.width, self._obj._rect.height]
            self._obj._rect.left = self._text_rect[0]
            self._obj._rect.top = self._text_rect[1]
            self._obj._rect.width = self._textsurface.get_width()
            self._obj._rect.height = self._textsurface.get_height()
            self._obj_rect = [self._text_rect[0], self._text_rect[1], self._textsurface.get_width(), self._textsurface.get_height()]


    def resetObj(self):
        # used for loop so it need to reset the original rect
        # this happen during the play when self._obj_rect is None
        # self._obj.set_rect(self._obj_rect_backup)
        self._obj_rect[0] = self._obj_rect_backup[0]
        self._obj_rect[1] = self._obj_rect_backup[1]
        self._obj_rect[2] = self._obj_rect_backup[2]
        self._obj_rect[3] = self._obj_rect_backup[3]

    def millis(self):
        dt = datetime.now() - self._wait_steps
        ms = int((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000)
        return ms

    def moveX(self, finalX, vel):
        self._movex = True
        self._finalX = finalX
        self._total_animations += 1
        self._total_animations_backup += 1
        self._movex_end = False
        self._movex_vel_tmp = vel

    def moveY(self, finalY, vel):
        self._movey = True
        self._finalY = finalY
        self._total_animations += 1
        self._total_animations_backup += 1
        self._movey_end = False
        self._movey_vel_tmp = vel

    def translate(self, finalX, finalY, vel):
        self.moveX(finalX, vel)
        self.moveY(finalY, vel)

    def scaleX(self, finalSizeX, vel):
        self._scalex = True
        self._finalScaleX = finalSizeX
        self._total_animations += 1
        self._total_animations_backup += 1
        self._scalex_end = False
        self._scalex_vel_tmp = vel

    def scaleY(self, finalSizeY, vel):
        self._scaley = True
        self._finalScaleY = finalSizeY
        self._total_animations += 1
        self._total_animations_backup += 1
        self._scaley_end = False
        self._scaley_vel_tmp = vel

    def scale(self, finalSizeX, finalSizeY, vel):
        self.scaleX(finalSizeX, vel)
        self.scaleY(finalSizeY, vel)

    def stay(self):
        self._stay = self._stay_backup = True

