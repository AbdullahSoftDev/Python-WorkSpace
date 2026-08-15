import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Multiple lines
y2 = np.cos(x)
plt.plot(x, y, label='sin')
plt.plot(x, y2, label='cos')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='red', s=50)
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.bar(categories, values)
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, alpha=0.7)
plt.show()

# Box plot
data = [np.random.normal(0, 1, 100) for _ in range(4)]
plt.boxplot(data)
plt.show()