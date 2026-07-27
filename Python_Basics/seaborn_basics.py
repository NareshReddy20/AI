import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# a=[10,11,12,10,45,47,48]
# sns.histplot(a,bins=[0,10,20,30,40,50,60],color='red',kde=True)
# plt.show()


# data={
#     "Age":[20,23,25,28,30],
#     "Salary":[15000,40000,80000,100000,200000]
# }
# df=pd.DataFrame(data)
# # print(df)

# sns.scatterplot(data=df,x="Age",y="Salary")
# plt.show()

# marks = [10,15, 40, 42, 45, 50, 52, 55, 58, 60, 62,
#          65, 68, 70, 72, 75, 78, 80, 85, 90, 95,150]
# sns.boxplot(marks,vert="False")
# plt.title("Student Marks Boxplot")
# plt.show()

# import matplotlib.pyplot as plt

# marks = [35, 40, 45, 50, 55, 60, 60, 60,
#          65, 70, 75, 80, 85, 90]

# # Violin plot
# sns.violinplot(marks)

# plt.title("Violin Plot Example")

# plt.show()




# students = ["CSE", "ECE", "CSE", "EEE", "ECE",
#             "CSE", "MECH", "EEE", "CSE"]

# # Count plot
# sns.countplot(x=students)

# # Title
# plt.title("Student Branch Count")

# plt.show()


data = pd.DataFrame({
    "Math": [80, 85, 90, 70, 60],
    "Science": [75, 80, 95, 65, 70],
    "English": [78, 82, 88, 60, 72]
})

# Pair plot
sns.pairplot(data)
plt.show()


#HeatMap
# Sample student dataset
# data = {
#     "Math": [80, 85, 90, 70, 60],
#     "Science": [75, 82, 95, 65, 70],
#     "English": [78, 80, 88, 60, 72],
#     "Computer": [90, 92, 98, 75, 85]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Correlation matrix
# corr = df.corr(numeric_only=True)

# # Heatmap
# sns.heatmap(
#     corr,
#     annot=True,
#     cmap="coolwarm"
# )

# plt.title("Student Marks Correlation Heatmap")

# plt.show()


# df=pd.DataFrame({"Marks":[10,12,15,17,20,22,24,26,28,30,35,40]})
# sns.kdeplot(df)
# plt.show()

# sns.histplot(data=df,x=df["Marks"],kde=True)
# plt.show()

# df=pd.DataFrame({
#     "sales":[12,24,20,17],
#     "month":["Aug","Sep","Oct","Nov"]
# })
# sns.lineplot(data=df,x=df["sales"],y=df["month"])
# plt.show()