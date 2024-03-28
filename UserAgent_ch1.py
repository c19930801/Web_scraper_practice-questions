from fake_useragent import UserAgent
ua=UserAgent()
#產生各瀏覽器的User-agent字串
print(ua.ie)
print(ua.google)
print(ua.firefox)
print(ua.safari)
#random 可以產生隨機的瀏覽器的User-agent字串
print(ua.random)

