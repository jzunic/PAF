import calculus as calc
import matplotlib.pyplot as plt
import numpy as np


def analiticko(f, donja_granica, gornja_granica):
    lista_brojeva = np.linspace(donja_granica, gornja_granica, 100)
    lista_rezultata = []

    for broj in lista_brojeva:
        lista_rezultata.append(f(broj))

    return lista_brojeva, lista_rezultata

def slika_derivacija():
    #Treba se zoomirat dosta na dio slike da bi se vidila odstupanja
    # lista_x, lista_y = calc.derivacija2(lambda x: x**3, -2, 2, 0.1)
    # lista_x1, lista_y1 = calc.derivacija2(lambda x: x**3, -2, 2, 0.01)
    lista_x1, lista_y1 = calc.derivacija2(lambda x: np.sin(x),-2, 2, 0.1)
    lista_x2, lista_y2 = calc.derivacija2(lambda x: np.sin(x),-2, 2, 0.01)
    # lista_x2, lista_y2 = analiticko(lambda x: 3*x**2, -2, 2,)
    lista_x3, lista_y3 = analiticko(lambda x: np.cos(x), -2, 2)

    # plt.scatter(lista_x, lista_y, s=5)
    plt.scatter(lista_x1, lista_y1, s=2, color="red")
    # plt.scatter(lista_x1, lista_y1, s=5)
    plt.scatter(lista_x2, lista_y2, s=5, color="green")
    plt.plot(lista_x3, lista_y3)
    plt.show()

podjele = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def slika_integrala():
    donje_sume = []
    gornje_sume = []

    for podjela in podjele:
        donja_suma, gornja_suma = calc.integral(lambda x: x**2, 1, 2, podjela)
        donje_sume.append(donja_suma)
        gornje_sume.append(gornja_suma)

    return donje_sume, gornje_sume

def slika_trapeznog_integrala():
    integrali = []

    for podjela in podjele:
        integral = calc.trapezni_integral(lambda x:x**2, 1, 2, podjela)
        integrali.append(integral)
    
    return integrali

donje_sume, gornje_sume = slika_integrala()
integrali = slika_trapeznog_integrala()
slika_derivacija()

plt.scatter(podjele, donje_sume, color="red", s=5)
plt.scatter(podjele, gornje_sume, color="green", s=5)
plt.scatter(podjele, integrali, color="black", s=5)
#analiticko rjesenje za x**2 na segmentu [1,2]
plt.plot(podjele, [7/3]*len(podjele))
plt.show()