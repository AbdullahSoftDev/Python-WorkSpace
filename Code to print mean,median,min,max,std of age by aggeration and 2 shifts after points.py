import pandas as pd
df = pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
print(df['Age'].agg(['mean', 'median', 'min', 'max', 'std']).apply(lambda x: f"{x:.2f}"))