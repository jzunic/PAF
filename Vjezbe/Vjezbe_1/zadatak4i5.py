import matplotlib.pyplot as plt


def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = -k * x1 + y1
    print("y = {}x + ({})".format(k, l))


pravac(1,2,3,4)


def nacrtaj():
    tocka1 = [1, 2]
    tocka2 = [3, 4]
    x_koordinate = [1, 3]
    y_koordinate = [2, 4]
    x_vrijednosti = [tocka1[0], tocka2[0]]
    y_vrijednoti = [tocka1[1], tocka2[1]]

    plt.scatter(x_koordinate, y_koordinate)
    plt.plot(x_vrijednosti, y_vrijednoti)
    plt.show()


def spremi():
    ime = input("Pod kojim imenom zelite spremiti graf: ")
    tocka1 = [1, 2]
    tocka2 = [3, 4]
    x_koordinate = [1, 3]
    y_koordinate = [2, 4]
    x_vrijednosti = [tocka1[0], tocka2[0]]
    y_vrijednoti = [tocka1[1], tocka2[1]]

    plt.scatter(x_koordinate, y_koordinate)
    plt.plot(x_vrijednosti, y_vrijednoti)
    plt.savefig("{}.pdf".format(ime))


plot_or_save = input("Zelite li prikazati graf pravca (1) ili ga spremiti kao pdf (2): ")
if plot_or_save == "1":
    nacrtaj()
elif plot_or_save == "2":
    spremi()