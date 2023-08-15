class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("Positive numbber cannot be accpeted")




try:
    num = int(input("Enter negative number >>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("Error occurs!", e)

