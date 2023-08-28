import numpy as np

var = np.linspace(10,100,5)   #store 5 numbers at equal distance between 10 to 100 in var
print(var)

#Slice function
var1 = np.array([(2,5,4,6),(4,8,7,3),(2,5,4,8)])
print(var1[0:,1])   #prints all the values in second position of each array from array no. 1
print()
print("Array: ")
print(var1)
print("Max: ", var1.max())
print("Min: ", var1.min())
print("Sum: ", var1.sum())