import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Desktop\Workspace\Semester 4\Documents\Extra Documents (Trash)\Numberic data.csv")

#print(df[df['Price']%2==0]) <- For all even values
#print(df[df['Price']%2!=0]) <- For all odd values
print(df[df['Price']>25])