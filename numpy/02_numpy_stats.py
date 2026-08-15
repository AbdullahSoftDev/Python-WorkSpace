import numpy as np

# Random data
data = np.random.normal(0, 1, 1000)

# Statistics
print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.var(data))
print(np.min(data))
print(np.max(data))
print(np.percentile(data, 75))

# Correlation
x = np.random.rand(100)
y = 2 * x + np.random.rand(100) * 0.1
print(np.corrcoef(x, y))

# Linear algebra
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
print(np.linalg.inv(a))
print(np.linalg.eig(a))
print(np.linalg.det(a))