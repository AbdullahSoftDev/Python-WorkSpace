import matplotlib.pyplot as plt
import numpy as np
advert=np.random.randint(1,100,10)
revenue=np.random.randint(1,100,10)
plt.scatter(advert,revenue,color='maroon',s=150,alpha=0.8)
plt.xlabel('Revenue Generated')
plt.ylabel('Advertisement')
plt.grid()
plt.show()
#_--------------------------
#pip install wordcloud