# inheritance
# To eliminate redundant code in classes and facilitate maintenance.

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] moves on the ground")


class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}] swims")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] flies")


wolf = Wolf("wolf", 1500 ,200)
wolf.move()

shark = Shark("shark", 3000 ,400)
shark.move()

dragon = Dragon("dragon", 8000 ,800)
dragon.move()
