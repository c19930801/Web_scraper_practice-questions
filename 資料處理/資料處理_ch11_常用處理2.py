import pandas as pd
#-------------合併多個DataFrame物件------------------
df1=pd.DataFrame({"Name":["A","B"],"Value":[11,12]})
df2=pd.DataFrame({"Name":["C"],"Value":[23]})
# 呼叫concat()方法合併2個DataFrame物件,ignore_index=True 忽略列索引
df3=pd.concat([df1,df2],ignore_index=True)
print(df3)
# 然後用concat()方法合併欄位
df4=pd.DataFrame({"Name":["A","B"],"Value":[11,12]})
df5=pd.DataFrame({"Size":["XL","L"]})
df6=pd.concat([df4,df5],axis=1) #axis=1是合併欄位
print(df6)