from pprint import pprint


class AnimationSequence:
    def __init__(self):
        self._animation_sequence = []
        self._current_animation = -1
        self._ended = False
        self._animation_sequence_array = []
        self._animation_sequence_array_index = -1

    def add_animation_sequence(self, anim):
        self._animation_sequence.append(anim)

    def rewind_animation(self):
        return self._current_animation

    def set_current_animation(self, num):
        self._current_animation = num

    def set_current_animation_by_name(self, name):
        # it find the animation with name and play till the end
        curranim = self.get_current_animation()
        if not curranim is None:
            curranim.reset()
        i = 0
        for x in self._animation_sequence:
            if x._name == name:
                self.set_current_animation(i)
                break
            i += 1

    def set_current_animation_sequence(self, lst):
        curranim = self.get_current_animation()
        if not curranim is None:
            curranim.endAnimation()
            curranim.resetAnim()

        self._animation_sequence_array = list(lst)
        self._animation_sequence_array_index = 0
        self.set_current_animation(lst[self._animation_sequence_array_index])
        curranim = self.get_current_animation()
        #print("_obj_rect_default", curranim._obj_rect_default)
        #curranim._obj_rect = curranim._obj_rect_default
        #curranim._obj_rect_backup = [curranim._obj._rect.left, curranim._obj._rect.top, curranim._obj._rect.width, curranim._obj._rect.height]
        curranim._is_ended = False
        curranim.resetRect()
        #pprint(vars(curranim), indent=2)

    def handle_next_animation(self):
        curranim = self.get_current_animation()
        if not curranim is None:
            curranim.endAnimation()
            curranim.resetAnim()
        if self.go_next_animation_sequence():
            an = self.get_current_animation()
            if not an is None:
                an._is_ended = False
                #an.resetRect()
                an.play()

    def go_next_animation(self):
        if self._current_animation + 1 < len(self._animation_sequence):
            self.set_current_animation(self._current_animation + 1)
            return True
        else:
            self._current_animation = 0
            self._ended = False
            return False

    def go_next_animation_sequence(self):
        if self._animation_sequence_array_index + 1 < len(self._animation_sequence_array):
            self._animation_sequence_array_index += 1
            self.set_current_animation(self._animation_sequence_array[self._animation_sequence_array_index])
            return True
        else:
            return False

    def get_current_animation(self):
        return self._animation_sequence[self._current_animation] if self._current_animation > -1 else None

    def is_play(self):
        curranim = self.get_current_animation()
        if not curranim is None:
            return curranim._is_play
        else:
            return False
