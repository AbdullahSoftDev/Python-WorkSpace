import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

# From numpy
arr = np.random.rand(3, 4)
df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])

# Indexing
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])
print(df.loc['row1'])
print(df.iloc[0])

# Column operations
df['Salary'] = [50000, 60000, 70000]
df['Bonus'] = df['Salary'] * 0.1

# Filtering
filtered = df[df['Age'] > 28]