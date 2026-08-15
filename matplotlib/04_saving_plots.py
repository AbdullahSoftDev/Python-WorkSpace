import matplotlib.pyplot as plt
import numpy as np

# Save figure
plt.figure()
plt.plot(np.random.rand(10))
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf')
plt.savefig('plot.svg')

# Multiple formats
plt.savefig('plot.jpg', quality=95)
plt.savefig('plot.eps')
plt.savefig('plot.tiff')

# Save with options
plt.savefig('plot.png', 
           dpi=300, 
           facecolor='white', 
           edgecolor='none',
           transparent=True,
           bbox_inches='tight')

# Close figure
plt.close()