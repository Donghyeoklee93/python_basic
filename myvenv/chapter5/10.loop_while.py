# while
# This is typically used when the number of repetitions is not predetermined.

i = 0
while i < 10:
    print(i)
    i += 1


i = 5
while i < 9:
    print(i)
    i += 1


i = 0
while i < 10:
    print(i)
    i += 2


# Infinite loop
# Creating a loop that always repeats by using True in the condition expression

while True:
    x = input("if you want to shut down, enter exit! >>>")
    if x == "exit":
        break