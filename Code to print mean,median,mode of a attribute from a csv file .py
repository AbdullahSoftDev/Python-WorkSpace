import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\autos.csv\study_performance.csv")
print()
print("Median",df['math_score'].median())
print("Mean",df['math_score'].mean())
print("Mode",df['math_score'].mode())