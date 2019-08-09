from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x, x2 = [5,8,10],[1,2,3]
y, y2 = [2,5,9],[4,5,6]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)

plt.title('Info')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True,color="b")

plt.show()