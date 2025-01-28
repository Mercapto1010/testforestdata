from array import *

arr = array('i', [])
n = int(input("Enter the no. of values in array "))

for i in range(n):
    x = int(input("Enter next value "))
    arr.append(x)
print(arr)

val = int(input("Enter value to be searched"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1    

print(arr.index(val))   



