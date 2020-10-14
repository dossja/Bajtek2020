import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

plt.plot(x, y, color="red")
plt.plot(x, z,color="pink")

plt.title("Test plot")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(["this is y", "this is z"])

plt.grid()

plt.savefig("wykres.png")

plt.show()