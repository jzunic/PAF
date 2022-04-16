import modul

motion1 = modul.Motion(10, 0.01, 10, 10, 0, 0, lambda v, x, t: -100*x)
motion1.motion()
motion1.plot()

motion2 = modul.Motion(0, 0.01, 10, 10, 5, 0, lambda v, x, t: 10)
motion2.motion()
motion2.plot()

motion3 = modul.Motion(0, 0.01, 10, 10, 0, 0, lambda v, x, t: v + x + t)
motion3.motion()
motion3.plot()

#Ne znam bas sto ocekivati za graf od motion3. Motion1 i motion2 se slazu s
#analitickim rjesenjem.