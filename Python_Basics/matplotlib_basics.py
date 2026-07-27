import matplotlib.pyplot as plt
import pandas as pd

# days = [1,2,3,4,5]
# sales = [100,120,150,170,200]
# plt.plot(days,sales)
# plt.title("Days VS Sales")
# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.show()

# days=["Mon","Tue","Wed","Thu","Fri"]
# temperature=[38,40,35,44,29]
# plt.plot(days,temperature)
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.show()

age=[20,22,25,28,30]
salary=[15000,40000,90000,200000,300000]
plt.scatter(age,salary)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Relationship between Age and Salary")
plt.grid(True)
plt.show()

# departments = ["IT","HR","Sales"]
# employees = [50,30,40]

# plt.bar(departments, employees)
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Employees by Department")
# plt.show()


# # Example data
# ages = [5, 7, 8, 9, 10, 12, 13, 15, 15, 16, 17, 18, 20, 21, 22]
# # Histogram
# plt.hist(ages, bins=[0, 5, 10, 15, 20, 25], edgecolor='black')
# # Labels and title
# plt.title("Age Distribution")
# plt.xlabel("Age Groups")
# plt.ylabel("Frequency")
# # Show graph
# plt.show()


# labels=["DEV","HR","AI/ML","Data science","Deveops"]
# sizes=[40,78,62,38,18]
# plt.pie(sizes,labels=labels)
# # plt.figure(figsize=(20,10))
# plt.show()


days = [1,2,3,4]

sales1 = [100,120,140,160]
sales2 = [90,110,130,150]

plt.plot(days, sales1, label="Store A")
plt.plot(days, sales2, label="Store B")

plt.legend()
plt.savefig("multiplelines.png")
plt.savefig("multiplelines.jpg")
plt.show()