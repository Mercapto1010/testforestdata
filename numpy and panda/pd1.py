# Series
# A pandas series is like 1-D array like object that can hold any data type. It is similar to that of columns in table
import pandas as pd

data = [1,2,3,4,5]

series = pd.Series(data)              
# print(series)
# print(type(series))

# Creating a series by dictionary

data2 = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data2)
# print(series_dict)


data3 = [10,20,30]
index = ['a','b','c']
series = pd.Series(data3, index = index)
print(series)