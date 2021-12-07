from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "dog"
        self.latin_name = "canis"
        self.tameable = True
        self.sound = "woof"

