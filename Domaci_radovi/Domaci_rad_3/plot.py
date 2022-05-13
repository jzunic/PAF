import matplotlib.pyplot as plt

datoteka = open("datoteka.txt", "r")
t=[]
v=[]
a=[]
x=[]
niz_nizova = []

for linija in datoteka:
    niz_nizova.append(linija.rstrip().split("|"))

for niz in niz_nizova:
    t.append(niz[0])
    a.append(niz[1])
    v.append(niz[2])
    x.append(niz[3])


t = list(map(float, t))
a = list(map(float, a))
v = list(map(float, v))
x = list(map(float, x))

plt.subplot(1, 3, 1)
plt.ylabel("x/m")
plt.xlabel("t/s")
plt.title("x-t graf")
plt.plot(t, x)

plt.subplot(1, 3, 2)
plt.ylabel("v/m/s")
plt.xlabel("t/s")
plt.title("v-t graf")
plt.plot(t, v)

plt.subplot(1, 3, 3)
plt.ylabel("a/m/s\u00B2")
plt.xlabel("t/s")
plt.title("a-t graf")
plt.plot(t, a)

plt.show()