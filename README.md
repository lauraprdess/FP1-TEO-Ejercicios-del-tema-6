# FP1 - Teoría - Ejercicios del Tema 6

En estos ejercicios practicaremos los contenidos del tema (generadores, definiciones por comprensión, expresiones *lambda* y funciones de orden superior como `max`, `min`, `sorted`, `map`, `filter`, `all` o `any`, y paso de funciones como parámetros) trabajando con un dataset real: los resultados de todos los partidos internacionales de fútbol masculino jugados entre selecciones desde 1872 (`data/partidos.csv`).

El módulo `analisis_partidos.py` ya incluye:

* La definición del tipo `Partido` (`namedtuple`), con los campos `date`, `home_team`, `away_team`, `home_score`, `away_score`, `tournament`, `city`, `country` y `neutral`.
* La función de lectura de datos `lee_partidos`.
* Tres funciones auxiliares que te serán útiles en varios ejercicios:
    * `juega(partido, seleccion)`: devuelve `True` si la selección jugó el partido, ya sea como local o como visitante.
    * `goles_a_favor(partido, seleccion)`: devuelve los goles que marcó la selección en el partido.
    * `goles_en_contra(partido, seleccion)`: devuelve los goles que recibió la selección en el partido.

No es necesario que implementes ninguna de las anteriores. Tu tarea consiste en implementar las funciones de análisis que se describen a continuación y verificar su correcto funcionamiento utilizando el archivo de pruebas `analisis_partidos_test.py`. **Debes utilizar definiciones por comprensión (generadores) siempre que sea posible**.

Ten en cuenta que en el dataset el marcador de cada partido incluye la prórroga, pero no la tanda de penaltis. Por tanto, un partido decidido en los penaltis figura como un empate.

## Ejercicio 1: Obtención de torneos distintos

Implementa la función `obten_torneos`. Esta función recibe una lista de partidos y debe devolver un conjunto (`set`) con los nombres de todos los torneos que aparecen en dicha lista.

Prueba la función mediante la función de test `test_obten_torneos` en `analisis_partidos_test.py`.

## Ejercicio 2: Partido con más goles de un torneo

Implementa la función `busca_partido_con_mas_goles`. La función recibe la lista de partidos y el nombre de un torneo. Debe devolver el `Partido` de ese torneo en el que se marcaron más goles en total (sumando los goles de ambas selecciones).

* Si no hay ningún partido del torneo indicado, la función debe devolver `None`.

**Haz uso de la función predefinida `max` para resolver este ejercicio.** Pista: `max` admite un parámetro `default` con el valor que debe devolver si el iterable está vacío.

Prueba la función mediante la función de test `test_busca_partido_con_mas_goles` en `analisis_partidos_test.py`.

## Ejercicio 3: Últimos partidos de una selección

Implementa la función `busca_ultimos_partidos_de_seleccion`. Esta función recibe la lista de partidos y el nombre de una selección. Debe devolver una lista con los **5 últimos partidos** jugados por esa selección (como local o como visitante), ordenados cronológicamente por su fecha (`date`), del más antiguo al más reciente.

* Si la selección ha jugado menos de 5 partidos, se devolverán todos ellos.

**Haz uso de la función predefinida `sorted` para resolver este ejercicio.**

Prueba la función mediante la función de test `test_busca_ultimos_partidos_de_seleccion` en `analisis_partidos_test.py`.

## Ejercicio 4: Goles marcados por una selección (versión generador)

Implementa la función `calcula_goles_marcados`. Debe calcular el total de goles marcados por una selección en todos los partidos que ha jugado, tanto como local como visitante.

**Haz uso de la función predefinida `sum` junto con un generador para resolver este ejercicio.**

Prueba la función mediante la función de test `test_calcula_goles_marcados` en `analisis_partidos_test.py`.

## Ejercicio 5: Goles marcados por una selección (versión map/filter)

Implementa la función `calcula_goles_marcados_2`. El objetivo es el mismo que en el ejercicio anterior: calcular el total de goles marcados por una selección.

**Haz uso de la función predefinida `sum` junto con `map` y `filter` para resolver este ejercicio.**

Prueba la función mediante la función de test `test_calcula_goles_marcados_2` en `analisis_partidos_test.py`.

## Ejercicio 6: ¿Ganó todos sus partidos?

Implementa la función `ha_ganado_todos`. Esta función recibe la lista de partidos, el nombre de una selección, el nombre de un torneo y un año. Debe devolver `True` si la selección **ganó todos** los partidos que jugó en ese torneo durante ese año, y `False` en caso contrario. Recuerda que los empates (incluidos los partidos decididos en los penaltis) no son victorias.

* Si la selección no jugó ningún partido de ese torneo en ese año, la función devolverá `True`. ¿Sabrías explicar por qué es ese el comportamiento de `all` con un iterable vacío?

**Haz uso de la función predefinida `all` para resolver este ejercicio.**

Prueba la función mediante la función de test `test_ha_ganado_todos` en `analisis_partidos_test.py`.

## Ejercicio 7: Selección con más goles

Implementa la función `busca_seleccion_con_mas_goles`. Esta función debe calcular el total de goles marcados por **cada selección** en **todos** sus partidos (como local y como visitante) y devolver una tupla con el nombre de la selección que más goles ha marcado y dicho total.

* Si la lista de partidos está vacía, debe devolver `None`.
* Utiliza un diccionario (`dict` o `defaultdict`) para acumular los goles por selección, recorriendo la lista de partidos una sola vez.
* Utiliza `max` para buscar el item con mayor acumulado del diccionario anterior.

Prueba la función mediante la función de test `test_busca_seleccion_con_mas_goles` en `analisis_partidos_test.py`.

## Ejercicio 8: ¿Ha ganado alguna vez a un rival?

Implementa la función `ha_ganado_alguna_vez`. Esta función recibe la lista de partidos, el nombre de una selección y el nombre de otra selección rival. Debe devolver `True` si la selección ha ganado **al menos un** partido contra el rival, y `False` en caso contrario.

**Haz uso de la función predefinida `any` para resolver este ejercicio.**

Prueba la función mediante la función de test `test_ha_ganado_alguna_vez` en `analisis_partidos_test.py`.

## Ejercicio 9: Primera victoria de una selección

Implementa la función `busca_primera_victoria`. Esta función recibe la lista de partidos y el nombre de una selección. Debe devolver el primer partido (el de fecha más antigua) que ganó dicha selección.

* Si la selección no ha ganado ningún partido, la función debe devolver `None`.

**Haz uso de la función predefinida `min` para resolver este ejercicio.**

Prueba la función mediante la función de test `test_busca_primera_victoria` en `analisis_partidos_test.py`.

## Ejercicio 10: Mayores goleadas de una selección

Implementa la función `busca_mayores_goleadas`. Esta función recibe la lista de partidos, el nombre de una selección y un número entero `n` (con valor por defecto 5). Debe devolver una lista con las `n` victorias de la selección con mayor diferencia de goles, ordenadas de mayor a menor diferencia.

* Si dos partidos tienen la misma diferencia de goles, irá antes aquel en el que la selección marcó más goles (por ejemplo, un 9-1 va antes que un 8-0).
* Si persiste el empate, irá antes el partido más reciente.

**Haz uso de la función predefinida `sorted` con el parámetro `reverse`.** Pista: si la función que pasas en el parámetro `key` devuelve una tupla, las tuplas se comparan elemento a elemento, de manera que el segundo elemento sólo se tiene en cuenta cuando hay empate en el primero, y así sucesivamente.

Prueba la función mediante la función de test `test_busca_mayores_goleadas` en `analisis_partidos_test.py`.

## Ejercicio 11: Media de goles por edición de un torneo

Implementa la función `calcula_media_goles_por_edicion`. Esta función recibe la lista de partidos y el nombre de un torneo. Debe devolver un diccionario cuyas claves sean los años en los que se jugaron partidos del torneo, y cuyos valores sean la media de goles por partido de ese año.

Sigue estos pasos:
* Recorre la lista de partidos **una sola vez** y agrupa los partidos del torneo indicado por año, usando un `defaultdict` cuyas claves sean los años y cuyos valores sean listas con los partidos de ese año.
* Construye el diccionario resultado mediante un **diccionario por comprensión** que recorra los items del diccionario anterior. Para calcular la media de cada año, usa `sum` con un generador para obtener el total de goles, y divídelo entre el número de partidos de ese año.

Prueba la función mediante la función de test `test_calcula_media_goles_por_edicion` en `analisis_partidos_test.py`.

## Ejercicio 12: Partidos por país sede

Implementa la función `cuenta_partidos_por_pais_sede`. Esta función recibe la lista de partidos y el nombre de un torneo. Debe devolver un `Counter` con el número de partidos de ese torneo que se han jugado en cada país.

**Resuelve este ejercicio en una sola línea, construyendo el `Counter` directamente a partir de un generador**, sin utilizar bucles.

Prueba la función mediante la función de test `test_cuenta_partidos_por_pais_sede` en `analisis_partidos_test.py`.

## Ejercicio 13: Filtrado de partidos con una condición

Implementa la función `filtra_partidos`. Esta función recibe la lista de partidos y una **función** `condicion`, que a su vez recibe un `Partido` y devuelve un `bool`. Debe devolver una lista con los partidos para los que la función `condicion` devuelve `True`.

Por ejemplo, la llamada `filtra_partidos(partidos, lambda p: p.neutral)` devolverá los partidos jugados en campo neutral.

Resuelve este ejercicio sin utilizar la función predefinida `filter`, mediante una lista por comprensión.

Prueba la función mediante la función de test `test_filtra_partidos` en `analisis_partidos_test.py`. Observa en el test los distintos tipos de condiciones que se pasan a la función.

## Ejercicio 14: Aplicar una función a los partidos de una selección

Implementa la función `aplica_a_partidos_de_seleccion`. Esta función recibe la lista de partidos, el nombre de una selección y una **función** `funcion`, que a su vez recibe un `Partido` y el nombre de una selección. Debe devolver una lista con el resultado de aplicar `funcion` a cada partido jugado por la selección, en el mismo orden en que aparecen en la lista de partidos.

Por ejemplo, la llamada `aplica_a_partidos_de_seleccion(partidos, 'Spain', goles_a_favor)` devolverá una lista con los goles que marcó España en cada uno de sus partidos. Observa que la función `goles_a_favor` se pasa como parámetro **sin paréntesis**: no la estamos llamando, sino pasándola para que sea `aplica_a_partidos_de_seleccion` quien la llame.

Prueba la función mediante la función de test `test_aplica_a_partidos_de_seleccion` en `analisis_partidos_test.py`. Observa que en el test se pasan como parámetro tanto funciones definidas en el módulo como expresiones *lambda*.

## Para reflexionar: generadores y listas por comprensión

Observa el siguiente código:

```python
goles_espana = (goles_a_favor(p, 'Spain') for p in partidos if juega(p, 'Spain'))
total = sum(goles_espana)
maximo = max(goles_espana)
```

* ¿Qué ocurre al ejecutarlo? ¿Por qué?
* ¿Qué cambio mínimo habría que hacer para que funcione?
