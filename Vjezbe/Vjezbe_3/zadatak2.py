import particle as prt
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.01, 0.1, 200)

x = []
y = []

for dt in t:
    prt1 = prt.Particle(dt)
    prt1.set_initial_conditions(10, 60, 0, 0)
    x.append(dt)
    y.append(prt1.analiticko_rjesenje(prt1.range()))

plt.plot(x, y)
plt.xlabel("dt/s")
plt.ylabel("err/%")
plt.show()