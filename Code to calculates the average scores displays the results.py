import pandas as pd
df=pd.read_csv(r"C:/Users/Abdullah/.spyder-py3/Codes/Students.csv",low_memory=False)
print(df.head(5))
df['Average']=df[['Big data','DBMS','Data structures']].mean(axis=1)
print(df['Average'])