import numpy as np
import matplotlib.pyplot as plt
shares=np.random.randint(1,100,size=(4))
brand=['Samsung','Apple','xiaomi','Redmi']
plt.pie(shares,labels=brand,autopct='%1.1f%%',colors=['red','blue','green','yellow'])
plt.grid()
plt.show()