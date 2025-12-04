# 这里是 Cody 的乱玩实验场
import random

def random_op():
    ops = ["+", "-", "*", "/"]
    return random.choice(ops)

if __name__ == "__main__":
    for _ in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random_op()
        print(f"{a} {op} {b}")
