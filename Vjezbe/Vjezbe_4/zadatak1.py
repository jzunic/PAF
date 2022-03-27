import calculus as calc
import matplotlib.pyplot as plt
import numpy as np


def analiticko(f, donja_granica, gornja_granica):
    lista_brojeva = np.linspace(donja_granica, gornja_granica, 100)
    lista_rezultata = []

    for broj in lista_brojeva:
        lista_rezultata.append(f(broj))

    return lista_brojeva, lista_rezultata

lista_x, lista_y = calc.derivacija2(lambda x: x**3, -5, 5)
lista_x1, lista_y1 = calc.derivacija2(lambda x: 50*np.sin(x),-5, 5)
lista_x2, lista_y2 = analiticko(lambda x: 3*x**2, -5, 5)
lista_x3, lista_y3 = analiticko(lambda x: 50 * np.cos(x), -5, 5)

plt.plot(lista_x, lista_y)
plt.plot(lista_x1, lista_y1)
plt.plot(lista_x2, lista_y2, ".")
plt.plot(lista_x3, lista_y3, "_")

plt.show()