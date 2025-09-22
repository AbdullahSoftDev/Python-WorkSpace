import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------------------------
plt.figure(figsize=(16,12))
months = ['July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tsale = (1200, 1300, 1100, 500, 1260, 1500)
plt.subplot(4, 1, 1)
plt.bar(months, tsale, color='skyblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
#--------------------------------------------------------
products = ['abc1', 'abc2', 'abc3', 'abc4', 'abc5']
products_sales = (400, 300, 250, 500, 350)
plt.subplot(4, 1, 2)
plt.bar(products, products_sales, color='pink')
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
#--------------------------------------------------------
region = ['East', 'West', 'North', 'South']
population = (400, 300, 250, 500)
plt.subplot(4, 1, 3)
plt.fill_between(region, population, color='maroon')
#--------------------------------------------------------
data=np.random.randint(18,70,size=(2000))
plt.subplot(4, 1, 4)
plt.hist(data,bins=10,color='orange',edgecolor='black')
plt.show()
#--------------------------------------------------------
