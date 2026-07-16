import pandas as pd
data={
    "m1":[90,57,78],
    "m2":[76,89,45],
    "m3":[100,95,34]
}
df=pd.DataFrame(data)
# df.columns=['java','python','c']
# df.index=['naresh','vishnu','ranga']
# print(df)

#----------loc and iloc----------#

# print(df.loc['naresh':'ranga'])

# print(df.iloc[0:3])

# print(df.loc['naresh','c'])

# print(df.iloc[0,2])

#----------Filtering----------#

# print(df[df["m3"]>80])

# print(df)
# print(df[((df["m3"]>90) & (df["m3"]<100)) | ((df['m1']>85) & (df['m1']<100))])

#----------Adding New Column----------#

# df['m4']=df['m1']+5
# print(df)

# df['m5']=[78,69,91]
# print(df)

#----------Updating Values----------#

# df['m3']=94
# print(df)

# df.loc[0,'m3']=100
# print(df)

# df.iloc[1,2]=95
# print(df)


#----------Aggregations----------#
# print(df["m1"].sum())
# print(df["m1"].mean())
# print(df["m1"].min())
# print(df["m1"].max())

