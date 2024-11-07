from scene.scene import Scene


class Transaction:

    def __init__(self, currentValidScenes:dict[str, Scene]) -> None:
        super().__init__()
        self.currentValidScenes = currentValidScenes

    def run(self):
        pass



