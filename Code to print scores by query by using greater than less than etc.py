import pandas as pd
df=pd.read_csv(r"C:\Users\Abdullah\Downloads\autos.csv\study_performance.csv")
#print(df.query('reading_score>70'))
#print(df.query('reading_score<50'))
print(df.query('reading_score>=99'))