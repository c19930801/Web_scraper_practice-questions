from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 開啟chrome瀏覽器
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
# 前往表單網頁
driver.get("https://fchart.github.io/test/login.html#")
#輸入使用者名稱和密碼,並點擊登入按鈕
username_input=driver.find_element(by='css selector',value='.login-form-field[name="username"]')
username_input.send_keys("joe")

password_input=driver.find_element(by='css selector',value='.login-form-field[name="password"]')
password_input.send_keys("12345678")

login_button=driver.find_element(by='css selector',value='#login-form-submit')
login_button.click()
# 取得並顯示<title>標籤
title=driver.title
print(title)
