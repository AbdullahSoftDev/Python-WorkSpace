import pandas as pd
df = pd.read_csv(r"C:\Users\Abdullah\Downloads\nba.csv")
agg=df.groupby(['Team','Position']).agg(total_salary=('Salary','sum'),average=('Salary','mean'),age_count=('Age','count'))
agg['average']=agg['average'].map('{:.2f}'.format)
agg['total_salary']=agg['total_salary'].map('{:.2f}'.format)
print(agg)
df.to_csv('updatedata.csv',index=False)