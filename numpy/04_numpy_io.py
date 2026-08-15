import numpy as np

# Save and load
arr = np.array([1, 2, 3, 4])
np.save('arr.npy', arr)
loaded = np.load('arr.npy')

# Save multiple arrays
np.savez('arrays.npz', a=arr1, b=arr2)
loaded = np.load('arrays.npz')
print(loaded['a'])

# Text files
np.savetxt('data.txt', arr, delimiter=',')
loaded = np.loadtxt('data.txt', delimiter=',')

# Binary files
arr.tofile('data.bin')
loaded = np.fromfile('data.bin', dtype=np.int64)