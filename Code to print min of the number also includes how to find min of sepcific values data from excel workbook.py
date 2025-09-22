import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Desktop\Workspace\Semester 4\Documents\Extra Documents (Trash)\Numberic data.csv")
print(df.min())
print(df[['Range', 'Radius']].min())