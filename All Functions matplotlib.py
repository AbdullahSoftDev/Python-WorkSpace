#import mathplot.pyplot as plt
#x=[22,33,44,55,66]
#plt.plot(x)
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#x=[2,4,6,8,9]
#y=[1,3,5,7,9]
#plt.plot(x,y)
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.plot([2,4,6,8,9],[1,3,5,7,9],color="r")
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.plot([2,4,6,8,9],[1,3,5,7,9],color="r")
#plt.title("Line Chart")
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.plot([2,4,6,8,9],[1,3,5,7,9],color="r")
#plt.title("Line Chart")
#plt.xlabel("X-axix")
#plt.ylabel("y-axix")
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.plot([2,4,6,8,9],[1,3,5,7,9],color="r")
#plt.title("Line Chart")
#plt.xlabel("X-axix")
#plt.ylabel("y-axix")
#plt.legend("Line")
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.bar([2,4,6,8,9],[1,3,5,7,9],color="r")
#plt.title("Line Chart")
#plt.xlabel("X-axix")
#plt.ylabel("y-axix")
#plt.legend("Line")
#plt.show()
#------------------------
#import mathplotlib.pyplot as plt
#plt.bar([2,4,6,8,9],[1,3,5,7,9],color="r",width=0.5)
#plt.title("Line Chart")
#plt.xlabel("X-axis")
#plt.ylabel("y-axis")
#plt.legend("Line")
#plt.show()
#------------------------
#import matplotlib.pyplot as plt
#x = ['Urdu', 'English','Science','Math']
#y = [1,2,3,4]
#plt.bar(x,y,color="pink",width=0.5)
#plt.title("Marks Chart")
#plt.xlabel("Subject Name")
#plt.ylabel("Marks")
#plt.legend(["info"])
#plt.show()
#------------------------
#import numpy as np
#import pandas as pd
#import mathplot.pyplot as plt
#student=np.arange(1001,1011)
#print(student)
#------------------------
#import numpy as np
#import pandas as pd
#import mathplot.pyplot as plt
#student=np.arange(1001,1011)
#big_data=np.random.randint(65,95,10)
#print(student,big_data)
#------------------------
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#np.random.seed(1)
#student=np.arange(1001,1011)
#big_data=np.random.randint(65,95,10)
#data_structure=np.random.randint(50,85,10)
#dbms=np.random.randint(70,99,10)
#print(student,big_data)
#------------------------
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#np.random.seed(1)
#student=np.arange(1001,1011)
#big_data=np.random.randint(65,95,10)
#data_structure=np.random.randint(50,85,10)
#dbms=np.random.randint(70,99,10)
#data=(
#     'StudentID:':student,
#      'Big Data:':big_data,
#      'DATABASE:':data_structure,
#      'DBMS:':dbms,
#      )
#df=pd.dataframe(data)
#print(df)
#------------------------
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#np.random.seed(1)
#student=np.arange(1001,1011)
#big_data=np.random.randint(65,95,10)
#data_structure=np.random.randint(50,85,10)
#dbms=np.random.randint(70,99,10)
#data=(
#     'StudentID:':student,
#      'Big Data:':big_data,
#      'DATABASE:':data_structure,
#      'DBMS:':dbms,
#      )
#df=pd.dataframe(data)
#print(df)
#df.to_csv('updatedstudentdata.csv',index=False)
#------------------------
#import pandas as pd
#df=pd.read_csv(r'filename.csv')
#print(df.head(5))
#df['average']=df[['dbms','big_data','data_structure']].mean(axix=1)
#print(df['average'])
#------------------------
#import pandas as pd
#df=pd.read_csv(r'filename.csv')
#print(df.head(5))
#df['average']=df[['dbms','big_data','data_structure']].mean(axix=1)
#top_score=df['average'].idxmax()
#print(top_score)
#------------------------
#import pandas as pd
#df=pd.read_csv(r'filename.csv')
#print(df.head(5))
#df['average']=df[['dbms','big_data','data_structure']].mean(axix=1)
#top_score=df['average'].idxmax()
#low_score=df['average'].idxmin()
#print(df['average'],top_score,low_average)
#------------------------
#import pandas as pd
#df=pd.read_csv(r'filename.csv')
#df['average']=df[['dbms','big_data','data_structure']].mean(axix=1)
#top_score=df.loc[df['average'].idxmax()]
#print(top_score.map('{:.1f}'.format)
#------------------------
#import matplotlib.pyplot as plt
#plt.bar(df['studentID'].astype(str),df['average'],color='purple')
#plt.xlabel('All students')
#plt.ylabel('Total average')
#plt.legend(['bar chart'])
#plt.title('BAR CHARt')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()
#------------------------
