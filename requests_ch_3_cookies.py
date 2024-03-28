import requests 
url="http://httpbin.org/cookies"
cookies=dict(name="Pusheen")
r=requests.get(url,cookies=cookies)
print(r.text)