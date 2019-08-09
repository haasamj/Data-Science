from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

days = [1,2,3]

sleeping = np.array([1,2,4])
eating = np.array([2,4,5])
working = np.array([2,5,9])
plt.subplot(211)
plt.plot([],[],color='r',label='sleeping')
plt.plot([],[],color='g',label='eating')
plt.plot([],[],color='b',label='working')

plt.stackplot(days,sleeping,eating,working,colors=['r','g','b'])

plt.subplot(212)
plt.plot(sleeping,'r')

# plt.title('Plot graph')
# plt.xlabel('xlabel')
# plt.ylabel('ylabel')
plt.grid(True,color='k')
plt.legend()
plt.show()