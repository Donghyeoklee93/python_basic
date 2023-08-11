korean = int(input("enter score for Korean >>>"))
math = int(input("enter score for Math >>>"))
english = int(input("enter score for English >>>"))

average = (korean + math + english) / 3

#Code 1
if korean < 0 or math < 0 or english < 0 :
    print("Wrong input")
elif average >= 80:
    print("Pass")
else:
    print("Fail")

#Code 2
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    if average >= 80:
        print("Pass")
    else:
        print("Fail")
else:
    print("Wrong input")