# Dataframe
# Create a dataframe from dictionary of list
import pandas as pd
data = {
    'Name': ['Abdul', 'Patrick', 'Abeer'],
    'Age' : [20,30,40],
    'City' : ['Delhi', 'Gurugram', 'Noida']
}
df = pd.DataFrame(data)
# print(type(df['Name']))
# print(df['Name'])
# print(df.loc[0])
# print(df.iloc[0,2])    #Accessing elements from dataframe
# print(df) 
#  Accessing a specified element

# print(df.at[1,'Age'])
# print(df.iat[2,2])

#  Data Manipulation with Dataframe
df['Salary']= [50000,2000000,7500000]   #Adding a column

df.drop('Salary',axis=1,inplace=True)   #Removing a column
# print(df)


# Adding age to column
# df['Age'] = df['Age']+1
# print(df)
# Create a data frame from a list of dictionary

# data = [
#     {'Name': 'Abdul', 'Age': 25,'City' : 'Delhi'},
#     {'Name': 'Krish', 'Age': 28,'City' : 'Gurgaon'},
#     {'Name': 'Raj', 'Age': 27,'City' : 'Noida'},
#     {'Name': 'Varun', 'Age': 26,'City' : 'Ghaziabad'}
# ]
# df = pd.DataFrame(data)
# print(df)
# print(type(df))

# df = pd.read_csv('data.csv')
# print(df.head(5))
# print(df.tail(5))