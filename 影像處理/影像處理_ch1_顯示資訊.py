from PIL import Image

im= Image.open("logo.jpg")
print("圖檔名稱:",im.filename)
print("圖檔格式:",im.format)
print("圖檔尺寸:",im.size)
print("圖檔模式:",im.mode)
print("圖檔的寬:",im.width)
print("圖檔的高:",im.height)