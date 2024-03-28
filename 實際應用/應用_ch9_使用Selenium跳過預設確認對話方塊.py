from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# 開啟Chrome瀏覽器
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#前往網頁
driver.get("https://fchart.github.io/test/login.html#")
#輸入使用者名稱和密碼,並點擊登入按鈕
username_input=driver.find_element(by='css selector',value='.login-form-field[name="username"]')
username_input.send_keys("mary")

password_input=driver.find_element(by='css selector',value='.login-form-field[name="password"]')
password_input.send_keys("12345678")

login_button=driver.find_element(by='css selector',value='#login-form-submit')
login_button.click()

time.sleep(2)
# driver.swith_to.alert 切換至預設的確認對話方塊
alert=driver.switch_to.alert
#呼叫 accept()來接受此對話方塊
alert.accept()
# 取得標籤
title=driver.title
print(title)