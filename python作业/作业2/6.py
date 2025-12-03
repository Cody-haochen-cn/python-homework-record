p = input("请输入七个大写字母:")
for i in p:
    if ord("A") <= ord(i) <= ord("Z"):
        print(chr(ord(i)+32))
    else:
        print("您输入的不是大写字母！")
