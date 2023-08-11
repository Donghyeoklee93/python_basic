# loop
# When you want to use a command repeatedly

# sequence data type
# : Ordered data types
# 1. list
# 2. string
# 3. range object
# 4. tuple
# 5. dictionary

# for statement
# - using list

champions = ["Teemo", "Ezreal", "Lee Sin"]

for champion in champions:
    print("choosed champion is", champion)

# using string

fighting_message = "Let's have confidence! There are no limits to me!"
for word in fighting_message:
    print(word)


# using range object
# range(10) -> 0 ~ 9 

for i in range(10):
    print(i)


for i in range(1,10):
    print(i)

for i in range(1,10, 2):
    print(i)