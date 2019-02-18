class Anim:
    def __init__(self, obj, loops, wait, name):
        self._obj = obj
        self._obj_rect = [obj._rect.left, obj._rect.top, obj._rect.width, obj._rect.height]
        self._obj_rect_backup = [obj._rect.left, obj._rect.top, obj._rect.width, obj._rect.height]
        self._loops = loops
        self._loops_step = 0
        self._wait = wait
        self._wait_steps = 0
        self._is_play = False
        self._is_ended = False
        self._name = name
        self._movex = False
        self._movey = False
        self._translate = False
        self._scalex = False
        self._scaley = False
        self._scale = False
        self._total_animations = 0
        self._total_animations_backup = 0

    def play(self):
        if not self._is_ended:
            self._is_play = True
            if self._movex and not self._movex_end:
                self._obj_rect[0] += self._movex_vel
                print(self._obj_rect[0])
                if (self._movex_vel > 0 and self._obj_rect[0] == self._finalX) or \
                        (self._movex_vel < 0 and self._obj_rect[0] == self._finalX):
                    self._obj_rect[0] = self._finalX
                    self._total_animations -= 1
                    self._movex_end = True
            if self._movey and not self._movey_end:
                self._obj_rect[1] += self._movey_vel
                if (self._movey_vel > 0 and self._obj_rect[1] == self._finalY) or \
                        (self._movey_vel < 0 and self._obj_rect[1] == self._finalY):
                    self._obj_rect[1] = self._finalY
                    self._total_animations -= 1
                    self._movey_end = True
            if self._scalex and not self._scalex_end:
                self._obj_rect[2] += self._scalex_vel
                self._obj_rect[0] -= self._scalex_vel/2
                if (self._scalex_vel > 0 and self._obj_rect[2] == self._finalScaleX) or \
                        (self._scalex_vel < 0 and self._obj_rect[2] == self._finalScaleX):
                    self._obj_rect[2] = self._finalScaleX
                    self._total_animations -= 1
                    self._scalex_end = True
            if self._scaley and not self._scaley_end:
                self._obj_rect[3] += self._scaley_vel
                self._obj_rect[1] -= self._scaley_vel/2
                if (self._scaley_vel > 0 and self._obj_rect[3] == self._finalScaleY) or \
                        (self._scaley_vel < 0 and self._obj_rect[3] == self._finalScaleY):
                    self._obj_rect[3] = self._finalScaleY
                    self._total_animations -= 1
                    self._scaley_end = True
            self._obj.set_rect(self._obj_rect)
        if self._total_animations == 0:
            # TODO handle if need to wait or loop or it's ended
            if self._loops > 0:
                self.resetObj()
                self.resetAnim()


    def resetObj(self):
        self._obj.set_rect(self._obj_rect_backup)
        self._obj_rect[0] = self._obj_rect_backup[0]
        self._obj_rect[1] = self._obj_rect_backup[1]
        self._obj_rect[2] = self._obj_rect_backup[2]
        self._obj_rect[3] = self._obj_rect_backup[3]

    def resetAnim(self):
        self._total_animations = self._total_animations_backup
        self._movex_end = False
        self._movey_end = False
        self._scalex_end = False
        self._scaley_end = False

    def moveX(self, finalX, vel):
        self._movex = True
        self._finalX = finalX
        self._total_animations += 1
        self._total_animations_backup += 1
        self._movex_end = False
        self._movex_vel = vel if self._finalX > self._obj._rect[0] else -vel

    def moveY(self, finalY, vel):
        self._movey = True
        self._finalY = finalY
        self._total_animations += 1
        self._total_animations_backup += 1
        self._movey_end = False
        self._movey_vel = vel if self._finalY > self._obj._rect[1] else -vel

    def translate(self, finalX, finalY, vel):
        self.moveX(finalX, vel)
        self.moveY(finalY, vel)

    def scaleX(self, finalSizeX, vel):
        self._scalex = True
        self._finalScaleX = finalSizeX
        self._total_animations += 1
        self._total_animations_backup += 1
        self._scalex_end = False
        self._scalex_vel = vel if self._finalScaleX > self._obj._rect[2] else -vel

    def scaleY(self, finalSizeY, vel):
        self._scaley = True
        self._finalScaleY = finalSizeY
        self._total_animations += 1
        self._total_animations_backup += 1
        self._scaley_end = False
        self._scaley_vel = vel if self._finalScaleY > self._obj._rect[3] else -vel

    def scale(self, finalSizeX, finalSizeY, vel):
        self.scaleX(finalSizeX, vel)
        self.scaleY(finalSizeY, vel)
