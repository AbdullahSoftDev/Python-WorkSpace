import matplotlib.pyplot as plt
months=['July','Aug','Sep','Oct','Nov','Dec']
tsale=(1200,1300,1100,500,1260,1500)
products=['abc1','abc2','abc3','abc4','abc5']
products_sales=(400,300,250,500,350)
plt.figure(figsize=(16,6))
plt.subplot(1,2,1)
plt.bar(months,tsale,color=['skyblue','red','black','pink','blue'])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.subplot(1,2,2)
plt.bar(products, products_sales,color=['red', 'orange', 'green', 'blue', 'purple'])
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
#plt.fill_between()
