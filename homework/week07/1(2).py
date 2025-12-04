def get_scores():
    scores = []
    for i in range(1,16):
        while True:
            s = input("请输入第{}门成绩：".format(i))
            try:
                score = float(s)
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("成绩不能超过一百或小于0")
            except ValueError:
                print("输入有误")
    return scores

def my_sum(all_scores):
    total = 0
    for x in all_scores:
        total += x
    return total

def my_average(total,quantity):
    return total / len(quantity)

n = get_scores()
s = my_sum(n)
a = my_average(s,n)
print("成绩总分{},平均分{}".format(s,a))
