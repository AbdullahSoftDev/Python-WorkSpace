import pandas as pd
df = pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
print(df['Salary'].mean())
df = df.groupby(['Team', 'Position'])['Salary'].mean().reset_index()
df.set_index(['Team', 'Position'], inplace=True)
print(df)
    