import requests

url="https://fchart.github.io/img/Butterfly.png"
r=requests.get(url,stream=True) # stream=True 是回應串流
path='Butterfly.png'
if r.status_code==200: #用if/else條件判斷是否請求成功
    with open(path,'wb') as fp:# 開啟二進位檔案 "WB"是寫入二進位檔案
        for chunk in r: #在for迴圈可以讀取reponse回應串流
            fp.write(chunk) #呼叫write將資料寫入檔案
    print("圖檔已經下載")
else:
    print("錯誤!HTTP請求失敗")
    