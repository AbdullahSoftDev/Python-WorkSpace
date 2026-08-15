import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style
sns.set_theme()
sns.set_style('darkgrid')

# Distribution
data = np.random.normal(0, 1, 1000)
sns.histplot(data, bins=30, kde=True)

# Pairplot
df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.rand(100)
})
sns.pairplot(df)

# Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

# Boxplot
tips = sns.load_dataset('tips')
sns.boxplot(data=tips, x='day', y='total_bill')

# Violin plot
sns.violinplot(data=tips, x='day', y='total_bill')

# lmplot
sns.lmplot(data=tips, x='total_bill', y='tip')

# Count plot
sns.countplot(data=tips, x='day')