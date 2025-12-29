students = {}
#增加
def add_student():
    xh = input("学号：")
    xm = input("姓名：")
    bj = input("班级：")
    xb = input("性别：")
    dh = input("电话：")
    jtdz = input("家庭地址：")
    students[xh] = {
        "姓名":xm,
        "班级":bj,
        "性别":xb,
        "电话":dh,
        "家庭地址":jtdz,
    }
    print("学生信息增加完成")
#修改
def modify_student():
    xh = input("要修改的学号：")
    if xh in students:
        stu = students[xh]
        print("原信息：",students[xh])
        xm = input("新姓名：")
        if xm:
            students["姓名"] = xm
        bj = input("新班级：")
        if bj:
            students["班级"] = bj
        xb = input("新性别：")
        if xb:
            students["性别"] = xb
        dh = input("新电话：")
        if dh:
            students["电话"] = dh
        jtdz = input("新家庭地址：")
        if jtdz:
            students["家庭地址"] = jtdz
    else:
        print("未找到学号")
#删除
def delete_students():
    xh = input("要删除的学号：")
    if xh in students:
        students.pop(xh)
        print("学号删除")
    else:
        print("未找到学号")
#查询
def see_students():
    xh = input("要查找的学号：")
    if xh in students:
        stu = students[xh]
        print("学号：", xh)
        print("姓名：", stu["姓名"])
        print("班级：", stu["班级"])
        print("性别：", stu["性别"])
        print("电话：", stu["电话"])
        print("家庭地址：", stu["家庭地址"])
    else:
        print("未找到该学号")
while True:
    print("1.增加 2.修改 3.删除 4.查询 0.退出")
    choice = input("请选择：")
    if choice == "1":
        add_student()
    elif choice == "2":
        modify_student()
    elif choice == "3":
        delete_students()
    elif choice == "4":
        see_students()
    elif choice == "0":
        break
    else:
        print("输入有误！")