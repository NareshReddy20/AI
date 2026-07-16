import pandas as pd
from openpyxl.workbook import Workbook
# df=pd.Series([1,2,3])
# print(df)

# #Creating Labels
# df=pd.Series([1,2,3],index=["x","y","z"])
# print(df)

data={
    "roll_no":[29,31,36],
    "name":["Naresh","Vishnu","Ranga"],
    "age":[20,21,22]
}
# print(data)
df=pd.DataFrame(data,index=["stu1","stu2","stu3"])
# print(df)

#----------Reading Files----------#

# to_csv=df.to_csv("students.csv",index="False")

# from_csv=pd.read_csv("students.csv")
# print(from_csv)

# to_excel=df.to_excel("students.xlsx")

# from_excel=pd.read_excel("students.xlsx")
# print(from_excel)

#----------Viewing Data----------#

churn_data=pd.read_csv('customer-churn.csv')
# print(churn_data.head())

# print(churn_data.tail())

# print(churn_data.columns)

# print(churn_data.shape)

# print(churn_data.info())

# print(churn_data.describe())

print(churn_data['gender'].isnull().sum())

print(churn_data['gender'].isnull().count())

print(churn_data['gender'].count())

# print(churn_data['gender'].isnull().sum())

#print(churn_data['gender'].sum())

print(churn_data['tenure'].sum())

print(churn_data['tenure'].count())

print(churn_data['tenure'].isnull())

# print(churn_data['tenure'].notnull())

#----------Selecting Data----------#

# print(churn_data['tenure'])

# print(churn_data[['tenure','gender','MonthlyCharges','TotalCharges']])

