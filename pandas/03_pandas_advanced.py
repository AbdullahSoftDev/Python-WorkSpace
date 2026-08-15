import pandas as pd
import numpy as np

# Time series
dates = pd.date_range('2023-01-01', periods=365, freq='D')
ts = pd.Series(np.random.randn(365), index=dates)

# Resampling
ts.resample('M').mean()
ts.resample('W').sum()

# Rolling window
ts.rolling(window=7).mean()
ts.rolling(window=7).std()

# Apply functions
df['Age_squared'] = df['Age'].apply(lambda x: x**2)

# Map
df['Age_category'] = df['Age'].map({25: 'Young', 30: 'Adult', 35: 'Senior'})

# String operations
df['Name_upper'] = df['Name'].str.upper()
df['Name_length'] = df['Name'].str.len()

# Date operations
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Multi-index
df.set_index(['Category', 'Product'], inplace=True)

# Export
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx')
df.to_json('output.json')