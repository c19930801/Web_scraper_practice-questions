from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://fchart.github.io/Example.html")
tag_ol=driver.find_element(By.XPATH,'//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup=BeautifulSoup(tag_ol.get_attribute('innerHTML'),"lxml")
tags_li=soup.find_all("li",class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()