from pathlib import Path
scores_path = Path(__file__).resolve().parent / "scores.txt"

def parse_scores(scores_str):
    score_list = scores_str.split("，")
    result = []
    for s in score_list:
        clean = s.strip()
        num = int(clean)
        result.append(num)
    return result

report_list = []

#打开txt文件
with open(scores_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            name_part, score_part = line.split(":", 1)
        elif "：" in line:
            name_part, score_part = line.split("：", 1)
        else:
            print("格式错误", line)
            continue
        name = name_part.strip()
        score_str = score_part.strip()

        scores = parse_scores(score_str)   #将成绩变为整数列表
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
for name, totle, average_score, max_score in sorted_report:
    print("姓名：", name,
          "总分：", totle,
          "平均分：{:.2f}".format(average_score),
          "最高分：", max_score)