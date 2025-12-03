from datetime import datetime
birthday = datetime(2005,6,10)
print(birthday.strftime("%Y-%m-%d"))
print(birthday.strftime("%d/%m/%Y"))
print(birthday.strftime("%B %d %Y"))
print(birthday.strftime("%Y年%m月%d日"))
print(birthday.strftime("%Y，%d %B %Y"))
