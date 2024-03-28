import re
# 在re模組 search()方法可以在字串中找出範本字串中的第一個符合的子字串 
strl="""joe˙s email is joe@gmail.com,
tom˙s email is tom@yahoo.com.tw"""
match=re.search(r"[\w.-]+@[A-Za-z0-9_.-]+",strl)
print(match.group())