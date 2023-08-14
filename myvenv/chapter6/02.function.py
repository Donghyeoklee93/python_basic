# basic
import random


def print_hello():
    print("Hello")

print_hello()


# function with parameter
def sum(a, b):
    print(a + b)

sum(3, 4)

# function with return
def get_random_number():
    number = random.randint(1,10)
    return number

print(get_random_number())

# function with parameter and return
def add(a, b):
    result = a + b
    return result

print(add(5, 6))

