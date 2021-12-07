from animal import Animal

class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.name = "bear"
        self.latin_name = "arctus arctus"
        self.tameable = False
        self.sound = "roar"