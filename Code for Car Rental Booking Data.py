import numpy as np
import pandas as pd
np.random.seed(1)
cars=np.array(['Sedan','Suv','Hatch','Van','Pickup'])
book=np.array(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
days=np.random.randint(1,30,size=(6,5))
df=pd.DataFrame(days,index=book,columns=cars)
df.index.name='Bookings'
total=df.sum(axis=0)
print(df)
total=total.sort_values(ascending=False)
print(total)
import matplotlib.pyplot as plt
plt.pie(total,labels=(total.index))
plt.title('Car Rental System')
plt.tight_layout()
plt.show()