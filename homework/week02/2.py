import math
r = float(input ("请输入圆半径："))
h = float(input ("请输入圆柱高："))
l = 2 * math.pi * r
v = math.pi * r ** 2 * h
print("圆周长:{:.2f}".format(l))
print("圆柱体积:{:.2f}".format(v))
