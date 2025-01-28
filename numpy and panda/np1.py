import numpy as np

arr1 = np.array([1,5,3,4,6])
arr1= arr1.reshape(1,5)
# print(arr1)
# print(type(arr1))
arr1 = np.array([[1,5,3,4,6], [2,8,7,9,10]])
# print(arr1)
# print(arr1.shape)

a = np.arange(0,10,2)
# print(a.reshape(5,1))

# b = np.ones((3,3))
b = np.eye(3)   #Identity matrix
print(b)