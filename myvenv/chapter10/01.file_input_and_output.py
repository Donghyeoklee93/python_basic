#write file
file = open("./myvenv/chapter10/data.txt", "w", encoding="utf8")
file.write("1. python with lee")
file.close()

#add file
file = open("./myvenv/chapter10/data.txt", "a", encoding="utf8")
file.write("\n2. Even non-experts can learn it really easily")
file.close()

#read file
file = open("./myvenv/chapter10/data.txt", "r", encoding="utf8")

#read all file
data = file.read()
print(data)
file.close()

#read file by line
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()