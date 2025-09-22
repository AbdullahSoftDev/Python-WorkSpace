import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
department={
    'HR':np.random.randint(40000,70000,20),
    'Accounts':np.random.randint(30000,90000,20),
    'Finance':np.random.randint(20000,60000,20),
    'IT':np.random.randint(10000,20000,20),
    }
df=pd.DataFrame(department).boxplot()
plt.show()