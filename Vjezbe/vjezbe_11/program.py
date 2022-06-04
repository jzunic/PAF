import modul as md
import numpy as np

konstante = md.Konstante()

tijelo1 = md.Tijelo(
    np.array((konstante.udaljenost_s_z, 0)),
    np.array((0, konstante.v_okomito)),
    konstante.M_z
)

tijelo2 = md.Tijelo(
    np.array((0, 0)),
    np.array((0, 0)),
    konstante.M_s
)

gibanje = md.Gibanje(tijelo1, tijelo2, konstante.godina, 360)
gibanje.plot()
