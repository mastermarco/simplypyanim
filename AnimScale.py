class AnimScale:
    def __init__(self, obj, w, h, velocity):
        self._obj = obj
        self._w_end = w
        self._h_end = h
        self._velocity = velocity
        self._velocity_x = None
        self._velocity_y = None
        self.set_velocity(w, h)
        self._is_play = False
        self._has_started = False
        self._has_ended = False
        self._w_direction_right = None
        self._h_direction_top = None

        self._do_loop_back = False
        self._do_loop = False
        self._w_start_tmp = self._w_current_tmp = -1
        self._h_start_tmp = self._h_current_tmp = -1

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
        self._w_start = self._w_start_tmp = self._obj._rect.width
        self._h_start = self._h_start_tmp = self._obj._rect.height
        self._w_current = self._w_current_tmp = self._w_start
        self._h_current = self._y_current_tmp = self._h_start

    def on_start(self):
        '''if self._do_loop_back:
            self.reset_for_loop_back()
        elif self._do_loop:
            self.reset()
        else:'''
        self.set_position_start()
        self._is_play = True
        self._has_started = True

        if not self._w_end is None:
            if self._w_current < self._w_end:
                self._w_direction_right = True
            else:
                self._w_direction_right = False

        if not self._h_end is None:
            if self._h_current < self._h_end:
                self._h_direction_top = False
            else:
                self._h_direction_top = True

    def play(self):
        if not self._has_started:
            self.on_start()

        if self._is_play:
            if self._w_end is None and self._h_current == self._h_end and self._h_end is None and \
                    self._w_current == self._w_end or self._w_current == self._w_end and self._h_current == self._h_end:
                self.on_end()
            else:
                if self._w_direction_right:
                    self._w_current += self._velocity_x
                    if self._w_current > self._w_end:
                        self._w_current = self._w_end
                elif not self._w_direction_right and not self._w_direction_right is None:
                    self._w_current -= self._velocity_x
                    if self._w_current < self._w_end:
                        self._w_current = self._w_end

                if self._h_direction_top:
                    self._h_current -= self._velocity_y
                    if self._h_current < self._h_end:
                        self._h_current = self._h_end
                elif not self._h_direction_top and not self._h_direction_top is None:
                    self._h_current += self._velocity_y
                    if self._h_current > self._h_end:
                        self._h_current = self._h_end

            if self._w_end is None:
                self._obj.set_scale_y(self._h_current)
            elif self._h_end is None:
                self._obj.set_scale_x(self._w_current)
            else:
                self._obj.set_scale(self._w_current, self._h_current)

    def on_end(self):
        self._is_play = False
        self._has_ended = True
        self._do_loop_back = False
        self._do_loop = False
        print("end!")

