import numpy as np
import matplotlib.pyplot as plt

# dv/dt = (vi++ - vi)/Dt = a => vi++ = vi + aDt

t = np.linspace(0, 10, 1000)

F = 10
m = 5
a = F/m
v = []
x = []
a_list = []
v_poc = 0
x_poc = 0
el_p = 0

for el in t:
    v_iduca = v_poc + a * (el - el_p)
    x_iduci = x_poc + v_iduca * (el - el_p)
    el_p = el
    v_poc = v_iduca
    x_poc = x_iduci
    v.append(v_iduca)
    x.append(x_iduci)
    a_list.append(a)
v = np.array(v)
x = np.array(x)

plt.subplot(2, 2, 1)
plt.title("v - t graf")
plt.xlabel("t/s")
plt.ylabel("v/m/s")
plt.plot(t, v)

plt.subplot(2, 2, 2)
plt.title("x - t graf")
plt.xlabel("t/s")
plt.ylabel("x/m")
plt.plot(t, x)

plt.subplot(2, 1, 2)
plt.title("a - t graf")
plt.xlabel("t/s")
plt.ylabel("a/m/s\u00B2")
plt.plot(t, a_list)

plt.show()
