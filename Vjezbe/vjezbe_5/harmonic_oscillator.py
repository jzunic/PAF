import matplotlib.pyplot as plt
import math
import numpy as np

from numpy import dtype

class HarmonicOscillator():
    def __init__(self, x_0, dt, m, k, vrijeme_oscilacije):
        self.x = [x_0]
        self.v = [0]
        self.a = [-k/m * x_0]
        self.t = [0]
        self.m = m
        self.k = k
        self.vrijeme_oscilacije = vrijeme_oscilacije
        self.dt = dt
    
    def __move(self):
        self.a.append((-self.k/self.m) * self.x[-1])
        self.v.append(self.v[-1] + self.a[-1] * self.dt)
        self.x.append(self.x[-1] + self.v[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)
    
    def oscillate(self):
        while self.t[-1] <= self.vrijeme_oscilacije:
            self.__move()

    def plot(self):
        plt.subplot(1, 3, 1)
        plt.ylabel("x/m")
        plt.xlabel("t/s")
        plt.title("x-t graf")
        plt.plot(self.t, self.x)

        plt.subplot(1, 3, 2)
        plt.ylabel("v/m/s")
        plt.xlabel("t/s")
        plt.title("v-t graf")
        plt.plot(self.t, self.v)

        plt.subplot(1, 3, 3)
        plt.ylabel("a/m/s\u00B2")
        plt.xlabel("t/s")
        plt.title("a-t graf")
        plt.plot(self.t, self.a)

        plt.show()

    def numericki_period(self):
        period = 0

        for i in range(1, len(self.x)):
            if self.x[i] >= self.x[0]:
                break
            period += self.dt

        return period
    
    def analiticki_period(self):
        period = 2 * np.pi * math.sqrt(self.m / self.k)

        return period

#oscilator = HarmonicOscillator(10, 0.01, 10, 100, 3)
#oscilator.oscillate()
# oscilator.plot()
#oscilator.numericki_period()
#print(oscilator.numericki_period(), oscilator.analiticki_period())
