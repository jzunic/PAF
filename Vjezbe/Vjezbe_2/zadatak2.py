import numpy as np
import matplotlib.pyplot as plt

v_0 = 64
theta = 50
g = -9.81
t = np.linspace(0, 10, 100)
t_poc = 0
x_poc = 0
y_poc = 0
x_list = []
y_list = []
v_y_list = []
v_x_list = []
v_x = v_0 * np.cos(50 * np.pi / 180)
v_0_y = v_0 * np.sin(50 * np.pi / 180)
for el in t:
    v_y = v_0_y + g * (el - t_poc)
    y =  y_poc + v_y * (el - t_poc)
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