import numpy as np

class Particle:
    def __init__(self, q, m, B, E, v_0, polozaj, vrijeme_gibanja, dt):
        self.q = q
        self.m = m
        self.B = B
        self.E = E
        self.vrijeme_gibanja = vrijeme_gibanja
        self.dt = dt
        self.v = [v_0]
        self.polozaj = [polozaj]
        self.a = [(self.q / self.m) * (self.E + np.cross(self.v[-1], self.B))]
        self.t = [0]

    def move(self):
        while self.t[-1] <= self.vrijeme_gibanja:
            self.v.append(self.v[-1] + self.a[-1] * self.dt)
            self.polozaj.append(self.polozaj[-1] + self.v[-1] * self.dt)
            self.a.append((self.q / self.m) * (self.E + np.cross(self.v[-1], self.B)))

            self.t.append(self.t[-1] + self.dt)

    def __acc_runge_kutta(self, v):
        return (self.q / self.m) * (self.E + np.cross(v, self.B))


    def runge_kutta(self):
        while self.t[-1] <= self.vrijeme_gibanja:
            k_1_v = self.__acc_runge_kutta(self.v[-1]) * self.dt
            k_1_polozaj = self.v[-1] * self.dt

            k_2_v = self.__acc_runge_kutta((self.v[-1] + k_1_v / 2)) * self.dt
            k_2_polozaj = (self.v[-1] + k_1_polozaj / 2) * self.dt

            k_3_v = self.__acc_runge_kutta((self.v[-1] + k_2_v / 2)) * self.dt
            k_3_polozaj = (self.v[-1] + k_2_polozaj / 2) * self.dt

            k_4_v = self.__acc_runge_kutta((self.v[-1] + k_3_v)) * self.dt
            k_4_polozaj = (self.v[-1] + k_3_polozaj) * self.dt

            self.v.append(self.v[-1] + (1 / 6) * (k_1_v + 2 * k_2_v + 2 * k_3_v + k_4_v))
            self.polozaj.append(self.polozaj[-1] + (1 / 6) * (k_1_polozaj + 2 * k_2_polozaj + 2 * k_3_polozaj + k_4_polozaj))

            self.t.append(self.t[-1] + self.dt)

    def info_for_plot(self):
        x= []
        y = []
        z = []

        for polozaj in self.polozaj:
            x.append(polozaj[0])
            y.append(polozaj[1])
            z.append(polozaj[2])

        return x, y, z
