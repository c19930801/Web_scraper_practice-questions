import pandas as pd
"""
----功能描述------          ----屬性或方法----
顯示前5筆、顯示後5筆        df.head()、df.tail()
取得列索引、欄索引和資料     df.index、df.columns、df.values
取得記錄數和形狀            len(df)、df.shape
顯示資料類別的摘要資料       df.info()
顯示統計摘要資料            df.describe()
"""
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
print(df)
# ---------顯示前幾筆和後幾筆紀錄-------------
# 呼叫head()方法顯示前幾筆紀錄,參數是筆數,沒有指定是預設值5筆,tail()方法是後5筆
print(df.head(2))#顯示前2筆
print(df.tail(3))#顯示後3筆
#----------取得DataFrame物件的列索引、欄索引和資料-----------
print(df.index) # 取得列索引
print(df.columns)# 取得欄索引
print(df.values)# 取得資料
print(df.values[2]) #取出第3筆["car"6 4]
print(df.values[1][2])# 取出第2筆第3欄的資料: 4
#----------顯示DataFrame物件和紀錄數和形狀---------
print(len(df))#取得記錄數: 4
print(df.shape)#取得形狀: (4, 3)
#----------顯示DataFrame物件的摘要資訊---------
print(df.info())# 顯示資料類別的摘要資料
print(df.describe())# 顯示統計摘要資料
