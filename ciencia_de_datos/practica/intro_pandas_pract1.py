# Ejercicio 1
# Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.
# Series de muestra: 
# [3, 7, 12, 15, 21], [1, 4, 10, 14, 19]

"""import pandas as pd 

s1 = pd.Series([3, 7, 12, 15, 21], dtype= int)
s2 = pd.Series([1, 4, 10, 14, 19], dtype= int)

suma = s1 + s2
print(suma)

resta = s1 - s2
print(resta)

multiplicacion = s1 * s2
print(multiplicacion)

division = s1 / s2
print(division)"""

# Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.
# Series de muestra:
# [3, 7, 9, 14, 25], [1, 7, 10, 16, 19]

"""import pandas as pd

serie1 = pd.Series([3, 7, 9, 14, 25], dtype= int)
serie2 = pd.Series([1, 7, 10, 16, 19], dtype= int)

mayor1 = serie1 > serie2
print(mayor1)

mayor2 = serie1 < serie2
print(mayor2)

iguales = serie1 == serie2
print(iguales)"""

# Ejercicio 3
# Escribí un programa para convertir un diccionario a una serie de Pandas.
# Diccionario de muestra:
"""dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

import pandas as pd

print(pd.DataFrame([dict1]))"""

# Ejercicio 4
# Escribí un programa que dado un diccionario cuyos valores son listas de números, cree otro diccionario con las mismas 
# claves, pero donde los valores sean una lista de números donde se potencia un número por el siguiente, tomándolos de a 
# pares. Para ser más claros miremos este ejemplo donde si un diccionario es:

# dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
# el diccionario resultante debería ser:

# dict2 = {"a": [1, 25], "b": [16, 27]}
# Esto se obtiene al hacer 1 al cubo (el primer par de la lista "a"), y 5 al cuadrado, por un lado; y 4 al cuadrado y 3
#  al cubo por el otro. Se considera que la cantidad de elementos en las listas siempre es par, por lo que no habría que 
# hacer ninguna comprobación al respecto. Se puede usar el dict1 como diccionario de muestra, pero considerá que la lista 
# puede ser más grande. Por último hay que convertir este último diccionario en un DataFrame de Pandas.



# Ejercicio 5
# Realizá un programa para crear y mostrar un DataFrame a partir de un diccionario y de unas etiquetas (o labels).

# Muestra:

# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]



# Ejercicio 6
# Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.

# Muestra:

# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]




# Ejercicio 7
# Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.

# Muestra:

# datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

# labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]



# Ejercicio 8
# Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" del DataFrama anterior.




# Ejercicio 9
# Escribí un programa que dado el DataFrame anterior imprima los nombres en mayúscula y la longitud de los mismos en una nueva tabla.