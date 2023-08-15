import csv

data = [
    ["item", "purchase_price", "quantity", "target_price"],
    ["samsung", 85000, 10, 90000],
    ["naver", 380000, 5, 400000]
]


file = open("./myvenv/chapter10/mystock.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()

def show_profile(data):
    name = data[0]
    purchase_price = int(data[1])
    quantity = int(data[2])
    target_price = int(int(data[3]))

    profit = (target_price - purchase_price) * quantity
    profit_ratio = (target_price/purchase_price - 1) * 100

    print(f"{name} {profit} {profit_ratio :.2f}%")

file = open("./myvenv/chapter10/mystock.csv", "r", encoding="utf-8-sig")
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profile(data)
file.close()