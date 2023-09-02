import matplotlib.pyplot as plt
from matplotlib import style  #importing style sub-package

style.use("classic")   #uses bmh style while displaying the graphs

x=[12,25,28,42,48,55,59,25,18]
y=[12,25,28,42,48,55,59,25,18]

plt.title("Scatter Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.scatter(x,y)

plt.show()