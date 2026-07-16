import pandas as pd
import pandas as pd
import numpy as np

# data = {
# 'School ID': [101, 102, 103, np.nan, 105, 106, 107, 108],
# 'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
# 'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm St', np.nan, '222 Maple Rd', '444 Cedar Blvd', '555 Birch Dr'],
# 'City': ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', np.nan, 'Pune', 'Jaipur'],
# 'Subject': ['Math', 'English', 'Science', 'Math', 'History', 'Math', 'Science', 'English'],
# 'Marks': [85, 92, 78, 89, np.nan, 95, 80, 88],
# 'Rank': [2, 1, 4, 3, 8, 1, 5, 3],
# 'Grade': ['B', 'A', 'C', 'B', 'D', 'A', 'C', 'B']
# }

# df = pd.DataFrame(data)
# print("Sample DataFrame:")
# print(df)

# print(df['Rank'].is_unique)
# print(df['Rank'].drop_duplicates(inplace=True))
# print(df['Rank'].replace(1,10))

# df_cleaned = df.dropna()
# print("\nDataFrame after removing rows with missing values:")
# print(df_cleaned)

# mean=df["Marks"].mean()
# mean_imputation=df["Marks"].fillna(mean)
# df['Marks']=mean_imputation
# print(df)

# forward_fill = df['Marks'].ffill()
# backward_fill = df['Marks'].bfill()

# print("\nForward Fill:")
# print(forward_fill)

# print("\nBackward Fill:")
# print(backward_fill)


data={
    "Department":["IT","IT","Non-IT","IT"],
    "Salary":[10,20,5,50]
}

df=pd.DataFrame(data)
print(df)

# print(df.groupby("Department")["Salary"].sum())
# new_df=df.sort_values("Salary")
# print(new_df)
# df=new_df.sort_index(ascending=False)
# print(df)

print(df["Department"].value_counts())

df1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["Naresh","Sai"]
})

df2 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[90,95]
})

result = pd.merge(df1, df2, on="ID")

# print(result)

# result["Marks"] = result["Marks"].apply(lambda x: x + 5)
# print(result)

print(result.set_index("Marks"))
print(result.reset_index)