import ProjectileDrop as pd
import numpy as np
import matplotlib.pyplot as plt

t_lista = np.linspace(0.001, 0.1, 100)
numericko_vrijeme = []

for t in t_lista:
    pd1 = pd.ProjectileDrop(2000, 200, t)
    numericko_vrijeme.append(pd1.numericko_vrijeme_padanja(t))

plt.scatter(t_lista, numericko_vrijeme, s=3, color="red")
plt.title("Ovisnost numerickog vremena padanja projektila o odabiru intervala dt")
plt.xlabel("dt/s")
plt.ylabel("numericko vrijeme padanja/s")

plt.show()