import random

# 1~50 的随机整数
answer = random.randint(1, 50)

count = 0     # 记录用户猜的次数

while True:
    s = input("请输入你猜的数(1~50 的整数)：")

    try:
        n = int(s)   # 尝试按整数转换
    except ValueError:
        # 不是整数（字母、浮点数、其它非法字符）
        print("输入有误：必须输入整数！请重新输入。\n")
        continue

    # 到这里说明是整数了，计数+1
    count += 1

    # 也可以顺便判断是否在1~50范围内（老师一般会默认加上这个）
    if n < 1 or n > 50:
        print("请输入 1~50 之间的整数！\n")
        continue

    if n < answer:
        print("你猜小了！\n")
    elif n > answer:
        print("你猜大了！\n")
    else:
        print("恭喜你，猜对了，你一共猜了 {} 次。".format(count))
        break
