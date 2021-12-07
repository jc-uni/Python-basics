from animal import Animal

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = "cat"
        self.latin_name = "felicidae"
        self.tameable = True
        self.sound = "meow"
