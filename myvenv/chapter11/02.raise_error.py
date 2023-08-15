# raise statement 
try:
    num = int(input("Enter negative number >>>"))
    if num >= 0:
        raise ValueError("Positive number cannot be accpeted")
except ValueError as e:
    print("Error occurs!", e)

