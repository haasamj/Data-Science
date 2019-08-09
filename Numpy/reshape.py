import numpy as np

arr1 = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])

# print(arr1)
# print(arr1.ndim)
#
# arr1 = arr1.reshape(2,2,4) # 4 rows, 2 cols and 2 elements in each row
#
# print(arr1)
# print(arr1.ndim)
arr1 = arr1.flat[0:]
print(arr1)
print(arr1.ndim)
arr1 = arr1.reshape(1,16)
print(arr1)
print(arr1.ndim)
