import math
a = float(input("请输入系数a："))
b = float(input("请输入系数b："))
c = float(input("请输入系数c："))
d = b ** 2 - ( 4 * a * c )
if d > 0:
    gen1 = ( - b + math.sqrt(d)) / 2*a
    gen2 = ( - b - math.sqrt(d)) / 2*a
    print("第一个根为：{:.2f}".format(gen1))
    print("第二个根为：{:.2f}".format(gen2))
else:
    print("△不>0")
