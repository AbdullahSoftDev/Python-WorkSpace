import numpy as np

# Array creation
arr1 = np.array([1, 2, 3, 4])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 4))
arr4 = np.eye(3)
arr5 = np.random.rand(3, 3)

# Array attributes
print(arr1.shape)
print(arr1.dtype)
print(arr1.size)

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a * b)
print(a ** 2)
print(np.sqrt(a))

# Slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:, 1])
print(arr[0, :])
print(arr[1:3, 1:3])

# Reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)

# Broadcasting
a = np.array([1, 2, 3])
b = 2
print(a * b)

# Universal functions
arr = np.array([1, 2, 3, 4])
print(np.sin(arr))
print(np.exp(arr))
print(np.log(arr))