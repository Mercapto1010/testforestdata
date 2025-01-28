from numpy import *
# arr1 = array([1,2,3,4,5])

# arr2 = arr1.copy()

# print((arr1))
# print((arr2))
# print(id(arr1))
# print(id(arr2))

# arr2 = arr1.view()
# arr2 = arr1
# arr2 = array([6,7,8,9,10])
# arr3=arr1 + arr2
# print(arr3)
# arr += 5
# for i in range(len(arr)):
#     arr[i] +=5
# print(arr)

#Adding two numbers using for loop
# arr1 = array([1,2,3,4,5])
# arr2 = [6,7,8,9,10]
# arr3 = []
# for i in range(len(arr1)):
#     a = int(arr1[i]+arr2[i])
#     arr3.append(a)
# print(arr3)    

# find maximum number using for loop
arr1 = array([1,2,3,4,5])
max= arr1[0]
for i in range(len(arr1)):
    if arr1[i]>max:
        max = arr1[i]
print("maximum number:", max)
