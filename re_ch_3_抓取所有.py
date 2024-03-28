import re
# 不同於search()方法只可以在字串中找出第一個符合的子字串,findall()方法可以找出所有符合的串列
strl="""joe˙s email is joe@gmail.com,
tom˙s email is tom@yahoo.com.tw"""
match=re.findall(r"[\w.-]+@[A-Za-z0-9_.-]+",strl)
print(match)