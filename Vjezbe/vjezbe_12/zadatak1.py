import universe as un
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11

sunce = un.Planet("Sunce", 1.989e30, np.array((0, 0)), np.array((0, 0)), "yellow")
zemlja = un.Planet("Zemlja", 5.972e24, np.array((-1*au, 0)), np.array((0, -29783)), "blue")
merkur = un.Planet("Merkur", 3.3e24, np.array((0, 0.466*au)), np.array((-47362, 0)), "darkgray")
venera = un.Planet("Venera", 4.8685e24, np.array((0.723*au, 0)), np.array((0, 35020)), "orange")
mars = un.Planet("Mars", 6.417e23, np.array((0, -1.666*au)), np.array((24007, 0)), "red")

ss = un.Universe(5*365.242*3600*24, 3600)

ss.dodaj_planet(zemlja)
ss.dodaj_planet(sunce)
ss.dodaj_planet(merkur)
ss.dodaj_planet(venera)
ss.dodaj_planet(mars)

ss.move()

x_lista, y_lista = [], []

for tijelo in [zemlja, sunce, merkur, venera, mars]:
    temp_x, temp_y = [], []

    for polozaj in (tijelo.p):
        temp_x.append(polozaj[0])
        temp_y.append(polozaj[1])

    x_lista.append(temp_x)
    y_lista.append(temp_y)
    

plt.plot(x_lista[1], y_lista[1], label=sunce.ime, color=sunce.boja, linewidth=5.0)

plt.plot(x_lista[2], y_lista[2], label=merkur.ime, color=merkur.boja, linewidth=1.0)
plt.plot(x_lista[2][-1], y_lista[2][-1], "o", color=merkur.boja)

plt.plot(x_lista[3], y_lista[3], label=venera.ime, color=venera.boja, linewidth=1.0)
plt.plot(x_lista[3][-1], y_lista[3][-1], "o", color=venera.boja)

plt.plot(x_lista[0], y_lista[0], label=zemlja.ime, color=zemlja.boja, linewidth=1.0)
plt.plot(x_lista[0][-1], x_lista[1][-1], "o", color=zemlja.boja)

plt.plot(x_lista[4], y_lista[4], label=mars.ime, color=mars.boja, linewidth=1.0)
plt.plot(x_lista[4][-1], y_lista[4][-1], "o", color=mars.boja)

plt.legend(loc="upper right")
plt.gca().set_aspect('equal')
plt.show()