import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(1)
start_date = np.datetime64('2025-02-01')
end_date = np.datetime64('2025-02-11')
date = np.arange(start_date, end_date, dtype='datetime64[D]')
Electronics = np.random.randint(150880, 250080, 10)
Cloths = np.random.randint(120080, 250000, 10)
Books = np.random.randint(108000, 250880, 10)
data_frame = {
    'Date': date,
    'Electronics': Electronics,
    'Cloths': Cloths,
    'Books': Books
}
df = pd.DataFrame(data_frame)
df['Total Sale'] = df[['Electronics', 'Cloths', 'Books']].sum(axis=1)
max_sale = df.loc[df['Total Sale'].idxmax()]
plt.plot(df['Date'], df['Total Sale'], marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sale')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()