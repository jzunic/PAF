import matplotlib.pyplot as plt
import Projectile as pro

pro1 = pro.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
pro2 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.1, 10, 1)
pro3 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.2, 10, 1)
pro4 = pro.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, 10, 1)

pro1.hitac_euler()
pro2.hitac_euler()
pro3.hitac_euler()
pro4.hitac_euler()

plt.plot(pro1.x, pro1.y, c="red")
plt.plot(pro2.x, pro2.y, c="blue")
plt.plot(pro3.x, pro3.y, c="purple")
plt.plot(pro4.x, pro4.y, c="green")

plt.legend([
    "dt = 0.01, bez otpora zraka",
    "dt = 0.1",
    "dt = 0.2",
    "dt = 0.01"
])

print(pro1.x[-1], pro2.x[-1], pro3.x[-1], pro4.x[-1])
print(pro3.x, pro3.y)

plt.show()