# 1. Substitution operation
# variable name = data

# 2. Arithmetic operation
# number operation
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) #Quotient
print(x % y) #Remainder
print(x ** y) #Square

# string operation
tag1 = "#tag1"
tag2 = "#tag2"
tag3 = "#tag3"

tag = tag1 + tag2 + tag3
print(tag)

message = "We love Python.\n" * 5
print(message)

# Compound assignment operator
level = 10
level += 1 # level = level + 1

health = 2000
health -= 300 # health = health - 300

attack = 300
attack *= 1.5 # attack = attack * 1.5

speed = 420
speed /= 2 # speed = speed / 2

print(level, health, attack, speed)
