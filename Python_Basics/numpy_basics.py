# ============================================================
# NUMPY BASICS & IMPORTANT METHODS
# ============================================================

# Topics Covered in this File:
#
# 1. Array Creation
#    - np.array()
#
# 2. Array Dimensions
#    - ndim
#    - 0D, 1D, 2D, 3D arrays
#
# 3. Array Indexing
#    - Positive indexing
#    - Negative indexing
#
# 4. Array Slicing
#    - start:end
#    - step slicing
#    - negative slicing
#
# 5. Array Properties
#    - dtype
#    - shape
#    - size
#
# 6. Copy vs View
#    - copy()
#    - view()
#
# 7. Array Reshaping
#    - reshape()
#    - flattening using reshape(-1)
#
# 8. Iterating Arrays
#    - for loop iteration
#
# 9. Joining Arrays
#    - concatenate()
#    - axis=0
#    - axis=1
#
# 10. Special Array Functions
#     - arange()
#     - linspace()
#
# 11. Splitting Arrays
#     - array_split()
#
# 12. Filtering Arrays
#     - Boolean Masking
#     - Conditional Filtering
#     - Multiple Conditions (&)


import numpy as np

#Creating Arrays

# arr=np.array([10,20,5,15])
# print(arr)
# print(type(arr))

# arr=np.array((10,20,5,15))
# print(arr)

# arr=np.array({10,20,5,15})
# print(arr)

#Dimensions

# arr = np.array([10, 20, 30])
# print(arr.ndim) 

# arr = np.array(42)
# print(arr.ndim) 

# arr=np.array([[10,20],[30,40]])
# print(arr)
# print(arr.ndim) 

# arr=np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# print(arr)
# print(arr.ndim) 


# Array Indexing
# print("Access 2d Array Elements : ",arr[0][1])
# print("Access 2d Array Elements : ",arr[-1][-1])

# Array Slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-4:0])
# print(arr[1:5])
# print(arr[4:])
# print(arr[:4])

# print(arr[-6:4])
# print(arr[:])
# print(arr[-5:])
# print(arr[::2])

# print(arr.dtype)

#Copy vs View

# x=arr.copy()
# x[0]=60
# print(x)
# print(arr)

# y=arr.view()
# y[0]=50
# print(y)
# print(arr)

# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)

# a=arr.reshape(4,2)
# print(a)

#Flattening Array
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# newarr=arr.reshape(-1)
# print(newarr)

#Iterating
# for x in newarr:
#     print(x)


# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# res=np.concatenate((arr1,arr2))
# print(res)

a=np.array([[1,2],[3,4]])
b=np.array([[6,7],[8,9]])
res1=np.concatenate((a,b),axis=1)
res1=np.hstack((a,b))
print(res1)

# arr=np.arange(-12,12,2)
# print(arr)

# arr1=np.linspace(0,12,100)
# print(arr1)

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)

# arr=np.array([10,20,15,17,14])
# new_array=arr[(arr>15)&(arr<20)]
# print(new_array)

# arr=np.ones((2,3))
# print(arr)

# arr=np.zeros((1,2))
# print(arr)

# arr=np.eye(3)
# print(arr)

# arr2 = np.diag([1, 2, 3])
# print(arr2)

# arr=np.array([1,2,3,4,5,6,7,10])
# res=np.where(arr%2==0)
# print(res)


# arr=np.array([3,5,7,9])
# x=np.searchsorted(arr,7)
# print(x)

# y=np.searchsorted(arr,7,side='right')
# print(y)

# z=np.searchsorted(arr,[4,6,8])
# print(z)


x=np.random.rand()
print(x)

x=np.random.randint(10)
print(x)

x=np.random.randint(5,size=(3,4))
print(x)

x=np.random.rand(2,4)
print(x)

x=np.random.choice([4,5,6])
print(x)