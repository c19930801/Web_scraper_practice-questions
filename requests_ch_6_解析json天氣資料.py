import requests
import json
url="https://openweathermap.org/data/2.5/weather?id=1673820&appid=439d4b804bc8187953eb36d2a8c26a02"
response=requests.get(url)
data=json.loads(response.text)

# 取得天氣描述
weather_desc=data["weather"][0]["description"]
# 取得溫度
temperature=data["main"]["temp"]
# 取得濕度
humidity=data["main"]["humidity"]

# 顯示天氣資訊
print("天氣描述",weather_desc)
print("溫度",temperature)
print("濕度",humidity)