import pandas as pd
import seaborn as sns
import scipy.stats as sspip

# Desafío I y II: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Descargá a tu computadora la tabla de personas que conforman el Ministerio de Ciencia y Tecnología de 
# Argentina, en formato csv. Cargá (lee) la tabla a un DataFrame de Pandas de nombre personas ¿Qué forma te lectura de 
# archivos usarías? ¿Qué separación entre columnas posee el archivo? ¿Cómo te diste cuenta? 
# Averiguá para qué sirven los parámetro sep, index_col, nrows y header

# personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv")
# print(personas.head())
# # sep --> Sirve para separar los datos segun el caracter que le ponga
personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";")
# print(personas.head())
# # index_col --> Sirve para usar columnas como etiquetas de fila del DataFrame, ya sea como nombre de cadena o índice de columna.
# # en el siguiente ejemplo, pone a la segunda columna al principio  
# personas_icol = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", index_col=2)
# print(personas_icol.head())
# # nrows --> Número de filas de archivo a leer. Muestra las primeras n filas.
# personas_nrows = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", nrows=3)
# print(personas_nrows.head())

# .head() = previsualización de los datos
# Si se le pone un valor, imprimirá esa cantidad de filas 

# .info() = averiguar la información general de la tabla
# muestra los nombres de las columnas de la tabla y el tipo de datos que contiene cada una de ellas

# describe: de todas las columnas numericas me devuelve los parametros estadisitcos
# print(personas.describe())
# el problema con describe es que se aplica a todas las columnas con tipo de dato numerico, y en algunos no tiene 
# sentido ya que son identificadores.

# iloc: devuelve el elemento que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame
# df.loc[fila, columna] 
# imprime la interseccion (Celda). Si le paso fila e imprime todos los datos de las columnas para esa fila

# acceder los datos de una columna del DataFrame como una lista mediante el método tolist():
# df['columna'].tolist()

# métodos groupby() y count() = permiten contar sobre una columna la frecuencia de un dato/evento en particular. 

# Desafio III: Extrae la columna seniority_level y contá cuántas personas tenían expertice nivel B, C y D
# def nivel(level):
#     cont = 0
#     for id in personas[personas["persona_id"]]:
#         if personas.loc[id, "seniority_level"] == level:
#             cont +=1
#     print(cont)

# nivel("B")
"""resolver"""

# Desafio IV: ¿Qué resultados obtuviste en cada caso? Explicá qué hace cada linea de código
# print(personas["seniority_level"].count())
# cuenta la cantidad de filas en seniority level
# print(personas.groupby("seniority_level").count())
# agrupa en filas por los posibles contendios de las casillas de la columna seniority level, y muestra la cantidad de
# elementos en cada columna del dataframe que corresponden a cada seniority level. 
# print(personas.groupby("seniority_level")[["persona_id"]].count())
# lo mismo que el anterior, pero solo muestra lo que corresponde a la columna persona_id



# filtrado: personas de sexo 1 y menor de 40 años
# filtro = personas[(personas["sexo_id"] == 1) & (personas["edad"] < 40)]
# print(filtro)
# retorna una parte del dataframe original

# para convertir el tipo de dato: 
# personas["seniority_level"].astype("string")
# dataframe = dato inmutable --> no se modifica. Para cambiar el tipo de dato entonces tengo que reasignar o reescribir:
# personas["seniority_level"] = personas["seniority_level"].astype("string")

# calcular un dato sobre filtro de otras columnas:
# personas[(personas["sexo_id"] == 1) & (personas["edad"] < 40)]["producciones_ult_4_anios"].mean()

# metodo para filtrar en columnas de tipo str:
# personas[personas["seniority_level"].str.contains("A")]
# str.contains() sirve para encontrar substrings dentro de una columna 

# concatenar --> adherir dos dataframes
# categoria_a = personas[personas["seniority_level"].str.contains("A")]
# categoria_b = personas[personas["seniority_level"].str.contains("B")]
# pd.concat([categoria_a, categoria_b])
# me devuelve los seniority level A y despues los B





# Desafio V: Contá cuántas personas de 30 años ingresaron al ministerio en 2011 ¿Cuántas formas de hacer este cálculo 
# se te ocurren?

# Desafio VI: Descargala en formato csv y cargala en un nuevo DataFrame de nombre categorias  

# Desafío VII: Identificá si existen columnas en común con el DataFrame grande

# Desafío vIII: averiguá para qué sirve cada uno de los métodos y qué parámetros podés pasarseles. 
# ¡Esta información nos será útil para más adelante!
