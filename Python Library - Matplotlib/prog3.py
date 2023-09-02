import matplotlib.pyplot as plt
from matplotlib import style  #importing style sub-package

style.use("bmh")   #uses bmh style while displaying the graphs

numbers=[0,2,5,12,17,18,20,21,25,28,30,31,32,33,34,35,38.39,42,48,52,53,55,59,60]
jumps=[0,5,10,15,20,25,30,35,40,45,50,55,60]

plt.title("Histogram")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.hist(numbers,jumps,histtype='bar')

plt.show()