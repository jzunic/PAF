import matplotlib.pyplot as plt
import Projectile as pro

pro1 = pro.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
pro2 = pro.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
pro3 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, 10, 1)
pro4 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, 10, 1)

pro1.hitac_runge_kutta()
pro2.hitac_euler()
pro3.hitac_runge_kutta()
pro4.hitac_euler()

plt.plot(pro1.x, pro1.y, c="red")
plt.scatter(pro2.x, pro2.y, c="blue", s=2.5)
plt.plot(pro3.x, pro3.y, c="green")
plt.scatter(pro4.x, pro4.y, c="purple", s=2.5)

plt.legend([
    "runge kutta, dt = 0.01, bez otpora zraka",
    "euler, dt = 0.01, bez otpora zraka",
    "runge kutta, dt = 0.01, s otporom zraka",
    "euler, dt = 0.01, s otporom zraka"
])

plt.show()