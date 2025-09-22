import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\study_performance.csv")
#--------------------------------
#   Personal Information
df['student_name']=""
df['student_id']=0
df.loc[0,"student_name"]="Muhammad Abdullah"
df.loc[0,"student_id"]=161
df_filtered = df[
    (df['student_name'].str.startswith('M')) &
    (df['gender'] == 'male')
]
df_filtered.to_csv('study_performance_Muhammad_Abdullah-161.csv', index=False)
#--------------------------------
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\study_performance.csv")
#   Basic exploration
print("First 10 Columns, Task: 1")
print(df.head(10))
#print(df.dtypes) <- can also be used
print("\n")

print("Column types, Task: 2")
print(df.info())
print("\n")

print("Count unique value, Task: 3")
epic= df[['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']].nunique()
print(epic)
print("\n")
#--------------------------------
#   Data cleaning
print("Checking and handling null values!, Task: 4")
print(df.isnull().sum())
abc=df.isnull().values.any()
print("Are there any null values in the DataFrame?",abc)
if abc==True:
    print(df.fillna(0))
print("\n")

print("Renaming comlumns!, Task: 5")
df.columns=df.columns.str.lower().str.replace(""," ")
print(df.columns)
print("\n")
#--------------------------------
#   Statistics
print("Average,min,max,std, Task: 6")
mathscore=df['math score']
print(" math scores avergae:",mathscore.mean(),"\n","math scores minimum:",mathscore.min(),"\n","math scores maximum:",mathscore.max(),"\n","math scores standard deviation:",mathscore.std())
print("\n")
readscore=df['reading score']
print(" reading scores avergae:",readscore.mean(),"\n","reading scores minimum:",readscore.min(),"\n","reading scores maximum:",readscore.max(),"\n","reading scores standard deviation:",readscore.std())
print("\n")
writescore=df['writing score']
print(" writing scores avergae:",writescore.mean(),"\n","writing scores minimum:",writescore.min(),"\n","writing scores maximum:",writescore.max(),"\n","writing scores standard deviation:",writescore.std())
print("\n")
#--------------------------------
#   Filtering and sorting
print("List students with score>90, Task: 7")
great= df[
    (df['math score'] > 90) &
    (df['reading score'] > 90) &
    (df['writing score'] > 90)
]
print(great)
print("\n")

print("Sort by writng score descending, Task: 8")
print(df.sort_values(by='writing score', ascending=False))
print("\n")
#--------------------------------
#   Groupping and aggregation
print(" Groupping by gender with mean scores, Task 9")
agg=df.groupby('gender').agg(Math_score=('math score','mean'),Reading_score=('reading score','mean'),Writing_score=('writing score','mean'))
print(agg)
print("\n")

print(" Groupping by test preparation course to count students, Task 10")
#agg=df.groupby('test preparation course').count() <- this can be also used
agg=df.groupby('test preparation course').size()
print(agg)
print("\n")
#----------------------------------
#   Transformation
print("Adding average scores, Task 11")
print("\n")
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
print(df[['student name', 'math score', 'reading score', 'writing score', 'average_score']].head(5))
print("\n")


print("Perfomance checkup, Task 12")
print("\n")
def p(x):
    if x < 50:
        return "Poor"
    elif 50 <= x < 70:
        return "Average"
    elif 70 <= x < 90:
        return "Good"
    else:
        return "Excellent"
df['performance_level'] = df['average_score'].apply(p)
print(df[['student name', 'average_score', 'performance_level']].head(5))
#----------------------------------