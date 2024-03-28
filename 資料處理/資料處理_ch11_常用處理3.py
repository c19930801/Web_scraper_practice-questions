import pandas as pd
data={"BatchNo":["a","a","b","b","b","c","c"],
      "Price":[100,80,120,130,200,360,250],
      "Rev":[32434,16543,1564,16543,5000,32434,3456]}
df=pd.DataFrame(data)
print(df)

# 使用groupby()方法以參數BatchNo來群組資料,可以計算出各群組的平均值
df2=df.groupby("BatchNo").mean()
print(df2)