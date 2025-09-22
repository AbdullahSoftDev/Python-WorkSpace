import numpy as np
import matplotlib.pyplot as plt
data=np.random.randint(18,70,size=(2000))
plt.title('Age Distribution in the Community')
plt.xlabel('Age')
plt.ylabel('Number of People')
plt.hist(data,bins=10,color='orange',edgecolor='black')
plt.show()
