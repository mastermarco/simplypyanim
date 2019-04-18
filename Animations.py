from AnimationSequence import AnimationSequence
from AnimMove import AnimMove


class Animations:
    def __init__(self, obj):
        self._sequences = []
        self._obj = obj
        self._is_play = False
        self.setup_animations()
        self._frame_to_play = []
        self.setup_frames_to_play(["move_left", "move_bottom", "move_right_top"])
        self._frame_current = -1

    def setup_animations(self):
        anims = []
        anims.append(AnimMove(self._obj, 100, 20, 1))
        #anims.append(AnimMove(self._obj, 0, None, 1))
        self.add_animations("move_left", anims, loop_back=True)
        anims.clear()

        anims.append(AnimMove(self._obj, 100, 80, 1))
        self.add_animations("move_bottom", anims, wait_start=1, loop_back=True, wait_end=5)
        anims.clear()

        anims.append(AnimMove(self._obj, 140, 10, 1))
        self.add_animations("move_right_top", anims)

    def add_animations(self, name, anims, loops=0, wait_start=0, wait_end=0, loop_back=False):
        tmp = AnimationSequence(name, self._obj, loops, wait_start, wait_end, loop_back)
        for anim in anims:
            tmp.add_anims(anim)
        self._sequences.append(tmp)

    def setup_frames_to_play(self, frames):
        self._frame_to_play.clear()
        self._frame_to_play = frames

    def draw_frames(self):
        if not self._is_play or self._frame_current == -1:
            return

        if len(self._frame_to_play) > 0:
            frame = self._frame_to_play[self._frame_current]
            anim = self.get_anim_by_name(frame)

            if not anim == None:
                if anim._is_play:
                    anim.play()
                elif not anim._has_played:
                    anim.play()
            else:
                print("Animation name not found")
                return

    def get_anim_by_name(self, name):
        for anim in self._sequences:
            if name == anim._name:
                return anim
        return None

    def play(self):
        self.on_start()

    def on_start(self):
        self._is_play = True
        self._frame_current = 0

    def on_end(self, animation_name):
        print(animation_name, " is ended!")
        if self._frame_current + 1 < len(self._frame_to_play):
            self._frame_current += 1
        else:
            # TODO: check if it's ok have as default the frame 0
            self._frame_current = -1

