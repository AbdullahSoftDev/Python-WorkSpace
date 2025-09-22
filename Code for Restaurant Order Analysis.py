import numpy as np
item=np.array(['Burger', 'Pizza', 'Pasta', 'Salad'])
days=np.array([f'Day {i+1}' for i in range(7)])
orders=np.random.randint(1,10,size=(4,7))
import pandas as pd
df=pd.DataFrame(columns=days,data=orders,index=item)
df.index.name='Items'
df.loc['Total Orders per day']=df.sum(axis=0)
print(df)
daily=df.drop('Total Orders per day')
maxxx=daily.sum(axis=1).idxmax()
print("Most popular dish overall:",maxxx)
import matplotlib.pyplot as plt
daily.plot(kind='bar', stacked=True)
plt.title('Daily Orders for Each Dish')
plt.xlabel('Order Items')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
