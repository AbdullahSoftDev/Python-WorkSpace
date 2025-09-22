import numpy as np
import pandas as pd
checkup1=np.random.randint(1,100,size=(7))
checkup2=np.random.randint(1,100,size=(7))
checkup3=np.random.randint(1,100,size=(7))
patients=[f'Patient{i+1}'for i in range(7)]
data={
      'Morning':checkup1,
      'Afternoon':checkup2,
      'Night':checkup3,
      }
df=pd.DataFrame(data,index=patients)
df.index.name='Patient_id'
df['Average']=df[['Morning','Afternoon','Night']].sum(axis=1)
print(df)
high=df['Average'].idxmax()
maxxx=df.loc[df['Average'].idxmax()]
print(maxxx)
import matplotlib.pyplot as plt
plt.barh(df.index,df['Average'],color='maroon')
plt.title('Temperature Chart of Patients')
plt.xlabel('Average Temperature')
plt.show()

