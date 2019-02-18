class AnimationSequence:
    def __init__(self):
        self._animation_sequence = []
        self._current_animation = -1
        self._ended = False

    def add_animation_sequence(self, anim):
        self._animation_sequence.append(anim)

    def go_next_animation(self):
        if self._current_animation + 1 < len(self._animation_sequence):
            self.set_current_animation(self._current_animation + 1)
            return True
        else:
            self._current_animation = 0
            self._ended = False
            return False

    def rewind_animation(self):
        return self._current_animation

    def set_current_animation(self, num):
        self._current_animation = num

    def set_current_animation_by_name(self, name):
        i = 0
        for x in self._animation_sequence:
            if x._name == name:
                self.set_current_animation(i)
                break
            i += 1

    def get_current_animation(self):
        return self._animation_sequence[self._current_animation] if self._current_animation > -1 else None

    def is_play(self):
        return self._animation_sequence[self._current_animation]._is_play if self._current_animation > -1 else False
