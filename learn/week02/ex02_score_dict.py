score_int_list = []
score = input("请输入成绩：")
score = score.split(",")
for s in score:
    clean_score = s.strip()
    int_score = int(clean_score)
    score_int_list.append(int_score)

count_dict = {}
for d in score_int_list:
    if d in count_dict:
        count_dict[d] += 1
    else:
        count_dict[d] = 1

print("成绩列表：", score_int_list)
print("成绩出现次数：", count_dict)