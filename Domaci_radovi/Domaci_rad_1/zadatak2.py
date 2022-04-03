from numpy import linspace
import particle_dodatak as prt
import matplotlib.pyplot as plt

prt1 = prt.Particle(0.01)

kut = []
domet = []
vrijeme =[]

for i in linspace(0, 90, 1000):
    prt1.set_initial_conditions(10, i, 0, 0)
    kut.append(i)
    domet.append(prt1.range())
    vrijeme.append(prt1.total_time())

plt.subplot(1, 2, 1)
plt.xlabel("kut/stupnjevi")
plt.ylabel("domet/m")
plt.plot(kut, domet)

plt.subplot(1, 2, 2)
plt.plot(kut, vrijeme)
plt.xlabel("kut/stupnjevi")
plt.ylabel("vrijeme/s")

plt.show()