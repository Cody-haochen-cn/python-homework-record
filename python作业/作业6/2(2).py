C = eval(input("请输入摄氏温度："))
def temp(C):
    F = C * 1.8 + 32
    return F
print("该摄氏温度对应的华氏温度为：{:.1f}".format(temp(C)))
