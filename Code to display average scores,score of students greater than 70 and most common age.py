import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.figure(figsize=(20,15))
classs=['class1', 'class2', 'class3', 'class4', 'class5', 
          'class6', 'class7', 'class8', 'class9', 'class10']
math=np.random.randint(1, 100, size=(10))
english=np.random.randint(1, 100, size=(10))
urdu=np.random.randint(1, 100, size=(10))
SST=np.random.randint(1,100,size=(10))
physics=np.random.randint(1,100,size=(10))
df=pd.DataFrame({
    'Classes': classs,
    'English': english,
    'Math': math,
    'Urdu': urdu,
    'SST': SST,
    'Physics': physics
})
avg = df[["English", "Math", "Urdu", "SST", "Physics"]].mean()
plt.subplot(4, 1, 1)
avg.plot(kind='bar', color='pink',edgecolor='black')
plt.xticks(rotation=360)
plt.grid(axis='y',alpha=0.7)
plt.title('Average Scores by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks') 
#--------------------------------------------------------
subjects=["English", "Math", "Urdu", "SST", "Physics"]
high=(df[subjects]>=70).sum()
plt.subplot(4, 1, 2)
plt.bar(high.index,high.values,color='orange',edgecolor='black')
plt.title('Number of Students Scoring 70 or Above')
plt.xlabel('Subjects')
plt.ylabel('Number of Students')
plt.grid(axis='y',alpha=0.7)
#--------------------------------------------------------
top=high.idxmax()
ages=np.random.randint(15,35,size=10)
print("Subject with most scorers:",top)
age=pd.Series(ages).value_counts()
common=age.idxmax()
print('Most common age is: ',common)
plt.subplot(4, 1, 3)
plt.bar(age.index.astype(str),age.values,color='maroon',edgecolor='black')
plt.title("Most Common Age Among Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.grid()
plt.tight_layout()
plt.show()