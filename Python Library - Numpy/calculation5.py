import numpy as np

var1 =  np.array([(5,4,3),(5,8,7)])
print("Array: ")
print(var1)
print("All values in single row: ", var1.ravel())   #prints all the array elements in single row
print("Sum of each columns: ", var1.sum(axis=0))   
print("Sum of each rows: ", var1.sum(axis=1))   
print("Square root of all the numbers: ", np.sqrt(var1))
print("Standard Deviation of all the numbers: ", np.std(var1))