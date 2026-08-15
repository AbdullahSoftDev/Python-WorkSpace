import seaborn as sns
import matplotlib.pyplot as plt

# Jointplot
tips = sns.load_dataset('tips')
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')

# KDE plot
sns.kdeplot(data=tips, x='total_bill', hue='day', fill=True)

# Pairplot with categories
sns.pairplot(data=tips, hue='sex')

# Barplot with confidence
sns.barplot(data=tips, x='day', y='tip', ci=95)

# Catplot
sns.catplot(data=tips, x='day', y='total_bill', hue='sex', kind='violin')

# Matrix plots
flights = sns.load_dataset('flights')
pivot = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')

# Regression
sns.regplot(data=tips, x='total_bill', y='tip', order=2)

# Diagonal plots
sns.distplot(tips['total_bill'], hist=True, kde=True)