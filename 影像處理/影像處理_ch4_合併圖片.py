from PIL import Image
# 使用paste()方法貼上圖片至image物件的指定位置
a_im=Image.open("koala.jpg")
b_im=Image.open("logo.png")
# 先計算出各1/2的中心點後
print(a_im.width,a_im.height)
print(b_im.width,b_im.height)
x=int(a_im.width/2)
y=int(a_im.height/2)
# 分別減去logo.png的尺寸的1/2寬和高 
x=x-int(b_im.width/2)
y=y-int(b_im.height/2)
# 即可呼叫paste()合併圖片
#　第一個參數是欲合併圖片的Ｉｍａｇｅ物件,第二個參數是貼上的位子
a_im.paste(b_im,(x,y))
