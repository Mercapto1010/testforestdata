import numpy as np
# ARRAY SLICING AND INDEXING

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Array: \n", arr)
# print(arr[0][3])    # in matrix indexing starts from 0
# print(arr[1:, 2:])     # [rows:, columns:]
# print(arr[0:2, 1:3])
# print(arr[1:, 1:3])

# MODIFY ELEMENTS
# arr[0,0]= 69
arr[1:,1:3]= 69
print(arr)