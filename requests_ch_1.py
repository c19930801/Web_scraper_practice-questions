import requests
url="https://fchart.github.io/test.html"
response=requests.get(url)
if response.status_code==200:
    print(response.text)
    print("編碼",response.encoding)
else:
    print("錯誤!HTTP請求失敗...")


url_params={"name":"陳會安","grade":95}
r=requests.get("https://httpbin.org/get",params=url_params)
print(r.text)