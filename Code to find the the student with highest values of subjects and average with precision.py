import pandas as pd
df=pd.read_csv(r"C:/Users/Abdullah/.spyder-py3/Codes/Students.csv",low_memory=False)
df['Average']=df[['Big data','DBMS','Data structures']].mean(axis=1)
df.rename(columns={'Unnamed: 0':'Index'},inplace=True)
print(df['Average'])
top_score=df.loc[df['Average'].idxmax()]
print(top_score.map('{:.1f}'.format))
#df.rename(columns={'Unnamed: 0':'Index'},inplace=True)