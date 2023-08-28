import numpy as np

var = np.array([(2,5,7),(3,4,8)])
var1 = var.reshape(3,2)   #rechapes the array in 3-row 2-column format
print(var)
print('Dimension of the array: ', var.ndim)   #prints dimension of an array
print("Size of the array: ", var.size)   #prints size of the array
print("Shape of the array in (row,column) format: ", var.shape)   #print the shape of the array in (row,column) format
print(var1)
