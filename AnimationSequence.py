import time

class AnimationSequence:
    def __init__(self, name, obj, loops=0, wait_start=0, wait_end=0, loop_back=False):
        self._name = name
        self._obj = obj
        self._sequences = []

        self._is_play = False
        self._has_played = False

        self._loop_back = loop_back
        self._loop_back_done = False

        self._loops = loops
        self._loops_tmp = 0

        self._wait_start = wait_start
        self._wait_start_tmp = 0
        self._start_time_tmp = 0

        self._wait_end = wait_end
        self._wait_end_tmp = 0
        self._end_time_tmp = 0

        '''self._is_velocity_set = False'''

    def add_anims(self, anims):
        self._sequences.append(anims)

    '''def set_velocity(self):
        self._is_velocity_set = True
        # loop trough all the animation to set up the single velocity
        print("to do set velocity")
        # first get the shorter one for x and h
        velocity_x = 1000
        velocity_y = 1000
        for anim in self._sequences:
            print(anim, anim._velocity_x, anim._velocity_y, velocity_x, velocity_y)
            if not anim._velocity_x is None and anim._velocity_x < velocity_x:
                print("x", anim._velocity_x, anim)
                velocity_x = anim._velocity_x
            if not anim._velocity_y is None and anim._velocity_y < velocity_y:
                print("y", anim._velocity_y, anim)
                velocity_y = anim._velocity_y
        # then assign it to all
        for anim in self._sequences:
            if not anim._velocity_x is None:
                anim._velocity_x = velocity_x
            if not anim._velocity_y is None:
                anim._velocity_y = velocity_y

        print(velocity_x, velocity_y)'''

    def play(self):
        '''if not self._is_velocity_set:
            self.set_velocity()'''

        if not self._is_play:
            self.on_start()

        for anim in self._sequences:
            if not anim._has_started or anim._is_play and not anim._has_ended:
                if self._wait_start == 0 or int(time.time() - self._start_time_tmp) >= self._wait_start:
                    anim.play()
            elif anim._has_started and not anim._is_play and anim._has_ended:
                # check here if needs loop and so on..
                if self._loop_back and not self._loop_back_done:
                    self._loop_back_done = True
                    anim.do_loop_back()
                    self.reset()
                elif not self._loop_back and self._loops > 0 and self._loops_tmp + 1 <= self._loops:
                    # Loops are allowed if it's not indicated loop_back
                    self._loops_tmp += 1
                    anim.do_loop()
                    self.reset()
                else:
                    if self._wait_end > 0 and self._end_time_tmp == 0:
                        self._end_time_tmp = time.time()
                    if self._wait_end == 0 or int(time.time() - self._end_time_tmp) >= self._wait_end:
                        self.on_end()

    def on_start(self):
        self.reset()
        self._is_play = True
        self._has_played = True
        self._start_time_tmp = time.time()

    def reset(self):
        self._wait_start_tmp = 0
        self._start_time_tmp = 0
        self._wait_end_tmp = 0
        self._end_time_tmp = 0

    def reset_loop(self):
        self._loops_tmp = 0

    def reset_loop_back(self):
        self._loop_back_done = False

    def on_end(self):
        self.reset_loop()
        self.reset_loop_back()
        self._obj._animations.on_end(self._name)

