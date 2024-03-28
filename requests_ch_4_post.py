import requests
url="http://httpbin.org/post"
post_data={"name":"陳會安","grade":95}
r=requests.post(url,data=post_data)
print(r.text)