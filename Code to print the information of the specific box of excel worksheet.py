import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\autos.csv\autos.csv",low_memory=False)
print(df.iloc[0,2])