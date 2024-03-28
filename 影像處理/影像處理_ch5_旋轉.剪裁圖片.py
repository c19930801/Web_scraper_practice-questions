from PIL import Image
im=Image.open("koala.jpg")
# 旋轉圖片(一) 使用rotate()方法來旋轉圖片,參數是逆時鐘的角度
im2=im.rotate(45)
# 旋轉圖片(二) 希望旋轉時連圖片尺寸也一起更動,使用transpose()
im2=im.transpose(Image.Transpose.ROTATE_90)
"""上述參數值有
Image.Transpose.FLIP_LEFT_RIGHT 左右旋轉
Image.Transpose.TOP_DOWN 上下旋轉
Image.Transpose.ROTATE_90 逆時鐘旋轉90度
Image.Transpose.ROTATE_180 逆時鐘旋轉180度
Image.Transpose.ROTATE_270 逆時鐘旋轉270度
"""
# 剪裁圖片 使用crop() 四個元素,分別是左上角和右下角剪裁的長方形範圍
im2=im.crop((50,100,300,400))