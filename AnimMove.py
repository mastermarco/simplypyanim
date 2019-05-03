from datetime import datetime
from Config import *


class AnimMove:
    def __init__(self, obj, x, y, velocity):
        self._obj = obj
        self._x_end = x
        self._y_end = y
        self._velocity = velocity
        self._velocity_x = None
        self._velocity_y = None
        self.set_velocity(x, y)
        self._is_play = False
        self._has_started = False
        self._has_ended = False
        self._x_direction_right = None
        self._y_direction_top = None

        self._do_loop_back = False
        self._do_loop = False
        self._x_start_tmp = self._x_current_tmp = -1
        self._y_start_tmp = self._y_current_tmp = -1

    def set_velocity(self, x, y):
        if x is None:
            self._velocity_y = self._velocity
        elif y is None:
            self._velocity_x = self._velocity
        else:
            if x > self._obj._rect.left:
                x_tmp = self._obj._rect.left - x
            else:
                x_tmp = x - self._obj._rect.left

            if y > self._obj._rect.top:
                y_tmp = self._obj._rect.top - y
            else:
                y_tmp = y - self._obj._rect.top

            if x_tmp > y_tmp:
                self._velocity_y = self._velocity * y_tmp/x_tmp
                self._velocity_x = self._velocity
            elif x_tmp < y_tmp:
                self._velocity_x = self._velocity * x_tmp/y_tmp
                self._velocity_y = self._velocity
            else:
                self._velocity_x = self._velocity_y = self._velocity

    def set_position_start(self):
        self._x_start = self._x_start_tmp = self._obj._rect.left
        self._y_start = self._y_start_tmp = self._obj._rect.top
        self._x_current = self._x_current_tmp = self._x_start
        self._y_current = self._y_current_tmp = self._y_start

    def reset_for_loop_back(self):
        self._x_end = self._x_start_tmp
        self._y_end = self._y_start_tmp
        self._x_direction_right = None
        self._y_direction_top = None

    def reset(self):
        self._x_start = self._x_start_tmp
        self._y_start = self._y_start_tmp
        self._x_current = self._x_current_tmp
        self._y_current = self._y_current_tmp
        self._x_direction_right = None
        self._y_direction_top = None

    def do_loop_back(self):
        self._do_loop_back = True
        self._has_started = False
        self._is_play = False
        self._has_ended = False

    def do_loop(self):
        self._do_loop = True
        self._has_started = False
        self._is_play = False
        self._has_ended = False

    def on_start(self):
        if self._do_loop_back:
            self.reset_for_loop_back()
        elif self._do_loop:
            self.reset()
        else:
            self.set_position_start()
        self._is_play = True
        self._has_started = True

        if not self._x_end is None:
            if self._x_current < self._x_end:
                self._x_direction_right = True
            else:
                self._x_direction_right = False

        if not self._y_end is None:
            if self._y_current < self._y_end:
                self._y_direction_top = False
            else:
                self._y_direction_top = True

    def play(self):
        if not self._has_started:
            self.on_start()

        if self._is_play:
            if self._x_end is None and self._y_current == self._y_end and self._y_end is None and \
                    self._x_current == self._x_end or self._x_current == self._x_end and self._y_current == self._y_end:
                self.on_end()
            else:
                if self._x_direction_right:
                    self._x_current += self._velocity_x
                    if self._x_current > self._x_end:
                        self._x_current = self._x_end
                elif not self._x_direction_right and not self._x_direction_right is None:
                    self._x_current -= self._velocity_x
                    if self._x_current < self._x_end:
                        self._x_current = self._x_end

                if self._y_direction_top:
                    self._y_current -= self._velocity_y
                    if self._y_current < self._y_end:
                        self._y_current = self._y_end
                elif not self._y_direction_top and not self._y_direction_top is None:
                    self._y_current += self._velocity_y
                    if self._y_current > self._y_end:
                        self._y_current = self._y_end

            if self._x_end is None:
                self._obj.set_position_y(self._y_current)
            elif self._y_end is None:
                self._obj.set_position_x(self._x_current)
            else:
                self._obj.set_position(self._x_current, self._y_current)

    def on_end(self):
        self._is_play = False
        self._has_ended = True
        self._do_loop_back = False
        self._do_loop = False
        print("end!")

