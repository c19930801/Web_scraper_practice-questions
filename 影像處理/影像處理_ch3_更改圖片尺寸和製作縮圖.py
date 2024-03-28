from PIL import Image

im=Image.open("logo.jpg")
# 更換成特定的圖片尺寸  resize()方法改變成指定尺寸(寬,高)
im2=im.resize((400,400))
# thumbnail() 方法縮小圖片 
im2=im.thumbnail((400,400))
#　保持比例來更改圖片尺寸,當決定新框度350後,自訂計算出此比例的高度,再用resize方法更改成保持比例的圖片尺寸
new_width=350
ratio=float(new_width)/im.width
new_height=int(im.height*ratio)
im2=im.resize((new_width,new_height))
# 製作縮圖 使用thumbnail()方法製作等比例例縮小的縮圖
"""
thumbnail() 跟 resize() 的不同處是，resize() 可以放大跟縮小，且可以不等比例縮放，而 thumbnail() 只能縮小，且只能等比例縮小，依據輸入參數裡的最短邊為主。
"""