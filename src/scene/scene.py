from src.terminal.utils import slow_typing


class Scene:

    def __init__(self, scene_id, description, typing_speed=None):
        self.scene_id = scene_id
        self.description = description
        if typing_speed is None:
            self.typing_speed = 0.15

    def show_description(self):
        slow_typing(self.description, self.typing_speed)
