# inheritance
# To eliminate redundant code in classes and facilitate maintenance.

import random


class Monster:
    max_num = 1000
    
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] moves on the ground")


class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}] swims")

class Dragon(Monster):
    #constructor overriding
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("fire attack", "tail attack", "wing attack")

    def move(self):
        print(f"[{self.name}] flies")
    
    def skill(self):
        print(f"[{self.name}] uses skill {self.skills[random.randint(0,2)]}")


wolf = Wolf("wolf", 1500 ,200)
wolf.move()
print(wolf.max_num)

shark = Shark("shark", 3000 ,400)
shark.move()
print(shark.max_num)

dragon = Dragon("dragon", 8000 ,800)
dragon.move()
dragon.skill()
print(dragon.max_num)
