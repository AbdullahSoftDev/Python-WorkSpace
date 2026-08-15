import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Line plot
df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=100),
    'Value': np.random.randn(100).cumsum()
})
fig = px.line(df, x='Date', y='Value', title='Time Series')
fig.show()

# Scatter plot
df = pd.DataFrame({
    'X': np.random.rand(100),
    'Y': np.random.rand(100),
    'Size': np.random.rand(100) * 100,
    'Color': np.random.rand(100)
})
fig = px.scatter(df, x='X', y='Y', size='Size', color='Color')
fig.show()

# Bar chart
df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, 80, 60, 120]
})
fig = px.bar(df, x='Product', y='Sales', title='Sales by Product')
fig.show()

# Histogram
fig = px.histogram(df, x='Sales', nbins=10)
fig.show()

# Box plot
fig = px.box(df, y='Sales')
fig.show()