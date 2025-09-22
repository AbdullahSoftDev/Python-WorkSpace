import pandas as pd
df=pd.read_csv(r"C:/Users/Abdullah/.spyder-py3/Codes/Students.csv",low_memory=False)
df['Average']=df[['Big data','DBMS','Data structures']].mean(axis=1)
print(df['Average'])
top=df['Average'].idxmax()
low=df['Average'].idxmin()
print('Maximum id is: ',top)
print('Minimum id is: ',low)
#df.rename(columns={'Unnamed: 0':'Index'},inplace=True)