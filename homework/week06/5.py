print("递归方法")
def jie(n):
    if n == 0:
        return 1
    else:
        return n * jie(n-1)
add = 0
n = int(input("请输入整数n:"))
while n > 0:
    add = add + jie(n)
    n = n - 1
print("递归的阶乘结果为：{}".format(add))


print("-----------------------")


print("一般方法")
def general(x):
    normal = 1
    for i in range(1,x+1):
        normal = normal * i
    return normal
x = int(input("请输入整数n:"))
ad = 0
while x > 0:
    ad = ad + general(x)
    x = x - 1
print("一般的阶乘结果为：{}".format(ad))
