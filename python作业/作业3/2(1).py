# 输入三个实数 a、b、c，按从大到小输出，并输出最大值和最小值

a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input("请输入c："))

# 如果只是为了截图演示，可以把上面的输入语句注释掉，
# 直接用下面一行给 a、b、c 赋值：
# a, b, c = 44.5, 50, 23.9

# 把 a、b、c 排成 a ≥ b ≥ c
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

print("从大到小输出：", a, b, c)
print("最大值为：", a)
print("最小值为：", c)
