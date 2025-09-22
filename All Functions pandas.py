import pandas as pd
df=pd.read_csv((r'file location here'))
print(df.head(2))

#1st lect
#print(df.dataframe())
#print(df.head())
#print(df.tail())
#print(df.columns)
#print(df.info())
#print(df.loc[2])
#print(df.loc[[0,1]])
#print(df.describe())
#print(df.mean())
#print(df.max())
#print(df[df['age']>25'])

#2nd lect
#print(calendar.month(yy,mm))
#print(df[['Name',"age",'salary']].head())
#print(df[df['Team']=='Boston'])
#print(df.query('age>25'))
#print(df['salary'].mean())
#print(f"{df['Salary'].mean():.2f}")
#print(f"(df['salary'].median():.2f)")
#print(f"(df['salary'].min():.2f)")
#print(f"(df['salary'].max():.2f)")
#print(f"(df['Age'].count():.2f)")
#print(f"(df['Salary'].count():.2f)")
#print(f"(df['Age'].std():.2f)")
#print(df['Age'].agg(['mean','medain','mode']).apply(lambda x:f"{x:2f}"))

#3rd lect
#team=df.groupby('team')
#print(team.first())
#------------------------------------------------
#team=df.groupby(['team'],['Position'])
#print(team.first())
#------------------------------------------------
#team=df.groupby(['team'],['Position'])
#print(team.last())
#------------------------------------------------
#team=df.groupby('Team')['salary'].mean()
#print(team)
#------------------------------------------------
#team=df.groupby('Team')['salary'].sum()
#print(team)
#------------------------------------------------
#team=df.groupby('Team')['salary'].medain()
#print(team)
#------------------------------------------------
#team=df.groupby('Team')['Age'].mean()
#print(team)
#------------------------------------------------
#team=df.groupby('Team')['Age'].count()
#print(team)
#------------------------------------------------
#agree_data=df.groupby(['Team','Position']).agg(total_salary=('Salary','sum'),avg_salary=('Salary','mean'),player_count=('name','count'))
#agree_data['avg_salary']=agree_data['avg_salary'].map('{:.2f}'.format)
#print(agree_data)
#------------------------------------------------
#agree_data=df.groupby(['Team','Position']).agg(total_salary=('Salary','sum'),avg_salary=('Salary','mean'),player_count=('name','count'))
#agree_data['avg_salary']=agree_data['avg_salary'].map('{:.2f}'.format)
#agree_data['total_salary']=agree_data['total_salary'].map('{:.2f}'.format)
#print(agree_data)
#df.to_csv('updatedata.csv',index=False)
#------------------------------------------------
#4th lecture
#c=avg=0
#for ele in df['marks']:
    #if str(ele).isnumeric():
        #c+=1
        #avg+=ele
#avg/=c
#df=df.repalce(to_replacewith='nan',value=avg)
#print(df)

#df['salary']=df['salary'].fillna(df['salary'].mean())
#print(df)        for integers

#df['college']=df['salary'].fillna(df['salary'])
#print(df)        

#print(df.dropna()) empty all dataframe
#df.rename(columns={'oldname':'newname'},inplace=True)
#print(df['salary'].mean())
#team=(df.groupby(['team','Position'])['salary'].mean())
#print(team)
#['avg_']
#df=df.set_index('avg_index',inplace=True)
#print(df)

#axis=1, inplace=True