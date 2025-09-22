import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(1)
columns = [f'Day_{i+1}' for i in range(7)]
energy_data = np.random.randint(20, 100, size=(5, 7))
df = pd.DataFrame(energy_data, columns=columns)
print(df)
df['Household ID'] = [f'Household_{i+1}' for i in range(5)]
df['Weekly Total'] = df[columns].sum(axis=1)
plt.bar(df['Household ID'], df['Weekly Total'], color='pink')
plt.title('Weekly Energy Usage per Household')
plt.xlabel('Household')
plt.ylabel('Total Energy Consumption (Units)')
plt.show()