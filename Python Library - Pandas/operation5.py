# Converting csv file to html file

import pandas as pd

stock = pd.read_csv('D:\Data Science and ML (Udemy)\Python Library - Pandas\\Book1.csv')
stock.to_html('Stocks')