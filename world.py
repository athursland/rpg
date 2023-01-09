# name: Ali Thursland
# date: 2019-11-11
# title: Text-based RPG

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplemented-Error("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return " You find yourself in a cave with a flickering \
        torch on the wall. You can make out four paths, \
        each equally as dark and foreboding."
