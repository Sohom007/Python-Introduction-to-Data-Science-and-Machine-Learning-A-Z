#Merging two datasets

import pandas as pd

food1 = {'SlNo':[1,2,3,4,5], 'Menu':['Chicken Butter Masala','Chilli Paneer','Chicken Bharta','Mutton Biriyani','Mutton Cutlet'], 'Price':[450,250,220,280,150]}
food2 = {'SlNo':[1,2,3,4,5], 'Menu':['Chicken Butter Masala','Mutton Biriyani','Fish Finger','Mixed Fried Rice','Butter Nun'], 'Price':[450,320,120,260,50]}

menu1 = pd.DataFrame(food1)
menu2 = pd.DataFrame(food2)

menu = pd.merge(menu1,menu2,on="SlNo")    # merges menu1 & menu2 based on SlNo 
print(menu)