#TASK 2: The Comparison dashboard
import matplotlib.pyplot as plt
print("TASK 2")
plt.subplot(1,2,1)
plt.bar(['Electronics','Clothing','Home'],[300,450,200])
plt.title("Bar Chart")
plt.show()
plt.subplot(1,2,2)
plt.plot([1,2,3,4,5],[2000,4500,4000,7500,9000])
plt.title("Line Plot")
plt.show()