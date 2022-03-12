import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, t):
    t = np.linspace(0, t, 1000)
    a = F/m
    v = []
    x = []
    a_list = []
    v_poc = 0
    x_poc = 0
    el_p = 0

    for el in t:
        v_iduca = v_poc + a * (el - el_p)
        x_iduci = x_poc + v_poc * (el - el_p) + 1/2 * a * (el - el_p)**2
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

def kosi_hitac(poc_brzina, upadni_kut, t):
    g = -9.81
    t = np.linspace(0, t, 100)
    t_poc = 0
    x_poc = 0
    y_poc = 0
    x_list = []
    y_list = []
    v_y_list = []
    v_x_list = []
    v_x = poc_brzina * np.cos(upadni_kut * np.pi / 180)
    v_0_y = poc_brzina * np.sin(upadni_kut * np.pi / 180)
    for el in t:
        v_y = v_0_y + g * (el - t_poc)
        y =  y_poc + v_0_y * (el - t_poc) + 1/2 * g * (el - t_poc)**2
        x = x_poc + v_x * (el - t_poc)
        
        v_0_y = v_y
        t_poc = el
        x_poc = x
        y_poc = y
        
        v_y_list.append(v_y)
        v_x_list.append(v_x)
        y_list.append(y)
        x_list.append(x)

    v_y_list = np.array(v_y_list)
    v_x_list = np.array(v_x_list)   
    x_list = np.array(x_list)
    y_list = np.array(y_list)

    plt.subplot(2, 2, 1)
    plt.ylabel("vx/m/s")
    plt.xlabel("t/s")
    plt.title("vx - t graf")
    plt.plot(t,v_x_list)

    plt.subplot(2, 2, 2)
    plt.ylabel("vy/m/s")
    plt.xlabel("t/s")
    plt.title("vy - t graf")
    plt.plot(t, v_y_list)

    plt.subplot(2, 1, 2)
    plt.title("y - x graf")
    plt.xlabel("x/m")
    plt.ylabel("y/m")
    plt.plot(x_list, y_list)
    plt.show()
