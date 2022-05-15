import numpy as np

class Projectile:
    def __init__(self, x_0, y_0, kut, v_0, gustoca_zraka, koeficijent_trenja, dt, masa, povrsina):
        self.t = [0]
        self.g = -9.81
        self.masa = masa
        self.gustoca_zraka = gustoca_zraka
        self.koeficijent_trenja = koeficijent_trenja
        self.povrsina = povrsina
        self.x = [x_0]
        self.y = [y_0]
        self.v_y = [v_0 * np.sin(kut * np.pi / 180)]
        self.v_x = [v_0 * np.cos(kut * np.pi / 180)]
        self.a_y = [self.g - (self.v_y[0] * self.koeficijent_trenja * self.gustoca_zraka * (self.v_y[0])**2) / (2 * self.masa)]
        self.a_x = [(-self.v_x[0] * self.koeficijent_trenja * self.gustoca_zraka * (self.v_x[0])**2) / (2 * self.masa)]
        self.dt = dt
    
    def __move(self):
        self.v_x.append(self.v_x[-1] + self.a_x[-1] * self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1] * self.dt)
        self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
        self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
        self.a_x.append((-np.sign(self.v_x[-1]) * self.koeficijent_trenja * self.gustoca_zraka * (self.v_x[-1])**2) / (2 * self.masa))
        self.a_y.append(self.g - (np.sign(self.v_y[-1]) * self.koeficijent_trenja * self.gustoca_zraka * (self.v_y[-1])**2) / (2 * self.masa))
        self.t.append(self.t[-1] + self.dt)

    def __x_akceleracija(self, brzina):
        return (-np.sign(brzina) * self.koeficijent_trenja * self.gustoca_zraka * (brzina)**2) / (2 * self.masa)

    def __y_akceleracija(self, brzina):
        return self.g - (np.sign(brzina) * self.koeficijent_trenja * self.gustoca_zraka * (brzina) / (2 * self.masa))

    def __move_runge_kutta(self):
        k_1_v_x = self.__x_akceleracija(self.v_x[-1]) * self.dt
        k_2_v_x = self.__x_akceleracija((self.v_x[-1] + k_1_v_x / 2)) * self.dt
        k_3_v_x = self.__x_akceleracija((self.v_x[-1] + k_2_v_x / 2)) * self.dt
        k_4_v_x = self.__x_akceleracija((self.v_x[-1] + k_3_v_x)) * self.dt

        k_1_v_y = self.__y_akceleracija(self.v_y[-1]) * self.dt
        k_2_v_y = self.__y_akceleracija((self.v_y[-1] + k_1_v_y / 2)) * self.dt
        k_3_v_y = self.__y_akceleracija((self.v_y[-1] + k_2_v_y / 2)) * self.dt
        k_4_v_y = self.__y_akceleracija((self.v_y[-1] + k_3_v_y)) * self.dt

        self.v_x.append(self.v_x[-1] + 1 / 6 * (k_1_v_x + 2 * k_2_v_x + 2 * k_3_v_x + k_4_v_x))
        self.v_y.append(self.v_y[-1] + 1 / 6 * (k_1_v_y + 2 * k_2_v_y + 2 * k_3_v_y + k_4_v_y))

        k_1_x = self.v_x[-1] * self.dt
        k_2_x = (self.v_x[-1] + k_1_x / 2) * self.dt
        k_3_x = (self.v_x[-1] + k_2_x / 2) * self.dt
        k_4_x = (self.v_x[-1] + k_3_x) * self.dt

        k_1_y = self.v_y[-1] * self.dt
        k_2_y = (self.v_y[-1] + k_1_y / 2) * self.dt
        k_3_y = (self.v_y[-1] + k_2_y / 2) * self.dt
        k_4_y = (self.v_y[-1] + k_3_y) * self.dt

        self.x.append(self.x[-1] + 1 / 6 * (k_1_x + 2 * k_2_x + 2 * k_3_x + k_4_x))
        self.y.append(self.y[-1] + 1 / 6 * (k_1_y + 2 * k_2_y + 2 * k_3_y + k_4_y))


        self.t.append(self.t[-1] + self.dt)

    
    def hitac_euler(self):
        while self.y[-1] >= 0:
            self.__move()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]

    def hitac_runge_kutta(self):
        while self.y[-1] >= 0:
            self.__move_runge_kutta()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]

    def domet(self):
        return sorted(self.x)[-1]
        