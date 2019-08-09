from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y,color="k",label="skitscat")

plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()