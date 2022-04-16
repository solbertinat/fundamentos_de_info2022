#1 - Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con 
# una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
def no_p (archivo):
    contador = 0
    with open(archivo,'r') as mi_arch:
        for linea in mi_arch:
            if linea[0] != 'P':
                contador += 1
    print(contador)

no_p(r"no_p.txt")

#2 - Escribí un programa que lea un archivo e imprima las primeras n líneas.

# import re
# archivo = (r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\archivo.txt")
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
# archivo = (r"C:\Users\ulichtenbaum\Documents\Fundamentos_de_informatica\archivo.txt")
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

# cuenta_palabras(r"archivo.txt")

# texto = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso3.txt')

# with open(texto, 'r') as file:
#     texto = file.read()
#     palabras = texto.split()
#     print(len(palabras))
#     print(palabras)


#5 - Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y 
# lo guarde en otro archivo.
# def remp_y_crear(archivo, nuevo_arch):
#     with open(archivo, 'r') as mi_arch:
#         for linea in mi_arch:
#             with open(nuevo_arch, 'w') as nuevo_a:
#                 nuevo_a.write("\n"+linea[0])

# remp_y_crear(r"archivo.txt", r"nuevo_archivo.txt")            

# import re
# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso3.txt')
# path2 = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\nuevo_verso.txt')

# with open(path, 'r') as file:
#     texto = file.read()
#     with open(path2, 'w') as miarch:
#         texto_nuevo = texto.replace('e', 'e\n')
#         miarch.write(texto_nuevo)
         

#6 - Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
# def elimina_saltos(archivo, nuevo_archivo):
#     with open(archivo, 'r') as mi_archivo:
#         for linea in mi_archivo:
#             contador = 0
#             while contador < len(linea):
#                 with open(nuevo_archivo, 'w') as nuevo:
#                     nuevo.write(linea)

# elimina_saltos(r"archivo_2.txt", r"nuevo_archivo.txt")

# import re
# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso1.txt')
# path2 = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\sin_lineas.txt')
# with open(path, 'r') as file:
#     texto = file.read()
#     lista = re.findall("\n", texto)
#     texto_nuevo = texto.replace('\n', '')
#     with open(path2, 'w') as file:
#         file.write(texto_nuevo)

#7 - Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir 
# cuantos caracteres tiene.
# def palabra_larga(archivo):
#     with open(archivo, "r") as archivo:
#         for linea in archivo:
#             print(linea)

# palabra_larga(r"archivo_2.txt")


# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso_nuevo.txt')

# with open(path, 'r') as file:
#     texto = file.read()
#     print(texto)
#     palabras = texto.split()
#     palabras_sin_coma = []
#     for i in palabras:
#         palabra = i.strip(",") #porque hay palabras que tienen seguida una coma y hay que sacarla para que no cuente como caracter.
#         palabras_sin_coma.append(palabra)
#     print(palabras_sin_coma)
#     mas_larga = len(max(palabras_sin_coma, key=len))
#     print(mas_larga)
#     for i in palabras_sin_coma:
#         if len(i) == mas_larga:
#             print(str(i) + " es la palabras mas larga y tiene " + str(mas_larga) + " caracteres")


#8 - Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
# def mover_contenido(archivo, archivo_2, guardar_aca):
#     with open(archivo, "r") as archivo1:
#         with open(archivo_2, "r") as archivo2:
#             with open(guardar_aca, "w") as guardar_aqui:


# import re
# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso1.txt')
# path2 = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso3.txt')


# with open(path, 'r') as file:
#     with open(path2, 'r') as file2:
#         path3 = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\texto_total.txt')
#         with open(path3, 'w') as file3:
#             for linea in file:
#                 file3.write(linea)
#             for linea in file2:
#                 file3.write(linea)



#9 - Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la reación entre número de veces que aparece la palabra en cuestión con respecto 
# a la cantidad total de palabras.

# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\verso_nuevo.txt')


# with open(path, 'r') as file:
#     texto = file.read()
#     palabras = texto.split()
#     palabras_sin_coma = [] # Los caracteres que no contamos como palabras
#     for i in palabras:
#         palabra = i.strip(",")
#         palabras_sin_coma.append(palabra)
#     cantidad_palabras = len(palabras_sin_coma)
#     frecuencias = {}               
#     for palabra in palabras_sin_coma:
#         if palabra in frecuencias:
#             frecuencias[palabra] += 1
#         else:
#             frecuencias[palabra] = 1
#     for palabra in frecuencias:
#         frecuencia = frecuencias[palabra] / cantidad_palabras
#         print("La palabra: "+ str(palabra) + " ,tiene una frecuencia de " + str(frecuencia))

#10 - Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una 
# determinada carpeta.

# import glob
# path = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\archivo_final.txt')
# import glob
# import os 
# os.chdir(r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\Archivos de prueba')
# files_list = glob.glob("*.txt")
# with open(path, "a") as f:
#     for file in files_list:
#         with open(file, "r") as g:
#             f.write(g.read())

