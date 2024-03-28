import re
# 群組抓取是用來取出正規表達式找到符合字串的部分內容,只用「()」誇號預先定義需要取出的部分內容
strl="""joe˙s email is joe@gmail.com,
tom˙s email is tom@yahoo.com.tw"""
match=re.search(r"([\w.-]+)@([A-Za-z0-9_.-]+)",strl)
print(match.group())
print(match.group(1))
print(match.group(2))