#运算
def jia(x,y):
    return x + y

def jian(x,y):
    return x - y

def cheng(x,y):
    return x * y

def chu(x,y):
    return x / y

def main():
    while True:
        x = float(input("请输入第一个数字："))
        y = float(input("请输入第二个数字："))

        print("请选择想要的运算：1.加 2.减 3.乘 4.除")
        choice = input("输入运算（1-4）：")

        if choice == "1":
            result = jia(x,y)
            op = "+"
        elif choice == "2":
            result = jian(x,y)
            op = "-"
        elif choice == "3":
            result = cheng(x,y)
            op = "*"
        elif choice == "4":
            if y == 0:
                print("错误!不能除以0")
                continue
            result = chu(x,y)
            op = "/"
        else:
            print("选择错误！")
            continue

        answer = float(input("{}{}{} = ".format(x,op,y)))

        if answer == result:
            print("回答正确，你好聪明！")
            print("正确答案为：{}".format(result))
        else:
            print("回答错误，继续加油！")
            print("正确答案为：{}".format(result))

        end = input("继续测试吗?（y/n）:")
        if end == "n":
            print("程序结束，欢迎再来哟")
            break
main()
        
