
korean_word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's learning Korean")
for word in korean_word_list:
    print(word)
    data = input()
    if word != data:
        break