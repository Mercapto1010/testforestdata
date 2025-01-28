# x = lambda a: a*a
# result = x(7)
# print(result)

from functools import reduce
num = [2,4,6,3,9,7]
evens = list(filter(lambda n: n%2==0, num))
print(evens)

double = list(map(lambda n: n*2, num))
print(double)

total = reduce(lambda a,b: a+b,num)
print(total)