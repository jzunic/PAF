import numpy as np
import matplotlib.pyplot as plt
import universe as universe

au = 1.496e11

sunce = universe.Planet("Sunce", 1.989e30, np.array((0, 0)), np.array((0, 0)), "yellow")
zemlja = universe.Planet("Zemlja", 5.972e24, np.array((-1*au, 0)), np.array((0, -29783)), "blue")
merkur = universe.Planet("Merkur", 3.3e24, np.array((0, 0.466*au)), np.array((-47362, 0)), "darkgray")
venera = universe.Planet("Venera", 4.8685e24, np.array((0.723*au, 0)), np.array((0, 35020)), "orange")
mars = universe.Planet("Mars", 6.417e23, np.array((0, -1.666*au)), np.array((24007, 0)), "red")
komet = universe.Planet("komet", 10e14, np.array((5*au, -au)), np.array((np.cos(np.pi/3)*16000), np.sin(np.pi/3)*16000), "black")

ss = universe.Universe(8.3*365.242*3600*24, 3600)

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
    

plt.plot(x_lista[1], y_lista[1], label=sunce.ime, color=sunce.boja, linewidth=5.0)

plt.plot(x_lista[2], y_lista[2], label=merkur.ime, color=merkur.boja, linewidth=1.0)
plt.plot(x_lista[2][-1], y_lista[2][-1], "o", color=merkur.boja)

plt.plot(x_lista[3], y_lista[3], label=venera.ime, color=venera.boja, linewidth=1.0)
plt.plot(x_lista[3][-1], y_lista[3][-1], "o", color=venera.boja)

plt.plot(x_lista[0], y_lista[0], label=zemlja.ime, color=zemlja.boja, linewidth=1.0)
plt.plot(x_lista[0][-1], y_lista[0][-1], "o", color=zemlja.boja)

plt.plot(x_lista[4], y_lista[4], label=mars.ime, color=mars.boja, linewidth=1.0)
plt.plot(x_lista[4][-1], y_lista[4][-1], "o", color=mars.boja)

plt.plot(x_lista[5], y_lista[5], label=komet.ime, color=komet.boja, linewidth=1.0)
plt.plot(x_lista[5][-1], y_lista[5][-1], "o", color=komet.boja)

plt.legend(loc="upper right")
plt.gca().set_aspect('equal')
plt.show()