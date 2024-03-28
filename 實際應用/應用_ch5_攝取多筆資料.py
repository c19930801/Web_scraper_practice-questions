from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

url="https://fchart.github.io/Ashion/#"
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url)
#使用BeautifulSoup分析網頁
soup=BeautifulSoup(driver.page_source,"lxml")
# 使用find方式 用class屬性值"product spad"定位<"section">父標籤
sec=soup.find("section",class_="product spad")
#呼叫.find_all方法取出之下所有<div>子標籤,和顯示紀錄數
items=sec.find_all("div",class_="product__item")
print(len(items))
#建立products空串列後,使用for迴圈取出每一筆紀錄來建立python字典
products=[]
for item in items:
    #商品名稱
    tag=item.find("h6").find("a")
    #並用單行選擇條件判斷當物件存在時,才取出標籤或屬性值
    title=tag.text.strip() if tag else "N/A" 
    #產品圖片
    tag=item.find("div",class_="product__item__pic")
    img=tag["data-setbg"].strip() if tag else "N/A"
    #價格
    tag=item.find("div",class_="product__price")
    price=tag.text.strip() if tag else "N/A"
    print(title)
    products.append({
        "title":title,
        "image":url+img,
        "price":price
    })
    driver.quit()
    with open("ashion.json","w",encoding="utf-8") as fp:#寫入json檔案
        json.dump(products,fp,indent=2,
                  sort_keys=True,# 照順序排列
                  ensure_ascii=False) # 解決中文亂碼

