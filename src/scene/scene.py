from src.terminal.utils import slow_typing


class Scene:

    def __init__(self, id, description, typing_speed=0.15):
        self.id = id
        self.description = description
        self.typing_speed = typing_speed

    def show_description(self):
        slow_typing(self.description, self.typing_speed)
        print('')
