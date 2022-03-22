import particle as prt

prt1 = prt.Particle(0.01)
prt1.set_initial_conditions(10, 60, 0, 0)
domet = prt1.range()
prt1.plot_trajectory()
prt1.analiticko_rjesenje(domet)