import pandas as pd
df=pd.read_csv(r'C:\Users\Abdullah\Downloads\autos.csv\nba.csv')
print("Mean of salary is:",f"{df['Salary'].mean():.2f}")
print("Median of salary is",f"{df['Salary'].median():.2f}")
print("Mode of salary is",f"{df['Salary'].mode().loc[0]:.2f}")