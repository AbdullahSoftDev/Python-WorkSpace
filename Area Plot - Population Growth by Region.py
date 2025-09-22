import matplotlib.pyplot as plt
import numpy as np
region = ['East', 'West', 'North', 'South']
population = np.random.randint(100,1000,4)
plt.title('Population Contribution by Region')
plt.xlabel('Regions')
#plt.xlabel('Regions', fontsize=12)
plt.ylabel('Population ')
#plt.ylabel('Population ', fontsize=12)
plt.grid()
plt.fill_between(region, population, color='maroon')
plt.tight_layout()
plt.show()