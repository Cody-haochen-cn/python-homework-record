def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return None
    return x / y
def get_op(x,y):
    print("请输入想要的计算 1.加 2.减 3.乘 4.除")
    op = input("")
    if op == "1":
        return add(x,y)
    elif op == "2":
        return sub(x,y)
    elif op == "3":
        return mul(x,y)
    elif op == "4":
        return div(x,y)
    else:
        return None
def main():
    while True:
        try:
            x = float(input("请输入x的值："))
            y = float(input("请输入y的值："))
        except ValueError:
            print("输入有效数字")
            continue
        result = get_op(x,y)
        if result is None:
            if y == 0:
                print("y不能为零")
            else:
                print("无效的操作")
            continue
        print("计算结果为：",result)
        get_continue = input("是否继续（y/n）")
        if get_continue == "n":
            break
main()