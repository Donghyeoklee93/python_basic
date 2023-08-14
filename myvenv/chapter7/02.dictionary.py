stock_a = {"samsung" : 82000, "lg" : 150000}

stock_b = {
    "samsung" : [81000, 81500, 82000, 82000],
    "lg" : (150000, 149000, 148000, 151000, 152000),

}

stock_c = {
    "samsung" : {
        "current_price" : 82000,
        "quantity_held" : 5,
        "purchase_price" : 81000
    }
}

# print(stock_a)
# print(stock_b)
# print(stock_c)

print(stock_a["samsung"])
print(stock_c["samsung"]["quantity_held"])


stock_a["samsung"] = 85000
print(stock_a)

del stock_a["lg"]
print(stock_a)

stock_d = {
    "samsung" : 82000,
    "sk" : 123000,
    "naver" : 370000,
    "kakao" : 133000,
}

print(stock_d.items())

for item in stock_d.items():
    print(item)

for item in stock_d.items():
    print(item[0])

for item in stock_d.items():
    print(item[1])

for key in stock_d.keys():
    print(key)

for value in stock_d.values():
    print(value)