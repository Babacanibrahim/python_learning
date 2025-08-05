import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,6)
y = np.arange(2,11,2)

"""
# plt.subplot(2,2,1)
# plt.plot(x,y,"red")

# plt.subplot(2,2,2)
# plt.plot(y,y**2,"black")

# plt.subplot(2,2,3)
# plt.plot(y,x,"yellow")

# plt.subplot(2,2,4)
# plt.plot(x,x**2,"blue")

# plt.show()
"""

# figure = plt.figure()

# axes1 = figure.add_axes([0.12,0.12,0.7,0.7])
# axes2 = figure.add_axes([0.2,0.5,0.2,0.2])

# axes1.plot(y,x)

# axes1.set_xlabel("X ekseni")
# axes1.set_ylabel("Y ekseni")
# axes1.set_title("Dış Graph")

# axes2.plot(x,y)
# axes2.set_xlabel("X ekseni")
# axes2.set_ylabel("Y ekseni")
# axes2.set_title("İç Graph")

"""
fig , axes = plt.subplots(nrows=2, ncols=1)

axes[0].plot(x,y)
axes[0].set_title("First Axes")
axes[1].plot(x,x**3)
axes[1].set_title("Second Axes")

plt.tight_layout()

fig.savefig("Figure1.png")
"""


# fig = plt.figure(figsize=(8,6))

# axes =fig.add_axes([0.1,0.1,0.9,0.9])

# axes.plot(x,y, "red",label = "X = Y", lw = 3)
# axes.plot(x,x**0.5, "green",label = "X = Y^2", lw = 3)
# axes.plot(x,x**3, "purple", label = "X = Y^0.5", lw = 3)

# axes.legend()

"""
fig = plt.figure(figsize=(8,6))

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y**1.3, "purple",lw = 3, marker = "o", markersize =13, markerfacecolor = "yellow",
          markeredgewidth = 5, markeredgecolor = "green")
"""


plt.show()