score_int_list = []
score = input("请输入成绩（用英文逗号分隔）：")
score_list = score.split(",")
for s in score_list:
    clean_score = s.strip()
    num = int(clean_score)
    score_int_list.append(num)
total = 0

for i in score_int_list:
    total += i

average = total / len(score_int_list)

max_score = score_int_list[0]
for i in score_int_list:
    if i > max_score:
        max_score = i

print("成绩列表：", score_int_list)
print("总分：", total)
print("平均分：", average)
print("最高分：", max_score)