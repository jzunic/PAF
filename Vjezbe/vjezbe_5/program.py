import matplotlib.pyplot as plt
import harmonic_oscillator as har
import numpy as np
import math

masa = 10
el_opruge = 1000
x_poc = 0.3
vrijeme_oscilacije = 2

def elongacija_brzina_akceleracija():
    osc = har.HarmonicOscillator(x_poc, 0.001, masa, el_opruge, vrijeme_oscilacije)

    osc.oscillate()
    osc.plot()

def xt_graf():
    t_analiticko = np.linspace(0, 2, 1000)
    period_analiticki = math.sqrt(el_opruge/masa)
    x_analiticko = x_poc * np.cos(period_analiticki * t_analiticko)


    osc1 = har.HarmonicOscillator(x_poc, 0.1, masa, el_opruge, vrijeme_oscilacije)
    osc2 = har.HarmonicOscillator(x_poc, 0.01, masa, el_opruge, vrijeme_oscilacije)
    osc3 = har.HarmonicOscillator(x_poc, 0.001, masa, el_opruge, vrijeme_oscilacije)

    osc1.oscillate()
    osc2.oscillate()
    osc3.oscillate()

    plt.scatter(osc1.t, osc1.x, s=3, color="red")
    plt.scatter(osc2.t, osc2.x, s=2, color="green")
    plt.scatter(osc3.t, osc3.x, s=1, color="orange")
    plt.plot(t_analiticko, x_analiticko)
    plt.xlabel("t/s")
    plt.ylabel("x/m")
    plt.title("Usporedba numerickih polozaja s analitickim rjesenjem")
    plt.legend([
        "0.1",
        "0.01",
        "0.001",
        "analiticko"
    ])

    plt.show()

def numericki_period_ovisnost():
    t_lista = np.linspace(0.1, 0.001, 10)
    analiticka_rjesenja = []
    numericka_rjesenja = []
    

    for t in t_lista:
        osc = har.HarmonicOscillator(x_poc, t, masa, el_opruge, vrijeme_oscilacije)
        
        osc.oscillate()
        numericka_rjesenja.append(osc.numericki_period())
        analiticka_rjesenja.append(osc.analiticki_period())
    
    plt.plot(t_lista, analiticka_rjesenja)
    plt.scatter(t_lista, numericka_rjesenja, s=3, color="red")
    plt.title("Ovisnost numerickog perioda titranja o odabiru vremenskog intervala dt")
    plt.xlabel("dt/s")
    plt.ylabel("T/s")
    plt.legend([
        "analiticko rjesenje",
        "numericko na segmentu [0.001, 0.1]"
    ])

    plt.show()

elongacija_brzina_akceleracija()
xt_graf()
numericki_period_ovisnost()


