# BeautifulSoup 模組 可以用來解析HTML網站的資料

# 安裝 BeautifulSoup 模組
"""pip install beautifulsoup4
   pip install lxml
"""
# 載入 beautifulSoup 模組
from bs4 import BeautifulSoup

#  取得攝取HTML標籤的相關資訊
"""
tag.text  :  取得HTML標籤內容
tag.attrs :  取得HTML標籤所有屬性的字典
tag["目標"]: 取得HTML標籤的[目標]屬性質 
tag.get("href",NOne) :取得第一個參數href屬性值,沒有此屬性,就回傳第2個參數None

"""
# 搜尋 HTML 標籤
"""
select_one("目標") :使用參數CSS選擇器字串搜尋HTML標籤,可以回傳第一個符合的HTML標籤物件
select("目標") :使用參數CSS選擇器字串搜尋HTML標籤,可以回傳所有符合的HTML標籤物件
find("目標") :使用參數的標籤名稱和屬性值來搜尋HTML標籤,可以回傳第一個符合的標籤物件
find_all("目標") :使用參數的標籤名稱和屬性值來搜尋HTML標籤,可以回傳所有符合的標籤物件
"""
"""
tag=soup.find("li",{"id":"q2"})
用find方法的第一個參數式<li>標籤,第二個參數式屬性字典,即id屬性值是q2"""
# 使用find_next()方法搜尋下一HTML標籤
"""
tag_ans1=soup.find("li",class_="response")
tag_ans = tag_ans1.find_next()
"""
