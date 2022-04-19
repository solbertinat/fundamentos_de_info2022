# 1 Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
#str = input("ingrese una frase o palabra: ")
#cap = str.capitalize()
#if (str == cap):
#    print("la primer letra es mayúscula")
#else:
#    print("la primer letra es minúscula")

#2 - Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además 
# informe si es par o impar (el 0 es un número par).
#numero = int(input("ingrese un numero: "))
#if (numero > 0):
#    print("es positivo")
#    if ((numero%2) > 0):
#        print("es impar")
#    elif ((numero%2) < 0):
#        print("es par") 
#elif (numero < 0):
#    print("es negativo")
#    if ((numero%2) > 0):
#        print("es impar")
#    elif ((numero%2) < 0):
#       print("es par")
#else:
#    print("es 0")
#    if ((numero%2) > 0):
#        print("es impar")
#    elif ((numero%2) < 0):
#        print("es par")
  

#3 - Escribí un programa que dado un número del 1 al 6, ingresado por teclado, 
# muestre cuál es el número que está en la cara opuesta de un dado. Si el número 
# es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
#num = int(input("ingrese un numero del 1 al 6: "))
#if (num < 6 or num > 1):
#    print("la cara opuesta del dado es " + (7-num))    
#else:
#    print("el numero ingresado no cumple con los requerimientos")

#4 - Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, 
# América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa 
# en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla. 
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por 
# la entrega de un paquete o, en su caso, el rechazo de la entrega.
#peso_paquete = int(input("ingrese el peso del paquete: "))
#lugar = input("ingrese la ubicacion de entrega: ")
#costos_ubicacion = {"America del Sur" : "10 usd", "America central" : "15 usd", "America del Norte" : "18 usd", "Europa" : "24 usd", "Asia" : "30 usd"}
#if (peso_paquete < 5):
#    print("cobro por entrega = " + costos_ubicacion[lugar])
#else:
#    print("su entrega fue rechazada: el peso del paquete excede el peso maximo de seguridad")

#5 - Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.
#numero_dia = int(input("ingrese un numero del 1 al 7: "))
#dias_semana = {1 : "Lunes", 2 : "Martes", 3 : "Miercoles", 4 : "Jueves", 5 : "Viernes", 6 : "Sabado", 7 : "Domingo"}
#if (numero_dia < 8 and numero_dia > 0):
#    print(dias_semana[numero_dia])
#else:
#    print("el numero ingresado no es un dia de la semana")

#6 - Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la 
# lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
# lista = [input(), input(), input(), input(), input()] 
# lista_inversa = [lista[4], lista[3], lista[2], lista[1], lista[0]]         
# print(lista_inversa)


#7 - Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se 
# introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.
'''numero = int(input("ingrese un numero: "))
lista = []
while numero >= 0:
    lista.append(numero)
    numero = int(input("ingrese un numero: "))
print(lista)   '''    


#8 - Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas 
# deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la 
# suma de los elementos de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene que ser
#la suma del primer elemento de la lista1 y el primero de la lista2)
''''Lista1 = [int(input("ingrese 5 numeros, uno por linea: ")), int(input()), int(input()), int(input()), int(input())]
Lista2 = [int(input("ingrese 5 numeros nuevamente: ")), int(input()), int(input()), int(input()), int(input())]
Lista3 = [Lista1[0]+Lista2[0], Lista1[1]+Lista2[1], Lista1[2]+Lista2[2], Lista1[3]+Lista2[3], Lista1[4]+Lista2[4]]
print(Lista3)'''

#9 - Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir 
# el nombre y la edad de cada alumno por teclado. El proceso de lectura de datos terminará cuando se 
# introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:
# - La edad máxima de todos los alumnos.
# - Los alumnos que tengan la edad máxima
''''dic = {}
nombre = input('ingrese el nombre del alumno: ')
edad = int(input('ingrese la edad del alumno: '))
while nombre != "*":
    dic = {nombre : edad}   
    nombre = input('ingrese el nombre del alumno: ')
    if nombre == "*":
        continue
    edad = int(input('ingrese la edad del alumno: '))
print(dic.values)
#print(dic.keys(max(dic.values)))  '''

    
# 10 - Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones 
# de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, 
# si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
''''cadena = "Aguacate"
freq = {}
for caracter in cadena: 
    if caracter not in freq:
        freq[caracter] = 0  # ==> caracter : 0
    freq[caracter] += 1
print(freq)'''

#11 - Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, 
# pero con el valor 0.
# cadena = "Aguacate"
# freq = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0, "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0, "0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
# for caracter in cadena: 
#     freq[caracter] += 1
# print(freq)

#12 - Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han
#  obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario
# cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
#  El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas 
# hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos 
# y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe
#  el programa tiene que dar un error.

''''dic = {}
cant_alumnos = int(input("ingrese el numero de alumnos que desea ingresar: "))
while cant_alumnos > 0:
    cant_alumnos -= 1
    alumne = input("nombre del alumno: ")
    if alumne in dic:
        print("ese alumno ya ha sido ingresado")
        continue
    nota = int(input("ingrese las notas, y temrine con un numero negativo: "))
    lista_notas = []
    while nota >= 0:
        lista_notas.append(nota)
        nota = int(input("ingrese un la nota: "))
    dic = {alumne : lista_notas}  
    prom_alum = sum(lista_notas) / len(lista_notas)
    lista_final = {alumne : prom_alum}
print(lista_final)'''    

#13 - Creá un programa que pida dos número enteros 
# al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
# n1 = int(input("ingrese un numero entero: "))
# n2 = int(input('ingrese otro numero entero: '))

# def esMultiplo(n1, n2):
#     if (n1%n2 == 0):
#         print(str(n2) + " es múltiplo de " + str(n1))
#     if (n2%n1 == 0):
#         print(str(n1) + " es múltiplo de " + str(n2))
#     if ((n2%n1 != 0) and (n1%n2 != 0)):
#         print("Los números ingresados no son múltiplos entre sí")

# esMultiplo(n1, n2)

#14 - Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
# mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.

def temp_media (maxima, minima):
    media = (int(maxima)+int(minima))/2
    print("la temperatura media es ", media, " grados")

dias = int(input("ingrese los dias que se vayan a introducir: "))
contador = 0
while contador < dias:
    max = input("ingrese la temperatura maxima: ")
    min = input("ingrese la temperatura minima: ")
    temp_media(max, min)
    contador +=1

#15 - 