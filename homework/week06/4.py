result = 1
def jie(n):
    global result
    for i in range(1,n+1):
        result = result * i
    return result
n = int(input("请输入整数n:"))
jie(n)
print("{}的阶乘结果为：{}".format(n,result))
