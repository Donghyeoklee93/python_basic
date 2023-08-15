champion1_name = "lee"
champion1_health = 700
champion1_attack = 90

print(f"Welcome, {champion1_name}")


champion2_name = "kim"
champion2_health = 800
champion2_attack = 95

print(f"Welcome, {champion2_name}")


def basic_attack(name, attack):
    print(f"{name} basic attack {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)

print("===========With using class===========")

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"Welcome, {name}")
    
    def basic_attack(self):
        print(f"{self.name} basic attack {self.attack}")

lee = Champion("lee", 700, 90)
kim = Champion("kim", 800, 95)
park = Champion("pack", 750, 92)
lee.basic_attack()
kim.basic_attack()
park.basic_attack()