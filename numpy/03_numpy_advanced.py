import numpy as np

# Boolean masking
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])

# Where
print(np.where(arr > 3, arr, 0))

# Fancy indexing
arr = np.arange(12).reshape(3, 4)
indices = [0, 2]
print(arr[indices])

# Broadcasting advanced
a = np.array([[1, 2, 3]])
b = np.array([[4], [5], [6]])
print(a + b)

# Axis operations
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

# Copy vs view
arr = np.array([1, 2, 3])
copy = arr.copy()
view = arr.view()