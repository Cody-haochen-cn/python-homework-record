c = float(input("输入成绩："))
if 0 <= c <=100:
    if c >=90:
        print("A")
    elif 80 <= c <90:
        print("B")
    elif 70 <= c <80:
        print("C")
    elif 60 <= c <70:
        print("D")
    else:
        print("E")
else:
    print("错误")
