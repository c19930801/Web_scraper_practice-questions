import requests,os
from bs4 import BeautifulSoup

url="https://fchart.github.io/"
os.makedirs("fchart",exist_ok=True) #創建一個目錄
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
#使用for迴圈走訪網頁的所有<img>標籤,使用find_all()找出所有<img>標籤
for img in soup.find_all("img"):
    try:
        # 因為src屬性可能只有部分網址,我們需要自行組合出完整的URL網址
        # 和呼叫replace()方法取代「\「成為「/」字元清理網址,即可用get()方法
        imgUrl=url+img.get("src").replace("\\","/")
        print("下載:",imgUrl)
        res=requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤..")
        continue
    # os.path.join(path, *paths) :聰明地連接一個或多個路徑段。回傳值是 path 和 *paths 的所有成員的串聯
    # os.path.basename(path) :回傳路徑名 path 的基底名稱。這是將 path 傳遞給函式 split() 後回傳結果中的第二個元
    imgFile=os.path.join("fchart",os.path.basename(imgUrl))
    fp= open(imgFile,"wb")
    # 使用for迴圈的目的是為了避免圖檔太大,所以每次回圈只寫入100000個字元
    for chunk in res.iter_content(10000):
        fp.write(chunk)
    fp.close()
print("結束網頁圖檔下載...")
