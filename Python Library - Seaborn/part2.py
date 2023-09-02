import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("flights")
print(dataset)

sb.jointplot(x='month', y='passengers', data=database)
plt.show()

sb.catplot(x='month', y='passengers', data=database, kind='box')
plt.show()