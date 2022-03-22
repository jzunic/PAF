import numpy as np
import matplotlib.pyplot as plt
import math

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
        while self.y[-1] >= 0:
            self.__move()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]
        self.max_x = self.x[-1]
        domet = self.max_x
        return domet

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.show()

    def analiticko_rjesenje(self):
        analiticko_rjesenje = self.v_0 ** 2 * np.sin(2 * self.kut * np.pi / 180) / (-self.g)
        odstupanje = (abs(analiticko_rjesenje - self.max_x) / analiticko_rjesenje) * 100

        # if analiticko_rjesenje == max_x:
        #     print("Rjesenja su jednaka")
        # else:
        #     print("Rjesenja se razlikuju za {}%". format(odstupanje))
        
        return odstupanje

    def total_time(self):
        vrijeme_trajanja_gibanja = self.t[-1]
        #print("Vrijeme trajanja gibanja je: {}s".format(vrijeme_trajanja_gibanja))
        return(vrijeme_trajanja_gibanja)

    def max_speed(self):
        brzine = []

        for v1, v2 in zip(self.v_x, self.v_y):
            v = math.sqrt(v1**2 + v2**2)
            brzine.append(v)
        
        max_brzina = sorted(brzine, reverse=True)[0]
        print(max_brzina)
    """
    Gledam hoce li za zadanu brzinu ikad udaljenost od tocke na putanji do sredista mete biti manja od
    radijusa meta, to znaci da je meta pogodena. Krecem od brzine 0 jer za nju znam da meta nece biti
    pogodena, da sam odabrao nesto >0 postoji sansa da bi potrebna brzina mogla biti manja. Sada svaki
    put kad uvjet nije zadovoljen ponovno se poziva funkcija rekurzija koja brise sve iz lista i mijenja
    testnu brzinu za korak u kojem se nalazi petlja. (npr 0 -> 0 + 0.01*1 -> 0 + 0.01*2 -> ...).
    Kada se uvjet ispuni ispisuje se brzina u i-1 koraku jer je tada zapravo zadovoljen uvjet, ali je u 
    petlji postavljeno da se odmah na pocetku i poveca.
    """
    def velocity_to_hit_target(self, x_s_mete, y_s_mete, radijus_mete):
        def promjena(promjena):
            self.__init__(0.01) 
            promjena_testne_brzine = 0.1
            testna_brzina = 0 + (promjena_testne_brzine * promjena)
            self.set_initial_conditions(testna_brzina, self.kut, 0, 0)
            self.range()
            return testna_brzina

        i = 0
        promjena(i)
        pogodio = False

        while pogodio == False:
            i += 1
            #print(i)
            for x, y in zip(self.x, self.y):
                if ((x - x_s_mete)**2 + (y - y_s_mete)**2) <= radijus_mete**2:
                    pogodio = True
                else:
                    promjena(i)
            if pogodio == True:
                potrebna_brzina = promjena(i-1)
                print("Priblizna najmanja brzina potrebna da bi projektil pogodio metu je: {}m/s". format(potrebna_brzina))
        # figure, graf1 = plt.subplots()
        # kruznica = plt.Circle((x_s_mete, y_s_mete), radijus_mete, fill=False)
        # plt.gcf().gca().add_artist(kruznica)
        # graf1.set_aspect(1)
        # graf1.set_xlim([0, self.max_x + radijus_mete])
        # graf1.set_ylim([0, self.max_x + radijus_mete])
        # plt.plot(self.x, self.y)
        # plt.show()
    
    def angle_to_hit_target(self, x_s_mete, y_s_mete, radijus_mete):
        def promjena(promjena):
            self.__init__(0.01) 
            promjena_testnog_kuta = 0.1
            testni_kut = 0 + (promjena_testnog_kuta * promjena)
            self.set_initial_conditions(self.v_0, testni_kut, 0, 0)
            self.range()
            return testni_kut

        i = 0
        promjena(i)
        pogodio = False

        while pogodio == False:
            i += 1
            #print(i)
            for x, y in zip(self.x, self.y):
                if ((x - x_s_mete)**2 + (y - y_s_mete)**2) <= radijus_mete**2:
                    pogodio = True
                else:
                    promjena(i)
            if pogodio == True:
                potrebni_kut = promjena(i-1)
                print("Kut pod kojim se projektil treba izbaciti da bi pogodio metu zadanom brzinom je: {} stupnjeva". format(potrebni_kut))




# prt1 = Particle(0.01)
# prt1.set_initial_conditions(10, 60, 0, 0)
# prt1.range()
# prt1.total_time()
# prt1.max_speed()
# prt1.velocity_to_hit_target(2, 2, 1)
# prt1.angle_to_hit_target(2, 2, 1)