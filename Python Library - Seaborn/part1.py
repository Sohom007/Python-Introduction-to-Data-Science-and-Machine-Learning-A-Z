import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("diamonds")
print(dataset)

sb.distplot(database["carat"])
plt.show()