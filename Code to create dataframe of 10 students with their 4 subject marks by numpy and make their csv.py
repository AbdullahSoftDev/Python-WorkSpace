import numpy as np
import pandas as pd
np.random.seed(1)
students=np.arange(1001,1011)
big_data=np.random.randint(65,93,10)
dbms=np.random.randint(70,95,10)
data=np.random.randint(43,64,10)
d=({
    'Student ID': students,
    'Big data': big_data,
    'DBMS': dbms,
    'Data structures': data
    })
#print('Students=',students,'\n','Big data=',big_data,'\n','DBMS=',dbms,'\n','Data structures=',data)
d=pd.DataFrame(d)
print(d)
d.to_csv('Students.csv')