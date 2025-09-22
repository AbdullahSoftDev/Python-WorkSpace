import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
months = ['Month 1','Month 2','Month 3','Month 4','Month 5','Month 6',]
data = np.random.randint(1000,2000,size=(6))
df = pd.DataFrame([data], columns=months)
print(df)
plt.figure(figsize=(8,8))
plt.plot(months,data,color='maroon',marker='p')
plt.title('Sales Growth Trend Over Six Months')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
#plt.grid()
#plt.tight_layout()
#marker='s','d','p','o'