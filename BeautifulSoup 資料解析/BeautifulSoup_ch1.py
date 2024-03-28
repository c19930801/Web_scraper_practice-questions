from bs4 import BeautifulSoup
import requests

url="https://fchart.github.io/"
response= requests.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.text,"lxml")
    taps=soup("a")
    for tag in taps:
        print(tag.get("href",None))
else:
    print("錯誤!HTTP請求失敗")
