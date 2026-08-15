import pandas as pd

# Reading data
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')
df = pd.read_sql('SELECT * FROM table', connection)

# Describe data
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns

# Data cleaning
df.isnull().sum()
df.dropna()
df.fillna(0)
df.drop_duplicates()

# Grouping
df.groupby('Category').mean()
df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'mean'})

# Merge
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['A', 'B']})
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 80]})
merged = pd.merge(df1, df2, on='ID')

# Pivot
pivot = df.pivot_table(values='Sales', index='City', columns='Product', aggfunc='sum')