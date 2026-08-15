import matplotlib.pyplot as plt
import numpy as np

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
x = np.linspace(0, 10, 100)
axes[0,0].plot(x, np.sin(x), 'b-')
axes[0,0].set_title('Sin')

# Plot 2
axes[0,1].plot(x, np.cos(x), 'r-')
axes[0,1].set_title('Cos')

# Plot 3
axes[1,0].scatter(np.random.rand(50), np.random.rand(50))
axes[1,0].set_title('Scatter')

# Plot 4
axes[1,1].hist(np.random.normal(0, 1, 1000), bins=30)
axes[1,1].set_title('Histogram')

plt.tight_layout()
plt.show()

# Gridspec
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(2, 3)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1:])