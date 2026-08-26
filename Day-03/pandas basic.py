#Select method
import pandas as pd
marks=pd.Series([10,20,30,40,50])
print(marks[3])
values=pd.Series([100,200,300,400],index=['a','b','c','d'])
print(values['b'])

data={'name':['a','b','c','d'],'age':[10,11,10,10],'marks':[20,23,21,12]}
df=pd.DataFrame(data)
print(df.info())
print(df.describe())
print(df["marks"].mean())
print(df["marks"].sum())
print(df["marks"].min())
print(df["marks"].max())

print(df["age"].value_counts())