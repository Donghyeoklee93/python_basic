class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] is [{self.price}]")

    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] is dropped")
        else:
            print(f"[{self.name}] cannot be dropped")

class Wearable_item(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}] is worn. [{self.effect}]")


class Usable_item(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}] is used. [{self.effect}]")


#instances
sword = Wearable_item("sword", 30000, 3.5, True, "Increase health by 5000, increase mana by 5000")
sword.wear()
sword.sale()
sword.discard()


potion = Usable_item("potion", 150000, 0.1, False, "Transparent effect lasts for 300 seconds")
potion.use()
potion.sale()
potion.discard()