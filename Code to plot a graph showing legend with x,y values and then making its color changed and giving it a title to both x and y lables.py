import matplotlib.pyplot as plt
plt.plot([2,4,6,8,9],[1,3,5,7,9],color="red")
plt.title("Line Chart")
plt.xlabel('x-Axis')
plt.ylabel('y-Axis',rotation='horizontal')
plt.legend(['bar'])
plt.show()