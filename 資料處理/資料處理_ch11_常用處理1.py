import pandas as pd
data={
    "開盤":[184.0,184.5,185.0,182.5,180.5],
    "最高":[185.0,183.5,181.5,185.5,182.5],
    "最低":[183.0,183.5,181.5,182.5,180.5],
    "收盤":[184.0,184.0,182.0,184.5,181.5],
    "Volume":[18569000,20198000,29107000,41130000,82352000]
}
df=pd.DataFrame(data)
df.to_csv("2330.tw.csv",index=False,encoding="utf8")
#------------在DataFrame物件處理日期範圍---------------
#.date_range()方法產生所需的日期範圍,第一個參數開始日
# periods週期參數可以指定產生之後共幾個日期
# freq 參數 "D"是日 :"M"是月
dates_d=pd.date_range("20170109",periods=5,freq="D")
print(dates_d)
pd=pd.read_csv("2330.tw.csv")
# 將上列日期串列新增近DataFrame物件的日期欄位
df["Date"]=dates_d
print(df)
#-------------在DataFrame物件計算百分比的改變--------------
# 呼叫pct_change()方法顯示與前一筆紀錄的百分比變化
print(df["Volume"].pct_change())

#--------------在DataFrame物件找出唯一值----------------
"""
----方法------      ----功能描述----
unique()            找出欄位中的唯一值
nunique()           欄位的不同值有幾種
Value_counts()      計算每一種值出現的次數
"""
print(df["開盤"].unique())
print(df["開盤"].nunique())
print(df["開盤"].value_counts())

