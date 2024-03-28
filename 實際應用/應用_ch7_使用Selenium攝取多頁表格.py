from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time,csv

url="https://fchart.github.io/ML/nba_items.html"

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get(url)

# pages_remaining變數判斷是否還有下一頁
pages_remaining=True
# page_num是目前的頁碼
page_num=1
# 然後用while迴圈取出全部分頁的HTML表格資料
while pages_remaining:
    # 使用BeautifulSoup分析HTML標籤字串
    soup=BeautifulSoup(driver.page_source,"lxml")
    # 呼叫select_one()取得<table>標籤
    tag_table=soup.select_one("#our-table")
    # 取得之下所有表格列的<tr>標籤
    rows=tag_table.find_all("tr")
    csvfile="NBA_Products"+str(page_num)+".csv"
    with open(csvfile,"w+",newline="",encoding="utf8")as fp:
        writer=csv.writer(fp)
        #用迴圈取出所有的標題列和資料列
        for row in rows:
            lst=[]
            for cell in row.find_all(["td","th"]):
                lst.append(cell.text.replace("\n","").
                           replace("\r","").
                           strip())
            writer.writerow(lst)
        print("儲存頁面:",page_num)
    try:

        # find_element()方法是使用class屬性來取得按鈕的標籤物件
        next_link=driver.find_element(By.CLASS_NAME,"nextbtn")
        # 條件式判斷是否有此物,如果有就呼叫click()方法模擬按下按鈕
        if next_link:
            next_link.click()
            time.sleep(5)
            page_num=page_num+1
        else:
            pages_remaining=False
    except Exception:
        pages_remaining=False
driver.close()