import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Contour plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z)
plt.colorbar()

# Heatmap
plt.imshow(Z, cmap='hot', aspect='auto')
plt.colorbar()

# Polar plot
theta = np.linspace(0, 2*np.pi, 100)
r = 2 * np.sin(4*theta)
plt.polar(theta, r)

# Pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

# Customizing
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 12