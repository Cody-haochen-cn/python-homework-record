s = 0
for i  in range(1,101):
    if i % 3 == 0:
        if i % 5 !=0:
            s = s + i
print("结果为{}".format(s))
