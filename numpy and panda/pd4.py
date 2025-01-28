import pandas as pd
from io import StringIO
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
df=pd.read_json(StringIO(Data))
# dd=df.to_json()
# dd=df.to_json(orient="index")
dd=df.to_json(orient='records')
dd=df.to_json(orient='columns')
dd=df.to_json(orient='table')
# print(dd)
# print(dd)

de = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None)
# print(de.head())

dg = de.to_csv('wine.csv')
# print(dg)

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
da = pd.read_html(url)
# print(da[0])

url1 = "https://en.wikipedia.org/wiki/Mobile_country_code"
db = pd.read_html(url1,match="Country",header=0)[0]
# print(db)

dg = pd.read_excel('boom.xlsx')
# print(dg)

dg.to_pickle('dg')
dp = pd.read_pickle('dg')
print(dp)



