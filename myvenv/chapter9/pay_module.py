# payment information, management module
# variables
version = 2.0

# function
def printAuthor():
    print("lee")

#class
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"
    
if __name__ == "__main__":
    print("pay module is run")

print(__name__)