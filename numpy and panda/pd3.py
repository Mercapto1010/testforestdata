import pandas as pd

df = pd.read_csv('data.csv')
# print(df.head(5))
# print(df.tail(5))
# print(df.describe())
# print(df.dtypes)

# print(df.isnull()) #Handling missing values
# print(df.isnull().any(axis=1))
# print(df.isnull().sum())
# print(df.fillna(0))
df['UP_fillNA']= df['UnitPrice'].fillna(df['UnitPrice'].mean())
# print(df)
# print(df.dtypes)
# df = df.rename(columns={'StockCode':'SC'})    # RENAMING THE COLUMN
# print(df.head())

df['Quantity_new']= df['Quantity'].astype(float)
df['UP_new']= df['UP_fillNA'].astype(int)

df['NewQ']= df['Quantity'].apply(lambda x: x*2)
# print(df.head())

# Data Agrregating and grouping

grouped_mean = df.groupby('Country')['UP_fillNA'].mean()
# print(grouped_mean)

# grouped_sum = df.groupby(['InvoiceNo','Country'])['UP_fillNA'].sum()
grouped_sum = df.groupby(['InvoiceNo','Country'])['UP_fillNA'].mean()
# print(grouped_sum)


# aggregate multiple functions

grouped_agg = df.groupby('InvoiceNo')['UP_fillNA'].agg(['mean','sum','count'])
# print(grouped_agg)



#--------MERGING AND JOINING DATAFRAMES--------#

# CREATE SAMPLE DATAFRAMES
df1 = pd.DataFrame({'Key':['A','B','C'], 'Value1': [1,2,3]})
df2 = pd.DataFrame({'Key':['A','B','D'], 'Value2': [4,5,6]})
# print(df1)
# print(df2)
# mrg = pd.merge(df1,df2,on='Key',how='inner')
# mrg = pd.merge(df1,df2,on='Key',how='outer')
# mrg = pd.merge(df1,df2,on='Key',how='left')
# mrg = pd.merge(df1,df2,on='Key',how='right')
mrg = pd.merge(df1,df2,on='Key',how='cross')
print(mrg)
