from AnimationSequence import AnimationSequence
from AnimMove import AnimMove


class Animations:
    def __init__(self, obj):
        self._sequences = []
        self._obj = obj
        self._is_play = False
        self.setup_animations()
        self._frame_to_play = []
        self.setup_frames_to_play(["move_left"])

    def setup_animations(self):
        anims = []
        anims.append(AnimMove(self._obj, 100, None, 1))
        #anims.append(AnimMove(self._obj, 0, None, 1))
        self.add_animations("move_left", anims)
        anims.clear()

    def add_animations(self, name, anims):
        tmp = AnimationSequence(name, self._obj)
        for anim in anims:
            tmp.add_anims(anim)
        self._sequences.append(tmp)

    def setup_frames_to_play(self, frames):
        self._frame_to_play.clear()
        self._frame_to_play = frames

    def draw_frames(self):
        if not self._is_play:
            return

        if len(self._frame_to_play) > 0:
            frame = self._frame_to_play[0]
            anim = self.get_anim_by_name(frame)

            if anim._is_play:
                anim.play()
            elif not anim._has_played:
                anim.on_start()
                anim.play()

    def get_anim_by_name(self, name):
        for anim in self._sequences:
            if name == anim._name:
                return anim
        return None

