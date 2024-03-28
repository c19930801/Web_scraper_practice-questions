import requests
url="https://www.taifex.com.tw/cht/3/totalTableDate"
post_data="queryType=1&goDay=&doQuery=1&dateaddcnt=1&queryDate=2024%2F01%2F11"
r=requests.post(url,data=post_data)
print(r.text)