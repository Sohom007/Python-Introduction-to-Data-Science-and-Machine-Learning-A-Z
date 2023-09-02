import matplotlib.pyplot as plt
from matplotlib import style  #importing style sub-package

style.use("bmh")   #uses bmh style while displaying the graphs

#first graph
plt.plot([5,40,45,80],[70,30,28,50])   
plt.show()

#second graph
x1=[50,60,70]
y1=[12,25,55]

x2=[80,40,10]
y2=[20,50,60]

plt.plot(x1,y1)
plt.plot(x2,y2)

plt.title("Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()