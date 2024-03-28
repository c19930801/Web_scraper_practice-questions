import re 
# 在re模組的compile()方法可以將正規表達式字串建立成樣式物件,當建立此物件後,就可以重復使用
strl="""joe˙s email is joe@gmail.com,
tom˙s email is tom@yahoo.com.tw"""
pattern=re.compile(r"[\w.-]+@[A-Za-z0-9_.-]+")
match=re.search(pattern,strl)
print(match.group())