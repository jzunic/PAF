import numpy as np

def derivacija(f, x, korak, metoda = "three-step"):
    rez = 0
    
    if metoda == "two-step":
        rez = (f(x + korak) - f(x))/(korak)
    else:
        rez = (f(x + korak) - f(x - korak))/(2 * korak)
    
    return rez

def derivacija2(f, donja_granica, gornja_granica):
    lista_brojeva = np.linspace(donja_granica, gornja_granica, 100)
    lista_derivacija = []
    
    for broj in lista_brojeva:
        lista_derivacija.append(derivacija(f, broj, 0.001))
    
    return lista_brojeva, lista_derivacija
#derivacija2(lambda x: x**2, 1, 2)
