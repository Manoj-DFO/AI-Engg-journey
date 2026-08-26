import pandas as pd
data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "age": [20, 21, 19, 22, 21, 20],
    "marks": [85, 72, 91, 65, 88, 76],
    "branch": ["ECE", "CSE", "ECE", "ME", "CSE", "ECE"]
}

df = pd.DataFrame(data)
print(df['name'],df['marks'])
print(df[df['marks'] >80])
print(df[df['age'] == 21])
print(df[(df['branch'] == 'ECE') & (df['marks'] > 80)])
a=df['marks'].sum()
b=a/6
print(df['marks'].max())
print(df.sort_values('marks',ascending=False))
print(df['branch'].value_counts())
print(df.shape)
df['PASS'] = df['marks'] >= 40
print(df)