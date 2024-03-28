import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用 chrome 遊覽器的 service 物件安裝 web Driver
service=Service(ChromeDriverManager().install())
# 設定 driver 的選項
options=webdriver.ChromeOptions()

# 開啟無頭模式

# 使用web Driver的service啟動瀏覽器
driver=webdriver.Chrome(service=service,options=options)

#載入網站
driver.get("https://fchart.github.io/test/infinitescroll.html")
# 捲動 5 次
for i in range(5):
    # 捲動到頁面底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 等待網頁載入新的資料
    time.sleep(2)
    # 顯示目前的網頁內容的字串長度
    print(len(driver.page_source))

# 關閉瀏覽器
driver.quit()