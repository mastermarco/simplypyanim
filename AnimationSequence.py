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

    def add_anims(self, anims):
        self._sequences.append(anims)

    def play(self):
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

