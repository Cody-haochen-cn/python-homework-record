import random
i = random.randint(1,50)
m = 0
guess = int(input("猜的数："))
while guess != i:
    if guess < i:
        print("输小了！")
    else:
        print("输大了！")
    guess = int(input("猜的数："))
    m = m + 1
print("恭喜你，猜对了，你猜了{}次,正确数字为{}".format(m,guess))
