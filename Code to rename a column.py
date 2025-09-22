import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
df.rename(columns={'Salary':'Tankhawa'},inplace=True)
print(df.dtypes)