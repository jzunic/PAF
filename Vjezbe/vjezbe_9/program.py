import bungee_jumping as bngj
import matplotlib.pyplot as plt

bngj1 = bngj.Bungee_jumping(20, 100, 1.225, 0.47, 10, 100, 10, 1, 0.0001)
bngj2 = bngj.Bungee_jumping(20, 100, 1.225, 0.47, 10, 100, 10, 0, 0.0001)

bngj1.move()
bngj2.move()


plt.plot(bngj1.t, bngj1.y)
plt.ylabel("y/m")
plt.xlabel("t/s")
plt.title("y-t graf s otporom zraka")
plt.show()


plt.plot(bngj2.t, bngj2.y)
plt.ylabel("y/m")
plt.xlabel("t/s")
plt.title("y-t graf bez otpora zraka")
plt.show()

potencijalna1, kineticka1, elasticna1, ukupna1 = bngj1.energija()
potencijalna2, kineticka2, elasticna2, ukupna2 = bngj2.energija()


plt.plot(bngj1.t, potencijalna1)
plt.plot(bngj1.t, kineticka1)
plt.plot(bngj1.t, elasticna1)
plt.plot(bngj1.t, ukupna1)
plt.legend([
    "gravitacijska potencijalna energija",
    "kineticka energija",
    "elasticna potencijalna energija",
    "ukupna energija sustava",
])
plt.ylabel("E/J")
plt.xlabel("t/s")
plt.title("Bungee jumping s otporom zraka")
plt.show()


plt.plot(bngj1.t, potencijalna2)
plt.plot(bngj1.t, kineticka2)
plt.plot(bngj1.t, elasticna2)
plt.plot(bngj1.t, ukupna2)
plt.legend([
    "gravitacijska potencijalna energija",
    "kineticka energija",
    "elasticna potencijalna energija",
    "ukupna energija sustava",
])
plt.ylabel("E/J")
plt.xlabel("t/s")
plt.title("Bungee jumping bez otpora zraka")
plt.show()