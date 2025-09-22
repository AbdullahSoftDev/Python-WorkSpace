import matplotlib.pyplot as plt
x=['Urdu','English','Pak Study','Computer','Math']
y=[40,90,57,93,64]
plt.plot(x,y,color="red")
plt.title("Line Chart")
plt.xlabel('x-Axis')
plt.ylabel('y-Axis',rotation='horizontal')
plt.legend(['bar'])
plt.show()

plt.bar(x,y,color="red")
plt.title("Line Chart")
plt.xlabel('x-Axis')
plt.ylabel('y-Axis',rotation='horizontal')
plt.legend(['bar'])
plt.show()