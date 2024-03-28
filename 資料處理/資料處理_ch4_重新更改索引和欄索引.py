import pandas as pd
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
print(df)

labels=["A","B","E","D"]
# 使用colums屬性重新指定欄索引(橫向)
df.columns=["Types","Count","Wheels"]
labels[2]="c"
# 使用index屬性更改列索引(直向)
df.index=labels
print(df)