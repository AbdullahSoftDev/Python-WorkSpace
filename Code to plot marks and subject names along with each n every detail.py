import matplotlib.pyplot as plt
x=['Urdu','English','Pak Study','Computer','Math']
y=[40,90,57,93,64]
plt.bar(x,y,color="red",width=0.7)
plt.title("Marksheet Chart")
plt.xlabel('Subject names')
plt.ylabel('Marks obtaiend')
plt.legend(['Marks'])
plt.show()