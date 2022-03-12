import zadatak4_modul as gibanje_projektila

v_y_lista, v_x_lista, y_lista, x_lista = gibanje_projektila.kosi_hitac(45.3, 34.1, 10)

nova_x_lista, nova_y_lista = gibanje_projektila.xy_graf(x_lista, y_lista)

Max_visina = gibanje_projektila.max_visina(nova_y_lista)

range = gibanje_projektila.domet(nova_x_lista)

gibanje_projektila.max_brzina(v_x_lista[0], v_y_lista)

gibanje_projektila.meta(40, 12, 15, range, Max_visina, x_lista, y_lista)