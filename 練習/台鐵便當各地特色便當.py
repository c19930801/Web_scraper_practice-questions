import requests
from bs4 import BeautifulSoup
import json

#首頁取得各區的網址
url="https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/entry"
urls=[]
articles=[]
re=requests.get(url)
#使用BeautifulSoup分析網頁
soup=BeautifulSoup(re.text,"lxml")
# 使用find方式 用class屬性值"bentoshopMap addSea"定位<"div">父標籤
posts=soup.find('div',class_="bentoshopMap addSea")
#呼叫.find_all方法取出之下所有<div>子標籤
st=posts.find_all('div',class_="bentoStore")
for s in st:
    btn=s.find('a')
    btn=btn.get('href')
    btn="https://www.railway.gov.tw"+btn
    urls.append(btn)

# 連接到各分局的網址
for i in range(6):
    out=[]
    re=requests.get(urls[i])
    soup=BeautifulSoup(re.text,"lxml")
    posts=soup.find('div',class_="main-tab-box")
    # 抓出title
    title=posts.find("h3")
    title=title.text
    # 抓出所有便當資料
    box_lunchs=posts.find_all("li")
    for box_lunch in box_lunchs:
        box_name=box_lunch.find("div",class_="pro-title")
        box_name=box_name.text
        out.append(box_name)
    articles.append({
                "分局名稱":title,
                "特色便當":out
    })
with open("tra.json","w",encoding="utf-8")as f:#寫入json檔案
    json.dump(articles,f,indent=2,
              sort_keys=True,# 照順序排列
              ensure_ascii=False) # 解決中文亂碼
    