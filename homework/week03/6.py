# 输入一个不超过4位的整数
n = int(input("请输入一个不超过4位的整数："))

# 不考虑符号，所以取绝对值
n_abs = abs(n)

# 转为字符串便于处理
s = str(n_abs)

# 1. 输出位数
print("它是{}位数".format(len(s)))

# 2. 分别输出每一位数字
print("每位数字为：", end="")
print(" ".join(s))

# 3. 逆序输出
rev = s[::-1]
print("逆序输出为：{}".format(rev))
