import csv

data = [
    ["name", "class", "number"],
    ["lee", 1, 20],
    ["kim", 3, 8],
    ["park", 5, 32]
]

file = open("./myvenv/chapter10/student.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()