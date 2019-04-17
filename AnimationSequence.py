class AnimationSequence:
    def __init__(self, name, obj, loop=0, repeat=False, wait_start=0, wait_end=0, loop_back=False):
        self._name = name
        self._obj = obj
        self._sequences = []
        self._loop = loop
        self._repeat = repeat
        self._wait_start = wait_start
        self._wait_end = wait_end
        self._loop_back = loop_back
        self._is_play = False
        self._has_played = False
        self._playing_index = -1

    def add_anims(self, anims):
        self._sequences.append(anims)

    def play(self):
        self._is_play = True
        index = -1
        for anim in self._sequences:
            index += 1
            if not anim._has_started or anim._is_play and not anim._has_ended:
                self._playing_index = index
                anim.play()
            elif anim._has_started and not anim._is_play and anim._has_ended:
                self.on_end()

    def on_start(self):
        self._is_play = True
        self._has_played = True

    def on_end(self):
        print("END!", self._name)
        self._obj._animations.on_end(self._name)
        '''if self._playing_index+1 < len(self._sequences):
            self._playing_index'''

