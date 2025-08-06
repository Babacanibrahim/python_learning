import numpy as np
import matplotlib.pyplot as plt

x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3


# Ödev 1
"""
fig = plt.figure()

axes = fig.add_axes([0.08,0.08,0.85,0.85])

axes.plot(x,y,"red")
"""

# Ödev 2
"""
fig = plt.figure(figsize=(8,6))

axes1 = fig.add_axes([0.05,0.1,0.8,0.8])
axes2 = fig.add_axes([0.15,0.5,0.4,0.3])

axes1.set_title("Outer Graph - X vs Z Graph")
axes2.set_title("Innter Graph - X vs Y Graph")

axes1.plot(x,z,"purple")
axes2.plot(x,y,"red")
"""

# Ödev 3

fig = plt.figure(figsize=(10,6))

splt1 = plt.subplot(1,2,1)
plt.plot(x,y,"red",marker = "o",markerfacecolor = "black")
splt1.set_xlabel("X values")
splt1.set_ylabel("Y values")
splt1.set_title("X-Y Graph")


splt2 = plt.subplot(1,2,2)
plt.plot(x,z,"purple",linestyle= "-.",lw =3)
splt2.set_xlabel("X values")
splt2.set_ylabel("Z values")
splt2.set_title("X-Z Graph")

plt.show()
