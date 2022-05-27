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
# personas_sep = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";")
# print(personas_sep.head())
# # index_col --> Sirve para usar columnas como etiquetas de fila del DataFrame, ya sea como nombre de cadena o índice de columna.
# # en el siguiente ejemplo, pone a la segunda columna al principio  
# personas_icol = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", index_col=2)
# print(personas_icol.head())
# # nrows --> Número de filas de archivo a leer. Muestra las primeras n filas.
# personas_nrows = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", nrows=3)
# print(personas_nrows.head())


