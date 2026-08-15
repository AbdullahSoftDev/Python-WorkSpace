import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# 3D scatter
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
fig.show()

# Surface plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.show()

# Multiple traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1,2,3], y=[2,3,1], mode='lines', name='Line'))
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,1,2], mode='markers', name='Markers'))
fig.show()

# Subplots
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Scatter(x=[1,2,3], y=[2,3,1]), row=1, col=1)
fig.add_trace(go.Bar(x=['A','B','C'], y=[1,3,2]), row=1, col=2)
fig.show()

# Interactive features
fig.update_layout(
    title='Interactive Plot',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    hovermode='x',
    template='plotly_dark'
)