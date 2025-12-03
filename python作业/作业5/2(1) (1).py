for num in range(1,201):    #遍历
    s = 0
    for i in range(1,num):
        if num % i == 0:
            s = i + s

    if s == num:
        print(num)
