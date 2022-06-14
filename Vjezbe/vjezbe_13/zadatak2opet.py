from matplotlib import animation
import universe as un
import numpy as np
import matplotlib.pyplot as plt
au = 1.496e11

sunce = un.Planet("Sunce", 1.989e30, np.array((0, 0)), np.array((0, 0)), "yellow")
zemlja = un.Planet("Zemlja", 5.972e24, np.array((-1*au, 0)), np.array((0, -29783)), "blue")
merkur = un.Planet("Merkur", 3.3e24, np.array((0, 0.466*au)), np.array((-47362, 0)), "darkgray")
venera = un.Planet("Venera", 4.8685e24, np.array((0.723*au, 0)), np.array((0, 35020)), "orange")
mars = un.Planet("Mars", 6.417e23, np.array((0, -1.666*au)), np.array((24007, 0)), "red")
komet = un.Planet("komet", 10e14, np.array((6.34141937e11, 1.20679083e11)), np.array((-9155.32535412, 7512.39600861)), "black")

ss = un.Universe(365.242*3600*24, 50000)

ss.dodaj_planet(zemlja)
ss.dodaj_planet(sunce)
ss.dodaj_planet(merkur)
ss.dodaj_planet(venera)
ss.dodaj_planet(mars)
ss.dodaj_planet(komet)

ss.move()

x_lista, y_lista = [], []
tijela = [zemlja, sunce, merkur, venera, mars, komet]

for tijelo in tijela:
    temp_x, temp_y = [], []

    for polozaj in (tijelo.p):
        temp_x.append(polozaj[0])
        temp_y.append(polozaj[1])

    x_lista.append(temp_x)
    y_lista.append(temp_y)

fig = plt.figure()

l1, = plt.plot([], [], color=zemlja.boja)
p1, = plt.plot([], [], color=zemlja.boja, marker="o")
p2, = plt.plot([], [], color=sunce.boja, marker="o")
l3, = plt.plot([], [], color=merkur.boja)
p3, = plt.plot([], [], color=merkur.boja, marker="o")
l4, = plt.plot([], [], color=venera.boja)
p4, = plt.plot([], [], color=venera.boja, marker="o")
l5, = plt.plot([], [], color=mars.boja)
p5, = plt.plot([], [], color=mars.boja, marker="o")
l6, = plt.plot([], [], color=komet.boja)
p6, = plt.plot([], [], color=komet.boja, marker="o")

plt.xlim(-2*au, 2*au)
plt.ylim(-2*au, 2*au)

writer = animation.PillowWriter(fps=50)

with writer.saving(fig, "ss.gif", 100):
    for i in range(len(zemlja.p)):
        l1.set_data(x_lista[0][:i], y_lista[0][:i])
        l3.set_data(x_lista[2][:i], y_lista[2][:i])
        l4.set_data(x_lista[3][:i], y_lista[3][:i])
        l5.set_data(x_lista[4][:i], y_lista[4][:i])
        l6.set_data(x_lista[5][:i], y_lista[5][:i])

        p1.set_data(x_lista[0][i], y_lista[0][i])
        p2.set_data(x_lista[1][i], y_lista[1][i])
        p3.set_data(x_lista[2][i], y_lista[2][i])
        p4.set_data(x_lista[3][i], y_lista[3][i])
        p5.set_data(x_lista[4][i], y_lista[4][i])
        p6.set_data(x_lista[5][i], y_lista[5][i])

        writer.grab_frame()
plt.show()