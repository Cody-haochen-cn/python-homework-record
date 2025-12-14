students_scores = {
    "张三":"89，76，91",
    "李四":"60，70，80",
    "王五":"100，95，98"
}

def parse_scores(scores_str):
    score_list = scores_str.split("，")
    result = []
    for s in score_list:
        clean = s.strip()
        num = int(clean)
        result.append(num)
    return result

report_list = []
for name, scores in students_scores.items():
    scores = parse_scores(scores)   #将分数变为整数列表
    #总分
    totle = 0
    for i in scores:
        totle = totle + i
    #平均分
    average_score = totle / len(scores)
    average_score = float(average_score)
    #最高分
    max_score = scores[0]
    for n in scores:
        if max_score < n:
            max_score = n
report_list.append((name, totle, average_score, max_score))
#排序
sorted_report = sorted(report_list, key=lambda i: i[2], reverse=True)
#输出
for name, totle, average, max_score in sorted_report:
    print("姓名：", name,
          "总分：", totle,
          "平均分：{:.2f}".format(average),
          "最高分：", max_score)
