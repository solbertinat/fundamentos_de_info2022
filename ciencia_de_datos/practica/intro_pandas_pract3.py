# Obtener las 10 personas con mayor edad y generar un nuevo DataFrame con la información de el id de la persona, el año, 
# su edad, el id de la categoría conicet y las producciones académicas de los últimos 4 años. 
# Unirlo con el DataFrame conicet y en base a ese generar una tabla con el id de la persona y la descripción de la 
# categoría en conicet. 
import pandas as pd

personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";")

top_10 = pd.DataFrame(personas.nlargest(10, ["edad"]))
top_10.drop(['sexo_id', 'maximo_grado_academico_id', 'disciplina_maximo_grado_academico_id', 'disciplina_titulo_grado_id', 'disciplina_experticia_id', 'tipo_personal_id', 'producciones_ult_anio',  'producciones_ult_2_anios', 'producciones_ult_3_anios', 'institucion_trabajo_id', 'seniority_level', 'categoria_incentivos', 'max_dedicacion_horaria_docente_id', 'institucion_cargo_docente_id', 'clase_cargo_docente_id', 'tipo_condicion_docente_id'], axis=1, inplace=True)

conicet = pd.read_csv(r"fundamentos_de_info2022\ciencia_de_datos\ref_categoria_conicet.csv", sep=";")

nuevo_df = pd.merge(top_10, conicet, on='categoria_conicet_id')
nuevo_df.drop(['anio', 'edad', 'producciones_ult_4_anios', 'categoria_conicet_id'], axis=1, inplace=True)

