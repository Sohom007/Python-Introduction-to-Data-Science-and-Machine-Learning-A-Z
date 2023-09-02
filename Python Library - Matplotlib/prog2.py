import matplotlib.pyplot as plt
from matplotlib import style  #importing style sub-package

style.use("bmh")   #uses bmh style while displaying the graphs

# bar-graph
x1=[50,60,70]
y1=[12,25,55]

x2=[80,40,10]
y2=[20,50,60]

x3=[-25,-45,-65]
y3=[-30,-50,-70]

plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)

plt.title("Bar Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()