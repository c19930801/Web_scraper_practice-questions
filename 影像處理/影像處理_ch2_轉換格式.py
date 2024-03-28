from PIL import Image

im=Image.open("logo.jpg")
print(im.format,im.size,im.mode)
print("轉換輸出成PNG格式...")
im.save("logo.png")
# save()方法如果沒有第2個參數,就是以附檔名決定圖檔格式
print("轉換輸出成GIF格式...")
im.save("logo.gif","GIF")
