import numpy as np
import matplotlib.pyplot as plt
import particle as prt

prt1 = prt.Particle(-1, 1, np.array((0, 0, 1)), np.array((0, 0, 0)), np.array((0.1, 0.1, 0.1)), np.array((0, 0, 0)), 20, 0.001)
prt2 = prt.Particle(1, 1, np.array((0, 0, 1)), np.array((0, 0, 0)), np.array((0.1, 0.1, 0.1)), np.array((0, 0, 0)), 20, 0.001)
prt1.move()
prt2.move()

x_1, y_1, z_1 = prt1.info_for_plot()
x_2, y_2, z_2 = prt2.info_for_plot()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_1, y_1, z_1)
ax.plot3D(x_2, y_2, z_2)

plt.show()