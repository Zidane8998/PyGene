import os

class Constants:
    def __init__(self):
        # Root directory constant that defines the project wide directory root
        # this allows the path references within the application to remain relative to the project root

        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.constants_dir = os.path.join(self.root_dir, 'constants')
        self.gameobject_dir = os.path.join(self.root_dir, 'game_objects')
        self.assets_dir = os.path.join(self.root_dir, 'assets')
