import numpy as np
import matplotlib.pyplot as plt
products = ['TV','Mobile','Tablet','Watches','Charger']
sales=np.random.randint(100,500,5)
plt.bar(products,sales,color=['skyblue','red','black','pink','blue'])
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()