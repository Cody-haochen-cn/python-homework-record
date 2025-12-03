import math
a = float(input("请输入第一条边："))
b = float(input("请输入第二条边："))
c = float(input("请输入第三条边："))
d = a + b + c
p = d / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print ("三角形面积:{:.3f}".format(s))
