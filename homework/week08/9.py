import csv
header = ['姓名', '英语', '数学', 'Python', '总分', '平均分']
initial_data = [
    ['张三', 85, 70, 76, 0, 0],
    ['李四', 42, 98, 65, 0, 0],
    ['王五', 98.1, 66.5, 79.5, 0, 0]
]
filename = '学生成绩统计.csv'
with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(initial_data)

print(f"已新建文件 {filename} 并写入初始数据")
processed_data = []
with open(filename, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    processed_data.append(header)
    for row in reader:
        name = row[0]
        english = float(row[1])
        math = float(row[2])
        python = float(row[3])
        total_score = english + math + python
        avg_score = round(total_score / 3, 2)
        new_row = [name, english, math, python, total_score, avg_score]
        processed_data.append(new_row)
print("\n统计之后的学生成绩情况")
print(f"{header[0]:<6} {header[1]:<6} {header[2]:<6} {header[3]:<8} {header[4]:<6} {header[5]:<6}")
for row in processed_data[1:]:
    print(f"{row[0]:<6} {row[1]:<6} {row[2]:<6} {row[3]:<8} {row[4]:<6} {row[5]:<6}")
with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(processed_data)
print(f"\n结果已成功保存至 {filename}")
