import numpy as np
import pandas as pd
np.random.seed(1)
Electronics=np.random.randint(20,100,size=(10))
Clothing=np.random.randint(20,100,size=(10))
Books=np.random.randint(20,100,size=(10))
Date=[f'May{i+1}'for i in range(10)]
days=[f'Day{i+1}'for i in range(10)]
data={
      'Date':Date,
      'Electronics':Electronics,
      'Clothing':Clothing,
      'Books':Books,
      }
df=pd.DataFrame(data,index=days)
df.index.name='Days'
print(df)
df['Total sales']=df[['Electronics','Clothing','Books']].sum(axis=1)
print(df)
maxxx=df.loc[df['Total sales'].idxmax()]
print(maxxx)
import matplotlib.pyplot as plt
plt.plot(df.index,df['Total sales'])
plt.title('Daily Total Sales')
plt.xlabel('Days')
plt.ylabel('Total Sales')
plt.xticks(rotation=30)
plt.grid()
plt.show()
