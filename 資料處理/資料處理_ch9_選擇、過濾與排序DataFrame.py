import pandas as pd
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
# 使用index參數指定自訂的列索引
df=pd.DataFrame(data,index=["A","B","C","D"])
print(df)
# ---------使用欄索引選取單一或多個欄位--------------
# DataFrame物件可以使用欄索引或欄索引串列,來選取單一欄位或多個欄位
print(df["種類"])
#　使用欄索引串列來同時選取多個欄位
print(df[["數量","輪數"]].head(3)) # 呼叫head()方法顯示前3筆
#----------使用列索引選取特定範圍的紀錄----------------
print(df[0:2])
#如果使用自訂的索引標籤來選取範圍,就會包含最後一筆
print(df["A":"c"])
# df.loc[列索引,欄索引]
print("df.loc['A','數量']")
print(df.loc["A","數量"])
print(df.loc[["C","D"],["數量","輪數"]])
# df.iloc[列索引位置,欄索引位置]
print(df.iloc[3])
print(df.iloc[2:4,1:3])# C,D的數量,輪數
#-----------使用布林條件過濾資料-----------
# 可以使用布林條件,只選擇條件成立的紀錄資料
# 轉換DataFrame資料型態: astype(資料型態)
df["輪數"]=df["輪數"].astype("int64")#.astype方法轉換成整數
print(df[df.輪數>3])
#-----------指定欄索引來排序紀錄資料------------
# sort_values方法指定排序欄位"數量",加上排序方法是從大到小 (ascending=False)
df2=df.sort_values("數量",ascending=False)
print(df2)