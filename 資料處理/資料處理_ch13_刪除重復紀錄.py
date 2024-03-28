import pandas as pd
data={"Rep":["Tom","Joe","Jack","Joe","Mary","Tom","Jinie","Jane","John","Joe","Jack","Jinie"],
      "Country":["USA","Canada","Canada","china","Japan","USA","Brazil","USA","Canada","Brazil","Japan","Brazil"],
      "Amount":[32434,16543,1564,16543,5000,32434,5243,5000,2346,6643,6465,5243]}
df=pd.DataFrame(data)
print(df)
#------------------刪除重復紀錄-----------------
#使用.drop_duplicates()方法刪除重復紀錄(完全相同的)
df1=df.drop_duplicates()
print(df1)
#------------------刪除重復的欄位值--------------------
df1=df.drop_duplicates("Country")
print(df1)