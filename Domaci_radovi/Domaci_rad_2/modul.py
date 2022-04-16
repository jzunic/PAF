import numpy as np
import matplotlib.pyplot as plt


class Motion:
    def __init__(self, x_0, dt, m, vrijeme_gibanja, v_0, t_0, F):
        self.x = [x_0]
        self.v = [v_0]
        self.a = [F(v_0, x_0, t_0) / m]
        self.t = [t_0]
        self.m = m
        self.dt = dt
        self.F = F
        self.vrijeme_gibanja = vrijeme_gibanja
    
    def __move(self):
        self.a.append(self.F(self.v[-1], self.x[-1], self.t[-1]) / self.m)
        self.v.append(self.v[-1] + self.a[-1] * self.dt)
        self.x.append(self.x[-1] + self.v[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)
    
    def motion(self):
        while self.t[-1] <= self.vrijeme_gibanja:
            self.__move()

    def plot(self):
        plt.plot(self.t, self.x)
        plt.show()

 

