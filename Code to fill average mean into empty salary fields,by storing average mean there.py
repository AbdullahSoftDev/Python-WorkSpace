import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print(df)