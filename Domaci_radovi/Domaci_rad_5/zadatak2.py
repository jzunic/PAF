import matplotlib.pyplot as plt
import numpy as np
import Particle as prt

prt1 = prt.Particle(
    -1,
    1,
    lambda t: np.array((0, 0, t)),
    lambda t: np.array((0, 0, 0)),
    np.array((0.1, 0.1, 0.1)),
    np.array((0, 0, 0)),
    10,
    0.01
)

prt2 = prt.Particle(
    1,
    1,
    lambda t: np.array((0, 0, t)),
    lambda t: np.array((0, 0, 0)),
    np.array((0.1, 0.1, 0.1)),
    np.array((0, 0, 0)),
    10,
    0.01
)

prt1.runge_kutta()
x_1, y_1, z_1 = prt1.info_for_plot()

prt2.runge_kutta()
x_2, y_2, z_2 = prt2.info_for_plot()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_1, y_1, z_1)
ax.plot3D(x_2, y_2, z_2)

plt.legend([
    "elektron, B(t)=(0, 0, t/10), E(t)=(0, 0, 0)",
    "pozitron, B(t)=(0, 0, t/10), E(t)=(0, 0, 0)",
])

plt.show()