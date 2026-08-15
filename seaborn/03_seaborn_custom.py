import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Custom palettes
sns.set_palette('husl')
sns.color_palette('coolwarm')

# Different styles
sns.set_style('whitegrid')
sns.set_style('darkgrid')
sns.set_style('ticks')
sns.set_style('white')

# Custom color
with sns.axes_style('darkgrid'):
    plt.figure()
    sns.scatterplot(data=tips, x='total_bill', y='tip', color='red')

# FacetGrid
g = sns.FacetGrid(tips, col='day', row='sex')
g.map(sns.scatterplot, 'total_bill', 'tip')

# Multi-plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0])
sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[1])
plt.show()