from matplotlib import pyplot as plt

x, x1 = [1,3,5,7,8], [2,4,6,8,10]
y, y1 = [5,2,7,8,8], [8,6,2,5,6]

plt.bar(x,y,color='r',label='Example one')
plt.bar(x1,y1,color='g',label='Example two')
plt.title('Bar Graph')
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.legend()

plt.show()