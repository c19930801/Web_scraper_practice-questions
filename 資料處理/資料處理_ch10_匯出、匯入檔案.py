import pandas as pd

""" # 匯出DataFrame
    方法                         說明
df.to_csv(檔案名稱)        匯出成CSV格式的檔案
df.to_json(檔案名稱)       匯出成json格式的檔案
df.to_html(檔案名稱)       匯出成html格式的檔案
df.to_excel(檔案名稱)      匯出成excel格式的檔案
df.to_sql(table,con=engine)          匯出成SQL資料庫的table參數的資料表,con參數式資料庫連接
"""
data={"種類":["Bike","Bus","Car","Truck"],
      "數量":[3,4,6,2],
      "輪數":[2,4,4,6]}
df=pd.DataFrame(data)
# to_csv方法匯出CSV檔案,第一個參數字串式黨名,
# index參數值決定是否寫入索引,True是寫入;False是不寫入
# encoding編碼是因為有中文字
df.to_csv("vehicles.csv",index=False,encoding="utf8")
# to_json第一個參數是檔名,因為有中文欄名所以要加上參數force_ascii=False
df.to_json("vehicles.json",force_ascii=False)

# --------匯入DataFrame物件-----------
"""
   方法                         說明
df.read_csv(檔案名稱)        匯入CSV格式的檔案
df.read_json(檔案名稱)       匯入json格式的檔案
df.read_html(檔案名稱)       匯入HTML格式的檔案
df.read_excel(檔案名稱)      匯入HTML格式的檔案
df.read_sql(query,engine)    匯入SQL資料庫資料,使用第2個參數的資料庫連接執行第1個參數的SQL指令
"""
df1=pd.read_csv("vehicles.csv",encoding="utf8")
df2=pd.read_json("vehicles.json")
print(df1)
print(df2)