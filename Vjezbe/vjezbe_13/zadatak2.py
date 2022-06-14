import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import universe as universe

au = 1.496e11

sunce = universe.Planet("Sunce", 1.989e30, np.array((4982872.393815673, 22211741.272785526)), np.array((-0.31487652, -1.40369414)), "yellow")
zemlja = universe.Planet("Zemlja", 5.972e24, np.array((-149579773210.89835, -1802974153.7505736)), np.array((-358.92127974, 29782.70172637)), "blue")
merkur = universe.Planet("Merkur", 3.3e24, np.array((-57981047672.46135, -74432098024.08752)), np.array((-24343.17209203, 25666.26546552)), "darkgray")
venera = universe.Planet("Venera", 4.8685e24, np.array((-71755952713.62416, -81633325598.07355)), np.array((-25847.17201456, 23370.61270456)), "orange")
mars = universe.Planet("Mars", 6.417e23, np.array((134127614014.43042, 257808932978.3384)), np.array((17839.03793578, -10327.86149883)), "red")
komet = universe.Planet("komet", 10e14, np.array((134127614020.43042, 257808932991.3384)), np.array((25000, 4300)), "black")

ss = universe.Universe(365.242*3600*24, 50000)

ss.dodaj_planet(zemlja)
ss.dodaj_planet(sunce)
ss.dodaj_planet(merkur)
ss.dodaj_planet(venera)
ss.dodaj_planet(mars)
ss.dodaj_planet(komet)

ss.move()

x_lista, y_lista = [], []

for tijelo in [zemlja, sunce, merkur, venera, mars, komet]:
    temp_x, temp_y = [], []

    for polozaj in (tijelo.p):
        temp_x.append(polozaj[0])
        temp_y.append(polozaj[1])

    x_lista.append(temp_x)
    y_lista.append(temp_y)

print(komet.p[-1])

# fig = plt.figure()

# l1, = plt.plot([], [], color=zemlja.boja)
# p1, = plt.plot([], [], color=zemlja.boja, marker="o")
# p2, = plt.plot([], [], color=sunce.boja, marker="o")
# l3, = plt.plot([], [], color=merkur.boja)
# p3, = plt.plot([], [], color=merkur.boja, marker="o")
# l4, = plt.plot([], [], color=venera.boja)
# p4, = plt.plot([], [], color=venera.boja, marker="o")
# l5, = plt.plot([], [], color=mars.boja)
# p5, = plt.plot([], [], color=mars.boja, marker="o")
# l6, = plt.plot([], [], color=komet.boja)
# p6, = plt.plot([], [], color=komet.boja, marker="o")

plt.xlim(-4*au, 4*au)
plt.ylim(-4*au, 4*au)

# writer = animation.PillowWriter(fps=50)

# with writer.saving(fig, "ss.gif", 100):
#     for i in range(len(zemlja.p)):
#         l1.set_data(x_lista[0][:i], y_lista[0][:i])
#         l3.set_data(x_lista[2][:i], y_lista[2][:i])
#         l4.set_data(x_lista[3][:i], y_lista[3][:i])
#         l5.set_data(x_lista[4][:i], y_lista[4][:i])
#         l6.set_data(x_lista[5][:i], y_lista[5][:i])

#         p1.set_data(x_lista[0][i], y_lista[0][i])
#         p2.set_data(x_lista[1][i], y_lista[1][i])
#         p3.set_data(x_lista[2][i], y_lista[2][i])
#         p4.set_data(x_lista[3][i], y_lista[3][i])
#         p5.set_data(x_lista[4][i], y_lista[4][i])
#         p6.set_data(x_lista[5][i], y_lista[5][i])

#         writer.grab_frame()

#plt.legend(loc="upper right")

# plt.plot(x_lista[1], y_lista[1], label=sunce.ime, color=sunce.boja, linewidth=5.0)

# plt.plot(x_lista[2], y_lista[2], label=merkur.ime, color=merkur.boja, linewidth=1.0)
# plt.plot(x_lista[2][-1], y_lista[2][-1], "o", color=merkur.boja)

# plt.plot(x_lista[3], y_lista[3], label=venera.ime, color=venera.boja, linewidth=1.0)
# plt.plot(x_lista[3][-1], y_lista[3][-1], "o", color=venera.boja)

# plt.plot(x_lista[0], y_lista[0], label=zemlja.ime, color=zemlja.boja, linewidth=1.0)
# plt.plot(x_lista[0][-1], y_lista[0][-1], "o", color=zemlja.boja)

# plt.plot(x_lista[4], y_lista[4], label=mars.ime, color=mars.boja, linewidth=1.0)
# plt.plot(x_lista[4][-1], y_lista[4][-1], "o", color=mars.boja)

# plt.plot(x_lista[5], y_lista[5], label=komet.ime, color=komet.boja, linewidth=1.0)
# plt.plot(x_lista[5][-1], y_lista[5][-1], "o", color=komet.boja)

# plt.legend(loc="upper right")
# plt.gca().set_aspect('equal')

# plt.show()