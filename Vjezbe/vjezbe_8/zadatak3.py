import matplotlib.pyplot as plt
import numpy as np
import Projectile as pro

lista_masa = np.linspace(1, 10, 100)
lista_koeficijenata_trenja = np.linspace(0, 1, 100)
lista_dometa_masa = []
lista_dometa_koeficijent_trenja = []

for masa in lista_masa:
    pro1 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, masa, 1) #x_0, y_0, kut, v_0, gustoca_zraka, koeficijent_trenja, dt, masa, povrsina
    pro1.hitac_runge_kutta()
    lista_dometa_masa.append(pro1.domet())

for koeficijent_trenja in lista_koeficijenata_trenja:
    pro1 = pro.Projectile(0, 0, 60, 10, 1.225, koeficijent_trenja, 0.01, 10, 1)
    pro1.hitac_runge_kutta()
    lista_dometa_koeficijent_trenja.append(pro1.domet())

plt.subplot(1, 2, 1)
plt.plot(lista_masa, lista_dometa_masa)
plt.xlabel("m/kg")
plt.ylabel("domet/m")


plt.subplot(1, 2, 2)
plt.plot(lista_koeficijenata_trenja, lista_dometa_koeficijent_trenja)
plt.xlabel("Cd")
plt.ylabel("domet/m")

plt.show()



