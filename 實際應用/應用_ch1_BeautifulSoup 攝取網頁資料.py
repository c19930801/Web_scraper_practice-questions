from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
# 載入網站取得<title>標籤
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)
# 建立BeautifulSoup物件
# driver.page_source屬性是Selenium取得的HTML網路標籤
soup=BeautifulSoup(driver.page_source,"lxml")
tag_ol=soup.find("ol",{"id":"list"})
tag_li=tag_ol.find_all("li",class_="line")
for tag in tag_li:
    print(tag.text)
driver.quit()