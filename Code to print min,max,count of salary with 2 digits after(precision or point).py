import pandas as pd
df=pd.read_csv(r'C:\Users\Abdullah\Downloads\autos.csv\nba.csv')
print("Minimum of salary is:",f"{df['Salary'].min():.2f}")
print("Maximum of salary is",f"{df['Salary'].max():.2f}")
print("Total count of salary is excluding null",f"{df['Salary'].count():.2f}")