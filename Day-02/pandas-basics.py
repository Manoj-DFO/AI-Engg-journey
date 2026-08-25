import pandas as pd
data={'NAME':['A','B','C','D','E'] ,'AGE':[22,21,21,21,22],'MARKS':[9,99,78,78,66]}
df=pd.DataFrame(data)
print(df)
df['AGE']
print(df.head())
print(df.tail())
print(df.columns)
print(df.dtypes)
print(df.shape)
print(df[['NAME','AGE']])
print(df[(df['MARKS']<80) & (df['AGE'] == 21)])
print(df[(df['MARKS']<80) | (df['AGE'] == 21)])
print(df.sort_values('MARKS', ascending=False))
df['marks for 200'] = df['MARKS']*2
print(df)
df['AGE'] = df['AGE'] + 1
print(df)
df['PASS'] = df['MARKS'] >= 40
print(df)

df.to_csv('Day-02/students.csv', index=False)
df2 = pd.read_csv('Day-02/students.csv')
print(df2)