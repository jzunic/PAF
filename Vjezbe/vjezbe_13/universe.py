import numpy as np

class Planet:
    def __init__(self, ime, masa, polozaj, brzina, boja):
        self.ime = ime
        self.boja = boja
        self.m = masa
        self.p = [polozaj]
        self.a = []
        self.v = [brzina]

class Universe:
    def __init__(self, vrijeme_gibanja, dt):
        self.vrijeme_gibanja = -vrijeme_gibanja
        self.dt = dt
        self.G = 6.67408 * 10**(-11)
        self.svemir = []
        self.t = [0]

    def dodaj_planet(self, planet):
        self.svemir.append(planet)

    def __akceleracija(self, tijelo1, lista_tijela):
        akceleracija = np.array((0., 0.))

        for tijelo in lista_tijela:
            if np.linalg.norm(tijelo1.p[-1] - tijelo.p[-1]) == 0:

                print("0")
            akceleracija += -self.G * tijelo.m * (tijelo1.p[-1] - tijelo.p[-1]) / (np.linalg.norm(tijelo1.p[-1] - tijelo.p[-1]))**3

        return akceleracija

    def move(self):
        i = 0

        for tijelo in self.svemir:
            planeti = self.svemir.copy()
            planeti.pop(i)

            while self.t[-1] > self.vrijeme_gibanja:
                tijelo.a.append(self.__akceleracija(tijelo, planeti))
                tijelo.v.append(tijelo.v[-1] + tijelo.a[-1] * self.dt)
                tijelo.p.append(tijelo.p[-1] + tijelo.v[-1] * self.dt)
                self.t.append(self.t[-1] - self.dt)

            i += 1
            self.t = [0]