def calculate_bmi(weight, height):
    """
    计算BMI指数
    :param weight: 体重(kg)
    :param height: 身高(m)
    :return: BMI指数
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    根据BMI值判断体重类别
    :param bmi: BMI指数
    :return: 体重类别
    """
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif 24 <= bmi < 28:
        return "偏胖"
    else:
        return "肥胖"

# 获取用户输入
weight = float(input("请输入您的体重(kg)："))
height = float(input("请输入您的身高(m)："))

# 计算BMI
bmi = calculate_bmi(weight, height)

# 输出结果
print(f"您的BMI指数为：{bmi:.2f}")
print(f"体重状态：{get_bmi_category(bmi)}")