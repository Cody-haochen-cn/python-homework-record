a = int (input("请输入任意三位整数:"))
f = abs(a)
b = f // 100
c = f % 100 // 10
d = f % 10
e = str(d) + str(c) + str(b)
print(e)
