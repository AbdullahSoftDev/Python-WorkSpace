import pandas as pd
df = pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
team=df.groupby('Team')['Salary'].median()
print(team)