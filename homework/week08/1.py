with open("满江红.txt", "w", encoding="utf-8")as f:
    f.write("满江红")

with open("满江红.txt", "r", encoding="utf-8")as f:
    content = f.read()
    print("读取到的内容：{}".format(content))
