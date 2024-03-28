import pandas as pd
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
print(df)
# set_index 方法的第一個參數是作為列索引的欄位,inplace參數True表示直接取代目前的DataFrane物件
df.set_index("種類",inplace=True)
print(df)