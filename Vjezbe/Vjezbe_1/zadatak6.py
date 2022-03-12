import matplotlib.pyplot as plt
import math

def kruznica(x1, y1, R, xs, ys):

    #gdje se nalazi tocka

    jednadzba = (x1 - xs)**2 + (y1 - ys)**2
    print(jednadzba)
    if jednadzba > R**2:
        print("Tocka se nalazi van kruznice")
    elif jednadzba < R**2:
        print("Tocka se nalazi unutar kruznice")
    else:
        print("Tocka se nalazi na kruznici")

    #koliko je tocka udaljena od najblize tocke na kruznici
    #pravac koji prolazi sredistem kruznice i nasom tockom
    if jednadzba == R**2:
        print("Udaljenost od kruznice je 0")
    else:
        k = (y1-ys)/(x1-xs)
        l =  -k*x1 + y1

        #sustav (x-xs)**2 + (y-ys)**2 = R**2 i y = kx + l, dat ce dvije tocke od koje uzimam samo onu kojoj je udaljenost d nase manja
        rjesenje1x = (-(2*k*l-2*xs-2*k*ys) + math.sqrt((2*k*l-2*xs-2*k*ys)**2-4*(1+k**2)*(-(R**2)-2*l*ys+l**2+ys**2+xs**2)))/2*(1+k**2)
        rjesenje2x = (-(2 * k * l - 2 * xs - 2 * k * ys) - math.sqrt((2 * k * l - 2 * xs - 2 * k * ys) ** 2 - 4 * (1 + k ** 2) * (-(R ** 2) - 2 * l * ys + l ** 2 + ys ** 2 + xs ** 2))) / 2 * (1 + k ** 2)
        rjesenje1y = k*rjesenje1x + l
        rjesenje2y = k*rjesenje2x + l

        d1 = math.sqrt((x1 - rjesenje1x)**2 + (y1 - rjesenje1y)**2)
        d2 = math.sqrt((x1 - rjesenje2x)**2 + (y1 - rjesenje2y)**2)

        if d1 > d2:
            print("tocka je od kruznice udaljena za {}". format(d2))
        else:
            print("tocka je od kruznice udaljena za {}".format(d1))


    #plot
    figure, axes = plt.subplots()
    kruznica = plt.Circle((xs, ys), R, fill=False)
    plt.gcf().gca().add_artist(kruznica)
    axes.set_aspect(1)
    axes.set_xlim([-5,5])
    axes.set_ylim([-5,5])
    plt.scatter(x1, y1)

    odgovor = input("Zelite li sliku samo prikazati (1) ili ju zelite spremiti pod nekim imenom (2): ")
    if odgovor == "1":
        plt.show()
    else:
        ime = input("Pod kojim imenom zelite spremiti sliku: ")
        plt.savefig("{}.pdf".format(ime))


kruznica(4,0,3,0,0)