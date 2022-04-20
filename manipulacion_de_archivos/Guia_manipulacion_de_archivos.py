#1 - Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con
# una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
# def no_p (archivo):
#     contador = 0
#     with open(archivo,'r') as mi_arch:
#         for linea in mi_arch:
#             if linea[0] != 'P':
#                 contador += 1
#     print(contador)

# no_p(r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\no_p.txt")

#2 - Escribí un programa que lea un archivo e imprima las primeras n líneas.
# import re
# archivo = (r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt")
# def primeras_lineas(n):
#     with open(archivo, 'r') as mi_arch:
#         contador = 0
#         while contador < n:
#             print(mi_arch.readline())
#             contador += 1

# primeras_lineas(3)

#3 - Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima
# las n últimas.
# import re
# archivo = (r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt")
# def ultimas_lineas(n):
#     with open(archivo, 'r') as mi_arch:
#         lista = mi_arch.readlines()
#         contador = (len(lista) - n)
#         while contador < len(lista):
#             print(lista[contador])
#             contador +=1

# ultimas_lineas(2)

#4 - Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
# import re
# def cuenta_palabras(archivo):
#     with open(archivo, 'r') as mi_arch:
#         palabras = " ".join(mi_arch.readlines())
#         cantidad_p = len(palabras.split(" "))
#         print(cantidad_p)

# cuenta_palabras(r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt")


#5 - Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y
# lo guarde en otro archivo.
# def remp_y_crear(archivo, nuevo_arch):
#     with open(archivo, 'r') as mi_arch:
#         for linea in mi_arch:
#             with open(nuevo_arch, 'w') as nuevo_a:
#                 nuevo_a.write("\n"+linea[0])

# remp_y_crear(r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt", r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\nuevo_archivo.txt")


#6 - Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
# import re
# arch_original = (r'C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo_2.txt') 
# otro_archivo = (r'C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\otro_archivo.txt')

# with open(arch_original, 'r') as archivo:
#     contenido = archivo.read()
#     copiar = re.findall("\n", contenido)
#     pegar = contenido.replace("\n", '')
#     with open(otro_archivo, 'w') as otro: 
#         otro.write(pegar)

#7 - Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir
# cuantos caracteres tiene.
# def palabra_larga(archivo):
#     with open(archivo, "r") as archivo:
#         dic = {}
#         lista = []
#         for linea in archivo:
#             lista.append(linea.strip("\n"))
#             contador = 0
#             while contador < len(lista):
#                 dic = {lista[contador] : len(lista[contador])} 
#                 largo = [len(lista[contador])]
#                 contador += 1
#         mas_larga = max(largo)
#         def devolver_clave(val):
#             for key, value in dic.items():
#                 if val == value:
#                     print(key)
#         print("la palabra mas larga es: ")
#         print(devolver_clave(mas_larga))
#         print("y contiene " + str(mas_larga) + " letras")
# palabra_larga(r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo_2.txt")

#8 - Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
# import re
# path1 = (r'C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt')
# path2 = (r'C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo_2.txt')
# path3 = (r'C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\guardar_aca.txt')
# with open(path1, "r") as archivo1:
#     copiar1 = archivo1.read()
#     texto1 = re.search(copiar1, copiar1).group()
#     with open(path2, "r") as archivo2:
#         copiar2 = archivo2.read()
#         texto2 = re.search(copiar2, copiar2).group()
#         with open(path3, "w") as guardar:
#             guardar.write(texto1)
#             guardar.write(texto2)

#9 - Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo.
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto
# a la cantidad total de palabras.
# def contador_de_palabras(archivo): 
#     frecuencias = dict() 
#     with open(archivo, 'r') as miArchivo: 
#         word_list = miArchivo.read().split() 
#         for palabra in word_list:
#             if palabra in frecuencias: 
#                 frecuencias[palabra] += 1
#             else: 
#                 frecuencias[palabra] = 1 
#         for word in frecuencias.keys(): 
#             frecuencias[word] = round(frecuencias[word] / len(word_list),3) #3 decimales 
#     print(frecuencias)

# contador_de_palabras(r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\fundamentos_de_info2022\manipulacion_de_archivos\archivo.txt")

#10 - Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una
# determinada carpeta.
"""consultar"""