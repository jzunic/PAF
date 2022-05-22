import numpy as np
import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x_0, y_0, kut, v_0, gustoca_zraka, dt, masa, duljina, tijelo):
        if tijelo == "kocka":
            self.koeficijent_trenja = 1.05
        elif tijelo == "kugla":
            self.koeficijent_trenja = 0.47
        else:
            self.koeficijent_trenja = 0.47
        
        self.t = [0]
        self.g = -9.81
        self.masa = masa
        self.gustoca_zraka = gustoca_zraka
        self.duljina = duljina
        self.tijelo = tijelo
        self.x = [x_0]
        self.y = [y_0]
        self.v_y = [v_0 * np.sin(kut * np.pi / 180)]
        self.v_x = [v_0 * np.cos(kut * np.pi / 180)]
        self.a_y = [self.g - (self.v_y[0] * self.koeficijent_trenja * self.gustoca_zraka * (self.v_y[0])**2) / (2 * self.masa)]
        self.a_x = [(-self.v_x[0] * self.koeficijent_trenja * self.gustoca_zraka * (self.v_x[0])**2) / (2 * self.masa)]
        self.dt = dt

    def __povrsina_za_otpor(self, komponenta_brzine, brzina):
        povrsina = 0
        nepoznata_stranica = self.duljina / np.sin(np.arccos(komponenta_brzine / brzina))

        if self.tijelo == "kocka":
            povrsina = self.duljina * nepoznata_stranica
        elif self.tijelo == "kugla":
            povrsina = self.duljina**2 * np.pi
        else:
            povrsina = 1

        return povrsina
    
    def __x_akceleracija(self, brzina, povrsina):
        return (-np.sign(brzina) * self.koeficijent_trenja * self.gustoca_zraka * povrsina * (brzina)**2) / (2 * self.masa)

    def __y_akceleracija(self, brzina, povrsina):
        return self.g - (np.sign(brzina) * self.koeficijent_trenja * self.gustoca_zraka * povrsina * (brzina) / (2 * self.masa))

    def __move_runge_kutta(self):
        komponenta_brzine = self.v_y[-1]
        brzina = math.sqrt(self.v_y[-1]**2 + self.v_x[-1]**2)

        k_1_v_x = self.__x_akceleracija(self.v_x[-1], self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_2_v_x = self.__x_akceleracija((self.v_x[-1] + k_1_v_x / 2), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_3_v_x = self.__x_akceleracija((self.v_x[-1] + k_2_v_x / 2), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_4_v_x = self.__x_akceleracija((self.v_x[-1] + k_3_v_x), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt

        k_1_v_y = self.__y_akceleracija(self.v_y[-1], self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_2_v_y = self.__y_akceleracija((self.v_y[-1] + k_1_v_y / 2), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_3_v_y = self.__y_akceleracija((self.v_y[-1] + k_2_v_y / 2), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt
        k_4_v_y = self.__y_akceleracija((self.v_y[-1] + k_3_v_y), self.__povrsina_za_otpor(komponenta_brzine, brzina)) * self.dt

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

    def hitac_runge_kutta(self):
        while self.y[-1] >= 0:
            self.__move_runge_kutta()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]
    
    def angle_to_hit_target(self, x_s, y_s, radijus_mete):
        lista_udaljenosti_u_odnosu_na_kut = []
        udaljenosti = []
        kutovi = []
        potrebni_kut = 0
        pogodio = False

        for kut in range(0, 90, 1):
            self.__init__(0, 0, kut, 10, self.gustoca_zraka, self.dt, self.masa, self.duljina, "tocka")
            self.hitac_runge_kutta()

            udaljenosti = []

            for x, y in zip(self.x, self.y):
                udaljenost = math.sqrt((x - x_s)**2 + (y - y_s)**2) - radijus_mete
                udaljenosti.append(udaljenost)
                

            najmanja_udaljenost = sorted(udaljenosti)[0]
            lista_udaljenosti_u_odnosu_na_kut.append(
                {
                    "kut": kut,
                    "udaljenost":  najmanja_udaljenost
                }
            )
    
        for i in range(len(lista_udaljenosti_u_odnosu_na_kut)):
            if lista_udaljenosti_u_odnosu_na_kut[i]["udaljenost"] < 0:
                kutovi = np.linspace(lista_udaljenosti_u_odnosu_na_kut[i-1]["kut"], lista_udaljenosti_u_odnosu_na_kut[i]["kut"], 100)
                break
            else:
                najmanja_udaljenost = min(lista_udaljenosti_u_odnosu_na_kut, key=lambda x: x["udaljenost"])
                index = lista_udaljenosti_u_odnosu_na_kut.index(najmanja_udaljenost)

                kut = lista_udaljenosti_u_odnosu_na_kut[index]["kut"]
    
        for kut in kutovi:
            self.__init__(0, 0, kut, 10, self.gustoca_zraka, self.dt, self.masa, self.duljina, "tocka")
            self.hitac_runge_kutta()

            for x, y in zip(self.x, self.y):
                if ((x - x_s)**2 + (y - y_s)**2) <= radijus_mete**2:
                    pogodio = True
                    potrebni_kut = kut
            
            if pogodio:
                break
        
        if pogodio:
            print("Priblizni potrebni kut za pogoditi metu je {} stupnjeva". format(potrebni_kut))
            
            figure, graf1 = plt.subplots()
            kruznica = plt.Circle((x_s, y_s), radijus_mete, fill=False)
            plt.gcf().gca().add_artist(kruznica)
            graf1.set_aspect(1)
            graf1.set_xlim([0, self.x[-1] + radijus_mete])
            graf1.set_ylim([0, self.x[-1] + radijus_mete])
            plt.plot(self.x, self.y)
            plt.show()
        
        else:
            print("Meta ne moze biti pogodena")

            self.__init__(0, 0, kut, 10, self.gustoca_zraka, self.dt, self.masa, self.duljina, "tocka")
            self.hitac_runge_kutta()

            figure, graf1 = plt.subplots()
            kruznica = plt.Circle((x_s, y_s), radijus_mete, fill=False)
            plt.gcf().gca().add_artist(kruznica)
            graf1.set_aspect(1)
            graf1.set_ylim([0, y_s + radijus_mete])
            graf1.set_box_aspect(1)
            plt.plot(self.x, self.y)
            plt.show()
        