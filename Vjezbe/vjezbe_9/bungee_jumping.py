import numpy as np


class Bungee_jumping:
    def __init__(self, l, h, gustoca_zraka, koeficijent_trenja, masa, konstanta_opruge, vrijeme_titranja, povrsina, dt):
        self.l = l
        self.h = h
        self.g = -9.81
        self.gustoca_zraka = gustoca_zraka
        self.koeficijent_trenja = koeficijent_trenja
        self.masa = masa
        self.konstanta_opruge = konstanta_opruge
        self.povrsina = povrsina
        self.vrijeme_titranja = vrijeme_titranja
        self.dt = dt
        self.lista_elongacija = []

        self.y = [h]
        self.v = [0]
        self.t = [0]

    def __y_akceleracija(self, brzina, elongacija):
        return self.g - ((np.sign(brzina) * self.koeficijent_trenja * self.povrsina * self.gustoca_zraka * (brzina)**2 / (2 * self.masa)) - (self.konstanta_opruge * elongacija / self.masa))

    def move(self):
        while self.t[-1] < self.vrijeme_titranja:
            elongacija = 0
            
            if self.y[-1] < self.h - self.l:
                elongacija = self.h - self.l - self.y[-1]
                self.lista_elongacija.append(elongacija)
            else:
                self.lista_elongacija.append(0)
            
            k_1_v = self.__y_akceleracija(self.v[-1], elongacija) * self.dt
            k_1_y = self.v[-1] * self.dt

            k_2_v = self.__y_akceleracija((self.v[-1] + k_1_v / 2), (elongacija + k_1_y / 2)) * self.dt
            k_2_y = (self.v[-1] + k_1_y / 2) * self.dt

            k_3_v = self.__y_akceleracija((self.v[-1] + k_2_v / 2), (elongacija + k_2_y / 2)) * self.dt
            k_3_y = (self.v[-1] + k_2_y / 2) * self.dt

            k_4_v = self.__y_akceleracija((self.v[-1] + k_3_v), (elongacija + k_3_y)) * self.dt
            k_4_y = (self.v[-1] + k_3_y) * self.dt

            self.v.append(self.v[-1] + (1 / 6) * (k_1_v + 2 * k_2_v + 2 * k_3_v + k_4_v))
            self.y.append(self.y[-1] + (1 / 6) * (k_1_y + 2 * k_2_y + 2 * k_3_y + k_4_y))

            self.t.append(self.t[-1] + self.dt)
            

    def energija(self):
        potecijalna = []
        kineticka = []
        elasticna = []
        ukupna = []
        del self.t[-1]

        for y, v, elongacija in zip(self.y, self.v, self.lista_elongacija):
            potecijalna.append(self.masa * abs(self.g) * y)
            kineticka.append((1/2) * self.masa * v**2)
            elasticna.append((1/2) * self.konstanta_opruge * elongacija**2)
            ukupna.append(self.masa * abs(self.g) * y + (1/2) * self.masa * v**2 + (1/2) * self.konstanta_opruge * elongacija**2)

        return potecijalna, kineticka, elasticna, ukupna