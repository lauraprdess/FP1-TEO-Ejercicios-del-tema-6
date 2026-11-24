from collections import defaultdict, Counter, namedtuple
from datetime import date
import csv

Partido = namedtuple('Partido',
                     ['date',          # Fecha del partido, de tipo date
                      'home_team',     # Selección local, de tipo str
                      'away_team',     # Selección visitante, de tipo str
                      'home_score',    # Goles de la selección local, de tipo int
                      'away_score',    # Goles de la selección visitante, de tipo int
                      'tournament',    # Torneo o competición, de tipo str
                      'city',          # Ciudad donde se jugó el partido, de tipo str
                      'country',       # País donde se jugó el partido, de tipo str
                      'neutral'        # True si se jugó en campo neutral, de tipo bool
                     ])

def lee_partidos(ruta_archivo: str) -> list[Partido]:
    """
    Lee un archivo CSV con resultados de partidos internacionales de fútbol
    y devuelve una lista de tuplas Partido con la información de cada partido.

    Parámetros:
    ruta_archivo (str): Ruta al archivo CSV que contiene los datos.

    Devuelve:
    list[Partido]: Lista de tuplas Partido con los datos leídos del archivo.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        partidos = []
        lector = csv.reader(f)
        next(lector)
        for fecha, local, visitante, goles_local, goles_visitante, torneo, ciudad, pais, neutral in lector:
            partido = Partido(
                date=date.fromisoformat(fecha),
                home_team=local,
                away_team=visitante,
                home_score=int(goles_local),
                away_score=int(goles_visitante),
                tournament=torneo,
                city=ciudad,
                country=pais,
                neutral=neutral == 'TRUE'
            )
            partidos.append(partido)
        return partidos

def juega(partido: Partido, seleccion: str) -> bool:
    """
    Indica si una selección ha jugado un partido (como local o como visitante).

    Parámetros:
    partido (Partido): Partido a comprobar.
    seleccion (str): Nombre de la selección.

    Devuelve:
    bool: True si la selección es la local o la visitante del partido, False en caso contrario.
    """
    return partido.home_team == seleccion or partido.away_team == seleccion

def goles_a_favor(partido: Partido, seleccion: str) -> int:
    """
    Devuelve los goles que marcó una selección en un partido.
    Se supone que la selección ha jugado el partido.

    Parámetros:
    partido (Partido): Partido jugado por la selección.
    seleccion (str): Nombre de la selección.

    Devuelve:
    int: Goles marcados por la selección en el partido.
    """
    if partido.home_team == seleccion:
        return partido.home_score
    return partido.away_score

def goles_en_contra(partido: Partido, seleccion: str) -> int:
    """
    Devuelve los goles que recibió una selección en un partido.
    Se supone que la selección ha jugado el partido.

    Parámetros:
    partido (Partido): Partido jugado por la selección.
    seleccion (str): Nombre de la selección.

    Devuelve:
    int: Goles recibidos por la selección en el partido.
    """
    if partido.home_team == seleccion:
        return partido.away_score
    return partido.home_score

def obten_torneos(partidos: list[Partido]) -> set[str]:
    """
    Devuelve un conjunto con los distintos torneos de los partidos.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.

    Devuelve:
    set[str]: Conjunto de torneos distintos.
    """
    # TODO: Ejercicio 1
    pass

def busca_partido_con_mas_goles(partidos: list[Partido], torneo: str) -> Partido | None:
    """
    Devuelve el partido del torneo indicado en el que se marcaron más goles en total
    (sumando los de ambas selecciones). Si no hay partidos de ese torneo, devuelve None.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    torneo (str): Torneo para filtrar los partidos.

    Devuelve:
    Partido | None: Partido con más goles del torneo, o None si no hay partidos de ese torneo.
    """
    # TODO: Ejercicio 2
    pass

def busca_ultimos_partidos_de_seleccion(partidos: list[Partido], seleccion: str) -> list[Partido]:
    """
    Devuelve una lista con los 5 últimos partidos jugados por una selección, ordenados
    cronológicamente (del más antiguo al más reciente). Si la selección ha jugado menos
    de 5 partidos, devuelve todos ellos.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.

    Devuelve:
    list[Partido]: Lista con los últimos 5 partidos de la selección.
    """
    # TODO: Ejercicio 3
    pass

def calcula_goles_marcados(partidos: list[Partido], seleccion: str) -> int:
    """
    Calcula el total de goles marcados por una selección en todos sus partidos.
    Resuélvelo usando un generador.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.

    Devuelve:
    int: Total de goles marcados por la selección.
    """
    # TODO: Ejercicio 4
    pass

def calcula_goles_marcados_2(partidos: list[Partido], seleccion: str) -> int:
    """
    Calcula el total de goles marcados por una selección en todos sus partidos.
    Resuélvelo usando map y filter.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.

    Devuelve:
    int: Total de goles marcados por la selección.
    """
    # TODO: Ejercicio 5
    pass

def ha_ganado_todos(partidos: list[Partido], seleccion: str, torneo: str, año: int) -> bool:
    """
    Comprueba si una selección ganó todos los partidos que jugó en un torneo
    durante un año determinado. Si la selección no jugó ningún partido de ese
    torneo en ese año, devuelve True.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.
    torneo (str): Torneo a considerar.
    año (int): Año a considerar.

    Devuelve:
    bool: True si la selección ganó todos sus partidos del torneo en ese año, False en caso contrario.
    """
    # TODO: Ejercicio 6
    pass

def busca_seleccion_con_mas_goles(partidos: list[Partido]) -> tuple[str, int] | None:
    """
    Busca la selección que más goles ha marcado en total, sumando los marcados como
    local y como visitante. Devuelve una tupla con el nombre de la selección y el
    total de goles. Si no hay partidos, devuelve None.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.

    Devuelve:
    tuple[str, int] | None: Selección con más goles y su total, o None si no hay partidos.
    """
    # TODO: Ejercicio 7
    pass


def ha_ganado_alguna_vez(partidos: list[Partido], seleccion: str, rival: str) -> bool:
    """
    Comprueba si una selección ha ganado alguna vez a otra selección.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.
    rival (str): Nombre de la selección rival.

    Devuelve:
    bool: True si la selección ha ganado al rival en al menos un partido, False en caso contrario.
    """
    # TODO: Ejercicio 8
    pass

def busca_primera_victoria(partidos: list[Partido], seleccion: str) -> Partido | None:
    """
    Devuelve el primer partido (el de fecha más antigua) que ganó una selección.
    Si la selección no ha ganado ningún partido, devuelve None.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.

    Devuelve:
    Partido | None: Primera victoria de la selección, o None si no ha ganado ningún partido.
    """
    # TODO: Ejercicio 9
    pass

def busca_mayores_goleadas(partidos: list[Partido], seleccion: str, n: int = 5) -> list[Partido]:
    """
    Devuelve una lista con las n victorias de una selección con mayor diferencia de goles,
    ordenadas de mayor a menor diferencia. Si hay empate en la diferencia de goles, va antes
    el partido en el que la selección marcó más goles; y si persiste el empate, el más reciente.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.
    n (int): Número de partidos a devolver.

    Devuelve:
    list[Partido]: Lista con las n mayores goleadas conseguidas por la selección.
    """
    # TODO: Ejercicio 10
    pass

def calcula_media_goles_por_edicion(partidos: list[Partido], torneo: str) -> dict[int, float]:
    """
    Calcula la media de goles por partido de cada edición (año) de un torneo.
    Devuelve un diccionario cuyas claves son los años en los que se jugaron partidos
    del torneo y cuyos valores son la media de goles por partido de ese año.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    torneo (str): Nombre del torneo.

    Devuelve:
    dict[int, float]: Diccionario con la media de goles por partido de cada año del torneo.
    """
    # TODO: Ejercicio 11
    pass

def cuenta_partidos_por_pais_sede(partidos: list[Partido], torneo: str) -> Counter:
    """
    Cuenta cuántos partidos de un torneo se han jugado en cada país.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    torneo (str): Nombre del torneo.

    Devuelve:
    Counter: Contador con el número de partidos del torneo jugados en cada país.
    """
    # TODO: Ejercicio 12
    pass

def filtra_partidos(partidos: list[Partido], condicion) -> list[Partido]:
    """
    Devuelve una lista con los partidos que cumplen una condición.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    condicion (función): Función que recibe un Partido y devuelve un bool.

    Devuelve:
    list[Partido]: Lista con los partidos para los que la condición devuelve True.
    """
    # TODO: Ejercicio 13
    pass

def aplica_a_partidos_de_seleccion(partidos: list[Partido], seleccion: str, funcion) -> list:
    """
    Devuelve una lista con el resultado de aplicar una función a cada partido jugado
    por una selección, en el mismo orden en que aparecen en la lista de partidos.

    Parámetros:
    partidos (list[Partido]): Lista de partidos.
    seleccion (str): Nombre de la selección.
    funcion (función): Función que recibe un Partido y el nombre de una selección, y devuelve un valor.

    Devuelve:
    list: Lista con los resultados de aplicar la función a cada partido de la selección.
    """
    # TODO: Ejercicio 14
    pass
