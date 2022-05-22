import Projectile as pro
import matplotlib.pyplot as plt

pro1 = pro.Projectile(0, 0, 60, 10, 1.225, 0.01, 10, 0.5, "kugla")
pro2 = pro.Projectile(0, 0, 60, 10, 1.225, 0.01, 10, 1, "kocka")

pro1.hitac_runge_kutta()
pro2.hitac_runge_kutta()

plt.plot(pro1.x, pro1.y, c="red")
plt.plot(pro2.x, pro2.y, c="blue")

plt.legend([
    "putanja kugle",
    "putanja kocke",
])

plt.show()