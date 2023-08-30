import pandas as pd

#Printing data in table format

Dataset1 = {'SlNo':[1,2,3,4,5], 'Employee Name':['Sujay','Ayan','Bimal','Rik','Souvik'], 'Salary per month':['30 thousand','35 thousand','50 thousand','25 thousand','32 thousand']}

table1 = pd.DataFrame(Dataset1)

print(table1)