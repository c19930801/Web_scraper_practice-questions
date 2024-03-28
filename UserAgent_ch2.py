from fake_useragent import UserAgent
import requests
ua=UserAgent()
headers={'user-agent':ua.random}

url="https://www.momoshop.com.tw/main/Main.jsp"
r=requests.get(url,headers=headers)
print(r.status_code)
print(r.text)