import requests

url="https://openweathermap.org/data/2.5/weather?id=1673820&appid=439d4b804bc8187953eb36d2a8c26a02"
r=requests.get(url)
print(r.text)