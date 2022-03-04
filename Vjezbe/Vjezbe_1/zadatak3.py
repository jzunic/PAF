x = []
y = []

for i in range(2):
    temp_x = input("Unesite x koordinatu tocke: ")
    try:
        true_x = float(temp_x)
        #Ako unos nije broj onda ce izbaciti gresku i poslati na ponovni unos
    except:
        print("Unijeli ste krivo, unesite ponovno")
        true_x = input("Unesite x koordinatu tocke: ")
    temp_y = input("Unesite y koordinatu tocke: ")
    try:
        true_y = float(temp_y)
    except:
        print("Unijeli ste krivo, unesite ponovno")
        true_y = input("Unesite y koordinatu tocke: ")
    x.append(true_x)
    y.append(true_y)
print(x,y)
#formula y-y0 = k(x-x0), k = (y2 - y1)/(x2 - x1), y = kx - kx0 + y0

k = (y[0] - y[1])/(x[0] - x[1])
l = -k*x[0] + y[0]

print("y = {}x + ({})". format(k, l))
