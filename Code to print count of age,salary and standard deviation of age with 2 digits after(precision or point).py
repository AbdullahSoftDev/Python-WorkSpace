import pandas as pd
df=pd.read_csv(r'C:\Users\Abdullah\Downloads\autos.csv\nba.csv')
print("Total values in age column: ",f"{df['Age'].count():.2f}")
print("Total values in salary column: ",f"{df['Salary'].count():.2f}")
print("Standard deivation of age with points: ",f"{df['Age'].std():.2f}")