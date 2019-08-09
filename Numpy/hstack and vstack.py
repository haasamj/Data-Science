import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array ([4,5,6])

print(np.hstack((arr1,arr2)))

print(np.vstack((arr1,arr2)))

arr3 = np.array([[1,2,3],[-1,-2,-3]])
arr4 = np.array([[4,5,6],[-4,-5,-6]])

print(np.hstack((arr3,arr4)))

print(np.vstack((arr3,arr4)))