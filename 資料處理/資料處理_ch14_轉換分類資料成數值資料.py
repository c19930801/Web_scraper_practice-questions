import pandas as pd
data={"GenDer":["male","female","not specified","male","female","female"],
      "Size":["XL","M","XXL","L","S","XS"],
      "Price":[800,400,300,500,700,850]}
df=pd.DataFrame(data)
print(df)
# 利用字典建立對應值轉換將欄位資料轉換成數值
size_mapping={"XXL":5,
      "XL":4,
      "L":3,
      "M":2,
      "S":1,
      "XS":0}
df["Size"]=df["Size"].map(size_mapping)
print(df)