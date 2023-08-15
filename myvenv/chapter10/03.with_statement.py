# if using with, file close is run automatically 
with open("./myvenv/chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)
