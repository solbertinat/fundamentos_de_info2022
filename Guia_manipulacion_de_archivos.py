#1 - Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con 
# una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
'''def no_p (archivo):
    contador = 0
    with open(archivo,'r') as mi_arch:
        for linea in mi_arch:
            if linea[0] != 'P':
                contador += 1
    print(contador)

no_p(r"no_p.txt")'''

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

#5 - Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y 
# lo guarde en otro archivo.
# def remp_y_crear(archivo, nuevo_arch):
#     with open(archivo, 'r') as mi_arch:
#         for linea in mi_arch:
#             with open(nuevo_arch, 'w') as nuevo_a:
#                 nuevo_a.write("\n"+linea[0])

# remp_y_crear(r"archivo.txt", r"nuevo_archivo.txt")            

#6 - Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.


#7 - Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir 
# cuantos caracteres tiene.

#8 - Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

#9 - Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto 
# a la cantidad total de palabras.

#10 - Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una 
# determinada carpeta.