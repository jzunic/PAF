import numpy as np
import matplotlib.pyplot as plt
import math
def kosi_hitac(pocetna_brzina, kut_izbacaja, vrijeme):
    """
    Racuna vertikalne i horizontalne komponente brzine, visine i horizontalne udaljenosti.
    Prvo opcenito racuna gore navedene stavke. U slucaju da je korisnik unio za vrijeme vrijednost
    koja je veca od vremena gibanja projektila, funkcija ce uneseno vrijeme skratiti na vrijeme potrebno
    da projektil padne na tlo. Tada se prijasnje navedene stavke krate na samo moguce vrijednosti koje
    tijelo moze poprimiti u gibanju (npr. prva petlja vraca vrijednosti y koje mogu ici ispod nule sto
    nema fizikalnog smisla). U slucaju da korisnik unese vrijednost vremena koja je manja od vremena leta
    projektila, prve unesene vrijednosti se ne mijenjaju.

    Parametri
    ---------
    pocetna_brzina : float
        pocetna brzina projektila
    kut_izbacaja : float
        kut pod kojim je projektil izbacen
    vrijeme : float
        vrijeme koje korisnik unosi kao vrijeme leta tijela

    Funkcija vraca
    ---------
    nova_v_y_lista : list of float
        lista svih vertikalnih komponenti brzina
    nova_v_x_lista : list of float
        lista svih horizontalnih komponenti brzina
    lista_y : list of float
        lista svih visina na kojima se nalazio projektil
    lista_x : list of float
        lista svih horizontalnih udaljenosti od tocke izbacaja

    """
    dt = 0.01
    Dt = dt/10
    v_0_x = pocetna_brzina * np.cos(kut_izbacaja * np.pi / 180)
    v_0_y = pocetna_brzina * np.sin(kut_izbacaja * np.pi / 180)

    x_poc = 0
    y_poc = 0
    g = -9.81

    v_y_lista = []
    v_x_lista = []
    nova_v_y_lista = []
    nova_v_x_lista = []
    t = []
    x_lista = []
    y_lista = []

    for i in range(int(vrijeme / dt)):
        v_x_lista.append(v_0_x)
        v_y_lista.append(v_0_y)
        t.append(dt * i)

        v_y = v_0_y + g * dt
        y = y_poc + v_0_y * dt + 1/2 * g * dt**2
        x = x_poc + v_0_x * dt

        v_y_lista.append(v_y)
        x_lista.append(x)
        y_lista.append(y)

        v_0_y = v_y
        y_poc = y
        x_poc = x

    projektil_pao = False

    for i in range(int(vrijeme/dt)):
        if y_lista[i] <= 0:
            vrijeme_pada = i * dt
            projektil_pao = True
            break
    if projektil_pao:
        v_0_y = pocetna_brzina * np.sin(kut_izbacaja * np.pi / 180) 

        for i in range(int(vrijeme_pada / Dt)):
            v_y = 0
            v_y = v_0_y + g * Dt

            nova_v_y_lista.append(v_y)
            nova_v_x_lista.append(v_0_x)

            v_0_y = v_y
    else:
        print("Projektil u toliko vremena jos nije pao na pod")
        nova_v_y_lista = v_y_lista.copy()
        nova_v_x_lista = v_x_lista.copy()

    return nova_v_y_lista, nova_v_x_lista, y_lista, x_lista


def max_visina(niz_visina):
    """
    Funkcija sortira listu visina na kojima se nalazio projektil; ispisuje i vraca najvecu visinu.

    Parametri
    ---------
    niz_visina : list of float
        lista visina na kojima se tijelo nalazilo dok je letilo
    
    Funkcija vraca
    ---------
    sortirani_niz[0] : float
        najvecu visinu na kojoj se tijelo nalazilo
    """
    sortirani_niz = sorted(niz_visina, reverse=True)
    print("Najveca visina koju projektil postigne je: {}m".format(sortirani_niz[0]))
    return sortirani_niz[0]


def domet(niz_udaljenosti):
    """
    Funkcija sortira listu horizontalnih udaljenosti od mjesta izbacaja; ispisuje i vraca najvecu udaljenost

    Parametri
    ---------
    niz_udaljenosti : list of float
        lista horizontalnih udaljenosti od mjesta izbacaja 
    
    Funckija vraca
    ---------
    sortirani_niz[0] : float
        najveca horizontalna udaljenost od mjesta izbacaja
    """
    sortirani_niz = sorted(niz_udaljenosti, reverse=True)
    print("Najveca horizontalna udaljenost projektila od tocke izbacaja je: {}m".format(sortirani_niz[0]))
    return sortirani_niz[0]

def max_brzina(x_brzina, y_brzine):
    """
    Funkcija pronalazi najvecu vrijednosti vertikalne komponente brzine te racuna i ispisuje najvecu 
    ukupnu vrijednost brzine projektila u letu.

    Parametri
    ---------
    x_brzina : float
        horizontalna komponenta brzine
    y_brzine : list of float
        lista vertikalnih vrijednosti brzina
    """
    niz_brzina = []

    for v_y in y_brzine:
        v = math.sqrt(x_brzina**2 + v_y**2)
        niz_brzina.append(v)
    
    print("Maximalna brzina projektila tijekom leta je: {}m/s".format(sorted(niz_brzina, reverse=True)[0]))

def xy_graf(x_lista, y_lista):
    """
    Funkcija koja crta x - y graf, tj. graf putanje tijela. Sve vrijednosti koje nemaju fizikalnog smisla
    se izbacuju iz lista.

    Parametri
    ---------
    x_lista: list of float
        lista svih horizontalnih udaljenosti od mjesta izbacaja
    y_lista: list of float
        lista svih visina na kojima se projektil nalazio
    
    Funkcija vraca
    ---------
    nova_x_lista : list of float
        lista udaljenosti koje imaju fizikalnog smisla
    nova_y_lista : list of float
        lisza visina koje imaju fizikalnog smisla
    """
    for i in range(len(y_lista)):
        if y_lista[i] <= 0:
            nova_y_lista = y_lista[:i]
            nova_x_lista = x_lista[:i]
            break
        else:
            nova_y_lista = y_lista.copy()
            nova_x_lista = x_lista.copy()
    
    
    plt.plot(nova_x_lista, nova_y_lista)
    plt.xlabel("x/m")
    plt.ylabel("y/m")
    plt.title("x-y graf gibanja tijela")
    plt.show()

    return nova_x_lista, nova_y_lista

def meta(x_s, y_s, radijus, domet, max_visina, x_lista, y_lista):
    """
    Funkcija koja odreduje je li projektil u letu pogodio proizvoljno postavljenu metu, crta graf putanje
    projektila i metu. U slucaju da projektil nije pogodio metu, racuna najmanju udaljenost projektila od 
    mete.

    Parametri
    ---------
    x_s : float
        x koordinata sredista kruzne mete
    y_s : float
        y koordinata sredista kruzne mete
    radijus : float
        radijus kruzne mete
    domet : float
        maksimalna horizontalna udaljenost projektila od tocke izbacaja
    max_visina : float
        maksimalna vertikalna udaljenost od tocke izbacaja
    x_lista : float
        lista horizontalnih udaljenosti projektila od tocke izbacaja
    y_lista : float
        lista vertikalnih udaljenosti projektila od tocke izbacaja
    """
    pogodio = False

    for x, y in zip(x_lista, y_lista):
        if ((x - x_s)**2 + (y - y_s)**2) <= radijus**2:
            pogodio = True
    
    if pogodio:
        print("Projektil je pogodio metu")
    else: 
        print("Projektil nije pogodio metu")

        lista_udaljenosti = []

        for x, y in zip(x_lista, y_lista):
            udaljenost = math.sqrt((x-x_s)**2 + (y-y_s)**2) - radijus
            lista_udaljenosti.append(udaljenost)
        
        lista_udaljenosti = sorted(lista_udaljenosti)
        najmanja_udaljenost = lista_udaljenosti[0]
        
        print("Najmanja udaljenost izmedu mete i projektila je {}m". format(najmanja_udaljenost))


    figure, graf1 = plt.subplots()
    kruznica = plt.Circle((x_s, y_s), radijus, fill=False)
    plt.gcf().gca().add_artist(kruznica)
    graf1.set_aspect(1)
    graf1.set_xlim([0, domet + radijus])
    graf1.set_ylim([0, max_visina + radijus])

    plt.plot(x_lista, y_lista)
    plt.xlabel("x/m")
    plt.ylabel("y/m")
    plt.title("x-y graf gibanja tijela")
    plt.show()