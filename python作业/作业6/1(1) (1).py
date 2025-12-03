a = float(input("请输入第一个值："))
b = float(input("请输入第二个值："))
#自定义最小函数
def min(a,b):
    if a > b:
        return b
    else:
        return a
print("最小值为：",min(a,b))
