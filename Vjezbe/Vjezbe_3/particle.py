import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, dt):
        self.t = []
        self.x = []
        self.y = []
        self.v_y = []
        self.v_x = []
        self.a_y = []
        self.a_x = []
        self.dt = dt
        self.g = -9.81

    def set_initial_conditions(self, v_0, kut, x_0, y_0):
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.v_y.append(v_0 * np.sin(kut * np.pi / 180))
        self.v_x.append(v_0 * np.cos(kut * np.pi / 180))
        self.a_y.append(self.g)
        self.a_x.append(0)

        self.kut = kut
        self.v_0 = v_0

    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.v_x.append(self.v_x[-1] + self.a_x[-1] * self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1] * self.dt)
        self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
        self.y.append(self.y[-1] + self.v_y[-1] * self.dt)

    def range(self):
        while self.y[-1] >= 0 and self.dt != 0:
            self.__move()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]
        max_x = self.x[-1]
        return max_x

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.show()

    def analiticko_rjesenje(self, max_x):
        analiticko_rjesenje = self.v_0 ** 2 * np.sin(2 * self.kut * np.pi / 180) / (-self.g)
        odstupanje = (abs(analiticko_rjesenje - max_x) / analiticko_rjesenje) * 100

        # if analiticko_rjesenje == max_x:
        #     print("Rjesenja su jednaka")
        # else:
        #     print("Rjesenja se razlikuju za {}%". format(odstupanje))
        
        return odstupanje