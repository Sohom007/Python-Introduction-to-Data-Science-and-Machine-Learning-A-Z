import matplotlib.pyplot as plt
from matplotlib import style  #importing style sub-package

style.use("classic")   #uses bmh style while displaying the graphs

sales=[870,550,364,180]
cars=['Audi','Mercedes','Porche','Rolls Royce']
color=['pink','brown','yellow','blue']

plt.title("Pie Chart")

plt.pie(sales,labels=cars,colors=color)

plt.show()