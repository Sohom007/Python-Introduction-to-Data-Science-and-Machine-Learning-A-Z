#Linear Regression Model

import numpy as np
import matplotlib.pyplot as plt

height = np.array([140,141,144,148,150,152,153,155,156,157,157,159,160])
weight = np.array([40,45,55,50,52,55,54,60,65,70,72,75,78])
fun1 = np.polyfit(height,weight,1)

plt.plot(height,weight,'.')
plt.plot(height, np.polyval(fun1,height),'r-')
plt.show()