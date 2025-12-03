def factorial(n):
    """计算 n!"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


s = input("请输入整数 n：")

try:
    # 先尝试按整数处理
    n = int(s)
    if n < 0:
        print("错误：n 必须是非负整数！")
    else:
        print(f"{n}! = {factorial(n)}")

except ValueError:
    # 不是整数，再判断是小数还是字符串
    try:
        float(s)           # 能转成 float 说明是小数
        print("错误：输入的是小数，请输入整数！")
    except ValueError:     # 连 float 都转不了，说明是字符串等非法输入
        print("错误：输入的是字符串（或非法字符），请输入整数！")

    
