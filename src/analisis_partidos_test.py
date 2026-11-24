from analisis_partidos import *

print("Leyendo datos de partidos de 'data/partidos.csv'...")
PARTIDOS = lee_partidos('data/partidos.csv')
print(f"\t {len(PARTIDOS)} partidos leídos, desde {PARTIDOS[0].date} hasta {PARTIDOS[-1].date}")
print()

def formatea_partido(partido: Partido | None) -> str:
    """
    Devuelve una cadena con el resultado de un partido, para mostrarlo por pantalla.
    Por ejemplo: '1954-06-26 Switzerland 5-7 Austria (FIFA World Cup, Lausanne)'
    """
    if partido == None:
        return "None"
    return (f"{partido.date} {partido.home_team} {partido.home_score}-{partido.away_score} "
            f"{partido.away_team} ({partido.tournament}, {partido.city})")

def test_obten_torneos():
    print("Probando obten_torneos...")
    torneos = obten_torneos(PARTIDOS)
    print(f"\t Hay {len(torneos)} torneos distintos. Algunos de ellos: {sorted(torneos)[:5]}")
    assert len(torneos) == 227
    assert {'FIFA World Cup', 'UEFA Euro', 'Copa América', 'Friendly'} <= torneos
    print("\t OK")
    print()

def test_busca_partido_con_mas_goles():
    print("Probando busca_partido_con_mas_goles...")
    partido_mundial = busca_partido_con_mas_goles(PARTIDOS, 'FIFA World Cup')
    print(f"\t Partido con más goles de la historia de los Mundiales: {formatea_partido(partido_mundial)}")
    assert partido_mundial.date == date(1954, 6, 26)
    assert partido_mundial.home_team == 'Switzerland'
    assert partido_mundial.away_team == 'Austria'

    partido_eurocopa = busca_partido_con_mas_goles(PARTIDOS, 'UEFA Euro')
    print(f"\t Partido con más goles de la historia de las Eurocopas: {formatea_partido(partido_eurocopa)}")
    assert partido_eurocopa.date == date(1960, 7, 6)
    assert partido_eurocopa.home_team == 'France'
    assert partido_eurocopa.away_team == 'Yugoslavia'

    assert busca_partido_con_mas_goles(PARTIDOS, 'Nonexistent Tournament') == None
    print("\t OK")
    print()

def test_busca_ultimos_partidos_de_seleccion():
    print("Probando busca_ultimos_partidos_de_seleccion...")
    ultimos_partidos = busca_ultimos_partidos_de_seleccion(PARTIDOS, 'Spain')
    print("\t Últimos partidos de España:")
    for partido in ultimos_partidos:
        print(f"\t\t {formatea_partido(partido)}")
    assert len(ultimos_partidos) == 5
    assert ultimos_partidos[0].date == date(2026, 9, 29)
    assert ultimos_partidos[-1].date == date(2026, 11, 15)
    assert ultimos_partidos[-1].away_team == 'England'

    ultimos_partidos = busca_ultimos_partidos_de_seleccion(PARTIDOS, 'Canary Islands')
    print(f"\t Las Islas Canarias sólo han jugado {len(ultimos_partidos)} partidos internacionales:")
    for partido in ultimos_partidos:
        print(f"\t\t {formatea_partido(partido)}")
    assert len(ultimos_partidos) == 4
    print("\t OK")
    print()

def test_calcula_goles_marcados():
    print("Probando calcula_goles_marcados...")
    goles_españa = calcula_goles_marcados(PARTIDOS, 'Spain')
    goles_andorra = calcula_goles_marcados(PARTIDOS, 'Andorra')
    print(f"\t España ha marcado {goles_españa} goles en toda su historia; Andorra, {goles_andorra}")
    assert goles_españa == 1633
    assert goles_andorra == 79
    assert calcula_goles_marcados(PARTIDOS, 'Nonexistent Team') == 0
    print("\t OK")
    print()

def test_calcula_goles_marcados_2():
    print("Probando calcula_goles_marcados_2...")
    goles_españa = calcula_goles_marcados_2(PARTIDOS, 'Spain')
    goles_andorra = calcula_goles_marcados_2(PARTIDOS, 'Andorra')
    print(f"\t España ha marcado {goles_españa} goles en toda su historia; Andorra, {goles_andorra}")
    assert goles_españa == 1633
    assert goles_andorra == 79
    assert calcula_goles_marcados_2(PARTIDOS, 'Nonexistent Team') == 0
    print("\t OK")
    print()

def test_ha_ganado_todos():
    print("Probando ha_ganado_todos...")
    res = ha_ganado_todos(PARTIDOS, 'Spain', 'UEFA Euro', 2024)
    print(f"\t ¿Ganó España todos sus partidos en la Eurocopa 2024? {res}")
    assert res == True

    res = ha_ganado_todos(PARTIDOS, 'Spain', 'FIFA World Cup', 2010)
    print(f"\t ¿Ganó España todos sus partidos en el Mundial 2010? {res}")
    assert res == False

    res = ha_ganado_todos(PARTIDOS, 'Argentina', 'FIFA World Cup', 2022)
    print(f"\t ¿Ganó Argentina todos sus partidos en el Mundial 2022? {res}")
    assert res == False  # Perdió un partido y empató otros dos (decididos en los penaltis)

    assert ha_ganado_todos(PARTIDOS, 'Spain', 'FIFA World Cup', 1800) == True  # Vacío
    print("\t OK")
    print()

def test_busca_seleccion_con_mas_goles():
    print("Probando busca_seleccion_con_mas_goles...")
    res = busca_seleccion_con_mas_goles(PARTIDOS)
    print(f"\t La selección más goleadora de la historia es: {res}")
    seleccion, goles = res
    assert seleccion == 'England'
    assert goles == 2420
    assert busca_seleccion_con_mas_goles([]) == None
    print("\t OK")
    print()

def test_ha_ganado_alguna_vez():
    print("Probando ha_ganado_alguna_vez...")
    res = ha_ganado_alguna_vez(PARTIDOS, 'Spain', 'Brazil')
    print(f"\t ¿Ha ganado España alguna vez a Brasil? {res}")
    assert res == True

    res = ha_ganado_alguna_vez(PARTIDOS, 'Spain', 'Andorra')
    print(f"\t ¿Ha ganado España alguna vez a Andorra? {res}")
    assert res == True

    res = ha_ganado_alguna_vez(PARTIDOS, 'Andorra', 'Spain')
    print(f"\t ¿Y Andorra a España? {res}")
    assert res == False

    assert ha_ganado_alguna_vez(PARTIDOS, 'Spain', 'Nonexistent Team') == False
    print("\t OK")
    print()

def test_busca_primera_victoria():
    print("Probando busca_primera_victoria...")
    primera_victoria = busca_primera_victoria(PARTIDOS, 'Spain')
    print(f"\t Primera victoria de España: {formatea_partido(primera_victoria)}")
    assert primera_victoria.date == date(1920, 8, 28)
    assert primera_victoria.away_team == 'Denmark'

    primera_victoria = busca_primera_victoria(PARTIDOS, 'San Marino')
    print(f"\t Primera victoria de San Marino: {formatea_partido(primera_victoria)}")
    assert primera_victoria.date == date(2004, 4, 28)
    assert primera_victoria.away_team == 'Liechtenstein'

    assert busca_primera_victoria(PARTIDOS, 'Nonexistent Team') == None
    print("\t OK")
    print()

def test_busca_mayores_goleadas():
    print("Probando busca_mayores_goleadas...")
    goleadas = busca_mayores_goleadas(PARTIDOS, 'Spain')
    print("\t Mayores goleadas de España:")
    for partido in goleadas:
        print(f"\t\t {formatea_partido(partido)}")
    assert len(goleadas) == 5
    assert [p.date for p in goleadas] == [date(1933, 5, 21), date(1983, 12, 21), date(2013, 6, 20),
                                          date(1999, 6, 5), date(1999, 3, 27)]

    goleadas = busca_mayores_goleadas(PARTIDOS, 'Germany', 2)
    print("\t Mayores goleadas de Alemania:")
    for partido in goleadas:
        print(f"\t\t {formatea_partido(partido)}")
    assert [p.date for p in goleadas] == [date(1912, 7, 1), date(2006, 9, 6)]

    assert busca_mayores_goleadas(PARTIDOS, 'Nonexistent Team') == []
    print("\t OK")
    print()

def test_calcula_media_goles_por_edicion():
    print("Probando calcula_media_goles_por_edicion...")
    medias = calcula_media_goles_por_edicion(PARTIDOS, 'FIFA World Cup')
    print("\t Media de goles por partido en cada Mundial:")
    for año, media in sorted(medias.items()):
        print(f"\t\t {año}: {media:.2f}")
    assert len(medias) == 23
    assert abs(medias[1954] - 5.384615) < 1e-6
    assert abs(medias[2010] - 2.265625) < 1e-6
    assert abs(medias[2022] - 2.6875) < 1e-6
    assert calcula_media_goles_por_edicion(PARTIDOS, 'Nonexistent Tournament') == {}
    print("\t OK")
    print()

def test_cuenta_partidos_por_pais_sede():
    print("Probando cuenta_partidos_por_pais_sede...")
    partidos_por_pais = cuenta_partidos_por_pais_sede(PARTIDOS, 'FIFA World Cup')
    print(f"\t Países que más partidos de Mundiales han acogido: {partidos_por_pais.most_common(5)}")
    print(f"\t Partidos de Mundiales jugados en España: {partidos_por_pais['Spain']}")
    assert len(partidos_por_pais) == 19
    assert partidos_por_pais.most_common(2) == [('United States', 130), ('Germany', 102)]
    assert partidos_por_pais['Spain'] == 52
    assert cuenta_partidos_por_pais_sede(PARTIDOS, 'Nonexistent Tournament') == Counter()
    print("\t OK")
    print()

def test_filtra_partidos():
    print("Probando filtra_partidos...")
    neutrales = filtra_partidos(PARTIDOS, lambda p: p.neutral)
    print(f"\t Partidos jugados en campo neutral: {len(neutrales)}")
    assert len(neutrales) == 13245

    goleadas = filtra_partidos(PARTIDOS, lambda p: p.home_score + p.away_score >= 15)
    print(f"\t Partidos con 15 goles o más: {len(goleadas)}. El primero de ellos:")
    print(f"\t\t {formatea_partido(goleadas[0])}")
    assert len(goleadas) == 66

    partidos_españa = filtra_partidos(PARTIDOS, lambda p: juega(p, 'Spain'))
    print(f"\t Partidos jugados por España: {len(partidos_españa)}")
    assert len(partidos_españa) == 797
    print("\t OK")
    print()

def test_aplica_a_partidos_de_seleccion():
    print("Probando aplica_a_partidos_de_seleccion...")
    goles = aplica_a_partidos_de_seleccion(PARTIDOS, 'Spain', goles_a_favor)
    print(f"\t Goles marcados por España en sus 5 primeros partidos: {goles[:5]}")
    assert len(goles) == 797
    assert goles[:5] == [1, 1, 2, 2, 3]
    assert sum(goles) == 1633

    goles_recibidos = aplica_a_partidos_de_seleccion(PARTIDOS, 'Spain', goles_en_contra)
    print(f"\t Goles marcados por España: {sum(goles)}; goles recibidos: {sum(goles_recibidos)}")
    assert sum(goles_recibidos) == 711

    años = aplica_a_partidos_de_seleccion(PARTIDOS, 'Spain', lambda p, s: p.date.year)
    print(f"\t España jugó su primer partido en {años[0]} y el último en {años[-1]}")
    assert años[0] == 1920
    assert aplica_a_partidos_de_seleccion(PARTIDOS, 'Nonexistent Team', goles_a_favor) == []
    print("\t OK")
    print()

test_obten_torneos()
#test_busca_partido_con_mas_goles()
#test_busca_ultimos_partidos_de_seleccion()
#test_calcula_goles_marcados()
#test_calcula_goles_marcados_2()
#test_ha_ganado_todos()
#test_busca_seleccion_con_mas_goles()
#test_ha_ganado_alguna_vez()
#test_busca_primera_victoria()
#test_busca_mayores_goleadas()
#test_calcula_media_goles_por_edicion()
#test_cuenta_partidos_por_pais_sede()
#test_filtra_partidos()
#test_aplica_a_partidos_de_seleccion()
print("Todos los tests se ejecutaron correctamente.")
