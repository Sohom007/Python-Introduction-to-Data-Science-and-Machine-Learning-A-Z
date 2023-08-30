# Joint Function

import pandas as pd

food1 = {'SlNo':[1,2,3,4,5], 'Menu':['Chicken Butter Masala','Chilli Paneer','Chicken Bharta','Mutton Biriyani','Mutton Cutlet'], 'Price':[450,250,220,280,150]}
food2 = {'Ratings':['4.7/5','4.2/5','4.3/5','4.5/5','4.1/5']}

menu1 = pd.DataFrame(food1)
menu2 = pd.DataFrame(food2)

menu = menu1.join(menu2)    # joints menu1 & menu2 
print(menu)