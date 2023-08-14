def print_sum_avg(x, y, z):
    sum = x+y+z
    avg = (x+y+z)/3
    print("Total :", sum, "Average :", avg)

print_sum_avg(10, 20, 30)

#string formatting
def sum_avg(x, y, z):
    sum = x+y+z
    avg = (x+y+z)/3
    print(f"Total : {sum} Average : {avg}")

sum_avg(10, 20, 30)