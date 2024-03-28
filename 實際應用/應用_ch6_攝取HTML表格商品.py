from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time,csv

url="https://fchart.github.io/ML/nba_items.html"

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get(url)
#使用BeautifulSoup分析網頁
soup=BeautifulSoup(driver.page_source,"lxml")
#使用CSS選擇器取得<table>標籤
tag_table=soup.select_one("#our-table")
#取得之下所有表格列的<tr>標籤
rows=tag_table.find_all("tr")
# 開啟CSV檔案來寫入資料
with open("NBA_Products.csv","w+",newline="",encoding="utf-8")as fp:
    writer=csv.writer(fp)
    for row in rows:
        lst=[]
        for cell in row.find_all(["td","th"]):
            lst.append(cell.text.replace("\n","").
                       replace("\r","").
                       strip())
        print(lst)
        writer.writerow(lst)
driver.close()