h = float(input("身高："))
w = float(input("体重："))
t = w / (h * h)
if t < 18:
    print("低体重")
elif 18 <= t < 25:
    print("正常体重")
elif 25 <= t < 27:
    print("超重体重")
elif 27 <= t:
    print("肥胖")
