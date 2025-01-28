from numpy import *
arr1 = array([
    [1,2,3],[4,5,6]
])
arr2 = arr1.flatten()
# arr3 = arr2.reshape(4,3)
arr3 = arr2.reshape(2,2,3) # It will print a 3d array which has two 2-D arrays and this 2-D array has 2 1-D array and this 1-D array has 3 elements in it..🤯🤯
print(arr3)

# m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
# print(m.diagonal())

