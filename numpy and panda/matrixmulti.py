from numpy import *
# Matrix Multiplication 
# m1 is of order 2x3
m1 = [[1, 2, 3],
      [4, 5, 6]]
# m2 is of order 3x2
m2 = [[7, 8],
      [9, 10],
      [11, 12]]
# result is of order 2x2
result = [[0, 0],
          [0, 0]]
print(m1)
print(m2)
# for rows of m1
for i in range(len(m1)):
    # for coulumns of m2
    for j in range(len(m2[0])):
        # for rows of m2
        for k in range(len(m2)):
            result[i][j] += m1[i][k] * m2[k][j]
for r in result:
    print(r)            