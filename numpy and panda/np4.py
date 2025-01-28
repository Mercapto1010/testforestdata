import numpy as np
# statistical concepts------> Normalization
# to have a mean of 0  and standard deviation of 1 
# data = np.array([1,2,3,4,5])

# #  Calculate Mean and Standard Deviation
# mean = np.mean(data)
# std_dev = np.std(data)

# # Normalize the data
# normalized_data = (data-mean)/std_dev
# print("Normalized Data:\n", normalized_data)

# ------------------------------------------------------------------
data = np.array([1,2,3,4,5,6,7,8,9,10])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Standard_Deviation
Standard_Deviation = np.std(data)

# Variance
variance = np.var(data)

print("MEAN: ",mean)
print("MEDIAN: ",median)
print("Standard Deviation: ",Standard_Deviation)
print("Variance: ",variance)
