import Projectile as pro
import matplotlib.pyplot as plt

pro1 = pro.Projectile(0, 0, 60, 10, 1.225, 0.01, 10, 1, "kugla")
pro2 = pro.Projectile(0, 0, 60, 10, 1.225, 0.01, 10, 1, "tocka")

pro2.angle_to_hit_target(3, 4, 1)
pro2.angle_to_hit_target(10, 5, 3)
pro2.angle_to_hit_target(2, 2, 0.5)

