scores = []
for i in range(10):
    s = float(input(f"请输入第{i+1}个评委的分数："))
    scores.append(s)
max_score = max(scores)
min_score = min(scores)
total = sum(scores) - max_score - min_score
average = total / (len(scores)-2)
print("选手平均得分为：",average)
