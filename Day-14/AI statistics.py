import numpy as np
data = np.array([10, 20, 20, 30, 40, 50, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Std:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

import pandas as pd

# Create/load dataset
df = pd.read_csv("Day-14/students.csv")

# 1. See first 5 rows
print(df.head())

# 2. See rows and columns
print(df.shape)

# 3. See information about columns
print(df.info())

# 4. Statistical summary
print(df.describe())

# 5. Check missing values
print(df.isnull().sum())

# 6. Count unique values in each column
print(df.nunique())

# 7. Count how many times each value appears
print(df["branch"].value_counts())