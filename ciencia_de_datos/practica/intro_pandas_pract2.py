import pandas as pd
# Ejercicio 1
# Escribí un programa que dado un diccionario cuyos valores sean listas de números cree un DataFrame y luego seleccione e 
# imprima las filas del DataFrame basado en un valor de una columna.

"""
Diccionario = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
# , y el valor es 4 en la columna 1.

df = pd.DataFrame(Diccionario)

print(df.loc[df[1] == 4]) """

# Ejercicio 2
# Escribí un programa que guarde en una lista una columna de un DataFrame.
personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";")
"""
def guardar_en_lista(nombre_columna):
    lista = []
    lista.append(personas[nombre_columna])
    print(lista)

guardar_en_lista("edad") """

# Ejercicio 3
# Realizá un programa que agregue datos a un DataFrame vacío.
"""
df = pd.DataFrame()

def agregar_datos(nombre_columna, contenido_filas):
    df[nombre_columna] = contenido_filas #el contenido debe ser una lista 
    print(df)

agregar_datos("Paises", ["Argentina", "Chile", "Uruguay", "Brasil"])
"""

# Ejercicio 4
# Escribí un programa que elimine las primeras n filas de un DataFrame. Pista: el DataFrame original no debe modificarse.
"""
def eliminar_filas(numero):
    nuevoDF = pd.DataFrame(personas.drop(personas.index[0:numero]))
    print(nuevoDF)

eliminar_filas(20000)"""

# Ejercicio 5
# Realizá un programa que verifique si una columna dada se encuentra presente en un DataFrame.
"""
def corroborar_columna(columna, DF):
    list = []
    for column in DF:
        list.append(column)
    if columna not in list:
        print("la columna no se encuentra en el DataFrame")
    else:
        print("la columna se encuentra en el DataFrame")

corroborar_columna("edad", personas)
"""

# Ejercicio 6
# Escribí un programa que dado dos diccionarios genere dos DataFrame y los una tanto en el eje de las columnas como en el 
# eje de las filas.
"""
dicc1 = {"A":["A1", "A2", "A3"], "B":["B1", "B2", "B3"], "C":["C1", "C2", "C3"]}
df1 = pd.DataFrame(dicc1)
dicc2 = {"D":["D1", "D2", "D3"], "E":["E1", "E2", "E3"], "F":["F1", "F2", "F3"]}
df2 = pd.DataFrame(dicc2)

df_final = pd.concat([df1, df2], axis=1)
print(df_final)"""

# Ejercicio 7
# Creá un programa que dado un diccionario y una lista añada está última al DataFrame generado a partir del diccionario.
"""
dicc = {"nombre":("cecilia", "carolina", "lucía", "andrea", "romina", "laura"), "edad":(15, 22, 40, 18, 30, 16), "altura":(1.6, 1.7, 1.65, 1.8, 1.58, 1.88)}
reside_en = ("caballito", "palermo", "retiro", "palermo", "belgrano", "once")

def crear_df(diccionario, lista, nombre_columna):
    DF = pd.DataFrame(diccionario)
    DF[nombre_columna] = lista
    print(DF)

crear_df(dicc, reside_en, "reside_en")
"""

# Ejercicio 8
# Realizá un programa que dado dos DataFrames genere otro que contenga solo las columnas en común.
"""
df1 = pd.DataFrame({"A":["A1", "A2", "A3"], "B":["B1", "B2", "B3"], "C":["C1", "C2", "C3"]})
df2 = pd.DataFrame({"A":"A4", "C":["C4", "C5"], "D":["D1", "D2"]})

nuevo_df = pd.DataFrame(pd.concat([df1, df2], join="inner"))
print(nuevo_df)
"""