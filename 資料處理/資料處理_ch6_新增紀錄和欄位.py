import pandas as pd
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
print(df)

s=pd.Series({"種類":"Bicycle","數量":5,"輪數":2})
# 使用_append()方法,來新增Series物件,ignore_index參數值True是忽略索引
df2=df._append(s,ignore_index=True)
print(df2.tail())
# DataFrame物件只需指定不存在的欄索引,就可以新增欄位
df["奧客數"]=[1,20,4,2]
print(df)