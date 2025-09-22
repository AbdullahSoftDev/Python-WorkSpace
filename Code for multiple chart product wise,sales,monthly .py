import matplotlib.pyplot as plt
months = ['July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tsale = (1200, 1300, 1100, 500, 1260, 1500)
products = ['abc1', 'abc2', 'abc3', 'abc4', 'abc5']
products_sales = (400, 300, 250, 500, 350)
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 1)
plt.bar(months, tsale, color='skyblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.subplot(2, 2, 2)
plt.bar(products, products_sales, color='pink')
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.subplot(2, 2, 3)
region = ['East', 'West', 'North', 'South']
population = (400, 300, 250, 500)
plt.fill_between(region, population, color='maroon')
import numpy as np
plt.subplot(2, 2, 4)
data=np.random.randint(18,70,size=(2000))
plt.hist(data,bins=10,color='orange')
plt.show()
