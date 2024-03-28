import csv
import requests
from bs4 import BeautifulSoup

# 取得HTNL內容
url="https://fchart.github.io/test/album.html"
response=requests.get(url)
html=response.text
# 解析HTML內容
soup=BeautifulSoup(html,"lxml")
parent_tag=soup.select_one('body>main>div>div>div')
child_tags=parent_tag.select("div.col-md-4")
#儲存照片資訊到CSV檔案
with open("photos.csv","w",newline="",encoding="utf-8")as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["照片","描述文字","贊助金額","瀏覽數"])
    
    for tag in child_tags:
        #取得照片網址
        photo_url=tag.select_one('.card-img-top')['src']
        #取得描述文字.贊助金額和瀏覽數
        description=tag.select_one('.card-text').text.strip()
        price=tag.select_one('.price').text.strip()
        views=tag.select_one('.text-muted').text.strip()
        #寫入CSV檔案
        writer.writerow([photo_url,description,price,views])