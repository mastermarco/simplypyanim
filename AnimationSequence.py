class AnimationSequence:
    def __init__(self, name, obj, loop=0, repeat=False, wait_start=0, wait_end=0):
        self._name = name
        self._obj = obj
        self._sequences = []
        self._loop = loop
        self._repeat = repeat
        self._wait_start = wait_start
        self._wait_end = wait_end
        self._is_play = False
        self._has_played = False

    def add_anims(self, anims):
        self._sequences.append(anims)

    def play(self):
        self._is_play = True
        for anim in self._sequences:
            if not anim._has_started or anim._is_play:
                anim.play()

    def on_start(self):
        self._is_play = True
        self._has_played = True

