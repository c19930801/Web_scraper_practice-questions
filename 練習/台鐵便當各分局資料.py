import requests
from bs4 import BeautifulSoup
import json
url="https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/entry"
articles=[]

re=requests.get(url)
#使用BeautifulSoup分析網頁
soup=BeautifulSoup(re.text,"lxml")
# 使用find方式 用class屬性值"bentoshopMap addSea"定位<"div">父標籤
posts=soup.find('div',class_="bentoshopMap addSea")
#呼叫.find_all方法取出之下所有<div>子標籤
st=posts.find_all('div',class_="bentoStore")
for s in st:
    #分局名稱
    links=s.find('h3')
    link=links.text.strip().replace("\n","").replace("\r","")
    #把電話跟地址欄位用for迴圈分開
    num=s.find('p')
    b =[i for i in num.text.split() ]
    num=b[0]
    br=b[1]
    #用.get('href)方法抓出<a>子標籤中的<href>內容
    btn=s.find('a')
    btn=btn.get('href')
    btn="https://www.railway.gov.tw"+btn
    # json屬於表格檔案
    articles.append({
        "分局":link,
        "電話":num,
        "地址":br,
        "網址":btn

    })
with open("tra.json","w",encoding="utf-8")as f:#寫入json檔案
    json.dump(articles,f,indent=2,
              sort_keys=True,# 照順序排列
              ensure_ascii=False) # 解決中文亂碼
    

   
