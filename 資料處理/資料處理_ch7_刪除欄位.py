import pandas as pd
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
print(df)
# drop()方法刪除第2筆和第4筆
df2=df.drop(["Bus","Car"])
# 使用index[[0,2]]刪除第1筆和第3筆
df3=df.drop(df.index[[0,2]])
# 刪除欄位需要指定 axis 參數值是1
df4=df.drop(["輪數"],axis=1)
print(df2)
print(df3)
print(df4)