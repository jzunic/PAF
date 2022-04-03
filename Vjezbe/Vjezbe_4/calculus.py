import numpy as np

def derivacija(f, x, korak, metoda = "three-step"):
    rez = 0
    
    if metoda == "two-step":
        rez = (f(x + korak) - f(x))/(korak)
    else:
        rez = (f(x + korak) - f(x - korak))/(2 * korak)
    
    return rez

def derivacija2(f, donja_granica, gornja_granica, korak):
    lista_brojeva = np.linspace(donja_granica, gornja_granica, 100)
    lista_derivacija = []
    
    for broj in lista_brojeva:
        lista_derivacija.append(derivacija(f, broj, korak))
    
    return lista_brojeva, lista_derivacija

def integral(f, donja_granica, gornja_granica, broj_podjela):
    dx = (gornja_granica - donja_granica)/broj_podjela
    x_lista = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)
    donja_suma = 0
    gornja_suma = 0

    for i in range(len(x_lista) - 1):
        donja_suma += f(x_lista[i]) * dx
        gornja_suma += f(x_lista[i+1]) * dx

    return donja_suma, gornja_suma

def trapezni_integral(f, donja_granica, gornja_granica, broj_podjela):
    dx = (gornja_granica - donja_granica)/broj_podjela
    x_lista = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)
    integral = 0

    for i in range(len(x_lista) - 1):
        integral += dx*(f(x_lista[i]) + (f(x_lista[i+1]) - f(x_lista[i])) / 2)

    return integral


