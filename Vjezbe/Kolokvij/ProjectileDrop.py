import matplotlib.pyplot as plt
import numpy as np

class ProjectileDrop:
    def __init__(self, h, v_x, dt, x_0=0):
        self.h = h
        self.horizontalna_brzina = v_x
        self.g = -9.81
        self.dt = dt
        self.a = []
        self.x = [x_0]
        self.y = [h]
        self.v_x = [v_x]
        self.v_y = [0]
        self.t = [0]
        
        #print("Objekt je uspjesno stvoren\npocetna visina: {}m\nhorizontalna brzina: {}m/s\n".format(self.h, self.horizontalna_brzina))

    def Promjena_visine(self, nova_visina):
        self.h = nova_visina
        print(self.h)
    
    def Promjena_brzine(self, brzina):
        self.v_x[-1] += brzina
        #print(self.v_x[-1])

    def projektil(self, promjena_horizontalne_brzine=0):
        while self.y[-1] >= 0:
            self.Promjena_brzine(promjena_horizontalne_brzine)
            self.a.append(self.g)
            self.v_x.append(self.v_x[-1])
            self.v_y.append(self.v_y[-1] + self.a[-1]*self.dt)
            self.x.append(self.x[-1] + self.v_x[-1]*self.dt)
            self.y.append(self.y[-1] + self.v_y[-1]*self.dt)
            self.t.append(self.t[-1] + self.dt)

    def plot(self):
        plt.subplot(1, 2, 1)
        plt.title("x-y graf")
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.plot(self.x, self.y)

        plt.subplot(1, 2, 2)
        plt.title("v_y-t graf")
        plt.xlabel("t/s")
        plt.ylabel("v_y/m/s")
        plt.plot(self.t, self.v_y)

        plt.show()

    def numericko_vrijeme_padanja(self, dt):
        numericko_vrijeme = []
        
        self.__init__(self.h, self.horizontalna_brzina, dt)
        self.projektil()

        numericko_vrijeme.append(self.t[-1])

        return numericko_vrijeme

    def meta(self, x_s, radijus_mete, brzina_vjetra=0):
        t_lista = list(range(0, 101))
        vrijeme_izbacaja = int()

        for t in t_lista:
            self.x[0] += self.horizontalna_brzina
            pogodio = False
            self.__init__(self.h, self.horizontalna_brzina, self.dt, self.x[0])
            self.projektil(brzina_vjetra)

            if self.x[-1] >= abs(x_s - radijus_mete) and self.x[-1] <= x_s + radijus_mete:
                vrijeme_izbacaja = t
                pogodio = True
                break
        
        if pogodio:
            print("vrijeme izbacaja je: {}s".format(vrijeme_izbacaja))
            figure, graf1 = plt.subplots()
            kruznica = plt.Circle((x_s, 0), radijus_mete, fill=False)
            plt.gcf().gca().add_artist(kruznica)
            graf1.set_aspect(1)

            plt.plot(self.x, self.y)
            plt.show()
        else:
            print("Meta ispustena iz aviona koji se giba tom horizontalnom brzinom, na koju takoder djeluje vjetar konstantnom silom,  ne moze biti pogodena")



            


        


