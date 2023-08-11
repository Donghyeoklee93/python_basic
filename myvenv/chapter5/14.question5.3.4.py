
korean_word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

total_count = len(korean_word_list)
correct_count = 0
wrong_count = 0

print("Let's learning Korean")
for word in korean_word_list:
    print(word)
    data = input()
    if word == data:
        correct_count += 1

print("Total question number :", len(korean_word_list))
print("Total correct number :", correct_count)
print("Total wrong number :", len(korean_word_list) - correct_count)