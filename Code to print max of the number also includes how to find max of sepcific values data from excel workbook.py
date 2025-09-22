import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Desktop\Workspace\Semester 4\Documents\Extra Documents (Trash)\Numberic data.csv")
print(df.max())
print(df[['Range', 'Radius']].max())