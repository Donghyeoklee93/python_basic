class Monster:
    def say(self):
        print("I am moster")

goblin = Monster()
goblin.say()


#In Python, data types are also classes.
a = 10
b = "string object"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())

