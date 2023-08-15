# input won and exchange rate -> dollar

won = input("enter won value >>>")
dollar = input("enter exchange rate >>>")

try:
    print(int(won) / int(dollar))
except ValueError as e:
    print("Value error occurs", e)
except ZeroDivisionError as e:
    print("Dividing by zero cannot be possible.", e)
else:
    print("Exception doesn't occur")
finally:
    print("Code that is awalys run")




print("program")