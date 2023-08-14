#Without function
print("Hello, Donghyeok")
print("Remained date for using premium is 30 dates")

print("Hello, Lee")
print("Remained date for using premium is 15 dates")

print("Hello, Kim")
print("Remained date for using premium is 7 dates")

print()

#With function
def print_message(name, date):
    print("Hello,", name)
    print("Remained date for using premium is", date ,"dates")

print_message("Donghyeok", 30)
print_message("Lee", 15)
print_message("Kim", 7)