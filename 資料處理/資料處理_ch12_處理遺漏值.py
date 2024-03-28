import pandas as pd
#遺漏值:許多資料檔都含有特定數量的遺漏資料。 導致資料遺漏的原因很多。 例如，調查受訪者可能沒有回答每個問題、特定變數可能不適用於部分觀察值，以及編碼錯誤可能導致部分值被擲出。
df=pd.read_csv("test.csv")
print(df.head())# 顯示前5筆資料

# 使用info方法顯示诶一個欄位有多少個非NaN欄位值
print(df.info())
# 刪除欄位需要指定 axis 參數值是1
df=df.drop(["Cabin"],axis=1)
print("-----------------")
#----------------刪除NaN的紀錄--------------------
print(df["Age"].isnull().sum()) #isnull()可以判断所有的空值 sum()總數
# 因為NaN不能進行運算,所以呼叫dropna()方法刪除掉,subset屬性可以指定刪除那些欄位有NaN的紀錄
df2=df.dropna(subset=["Age"]) 
print(len(df2))
#----------------添補遺漏值--------------------
#　如果不想刪除NaN欄位值得記錄,可以添補遺漏值成固定值、平均值、中位數等
#　使用fillna()方法將"Age"欄位的NaN欄位值都改成參數value的值20
df["Age"]=df["Age"].fillna(value=20)
print(df["Age"].isnull().sum())
# 也可以使用fillna()方法將遺漏值添入mean()方法的平均數
df["Age"]=df["Age"].fillna(df["Age"].mean())



