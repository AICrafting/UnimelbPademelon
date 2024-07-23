import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1, figsize=(10,6))
ax = fig.add_subplot(111)


X,Y = np.meshgrid(np.linspace(0,20,21), np.linspace(0,20,21))

U = 1
V = 1/5 * X * X

N = np.sqrt(U**2+V**2)
U2,V2 = U/N, V/N
ax.quiver(X, Y, U2, V2)

plt.xlim([0,20])
plt.ylim([0,20])
plt.hlines(0, 0, 20)
plt.vlines(0, 0, 20)
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.grid()
plt.title("Direction field plot for the system")
plt.show()
