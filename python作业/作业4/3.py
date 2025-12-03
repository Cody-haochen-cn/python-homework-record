for i in range(100,401):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if i == a * a *a + b * b * b + c * c * c:
        print("水仙花数为{}".format(i))
