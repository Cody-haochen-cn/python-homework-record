x = float(input("输入x的值："))
if x < 1:
    print("y的值为{}".format(x))
elif 1 <= x <10:
    print("y的值为{}".format(2 * x - 1))
elif x >= 10:
    print("y的值为{}".format(3 * x - 11))
