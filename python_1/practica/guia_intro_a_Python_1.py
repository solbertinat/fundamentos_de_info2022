#1 - Escribir un programa que imprima la longitud de un string el cual se lee por teclado.
inp = input("ingrese una frase: ")
print(len(inp))

#2 - Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado 
# en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).
inp = input("ingrese una frase ")
if (len(inp) >= 6):
    print(str.upper(inp[4:6]))
else:
    print("su frase no tiene suficiente caracteres, por favor intente nuevamente")

#3 - Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.
inp = input('ingrese su nombre y apellido: ')
print('hola, ', inp)

#4 - Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
nombre = input("Ingrese su nombre ")
apellido1 = input("Ingrese su primer apellido ")
apellido2 = input("Ingrese su segundo apellido ")
print(str.upper(nombre[0]),str.upper(apellido1[0]),str.upper(apellido2[0]))

#5 - Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
numeros = input("Ingrese tres números (separados por un espacio) ")
lista = numeros.split(" ")
promedio = (int(lista[0]) + int(lista[1]) + int(lista[2]))/len(lista)
print(promedio)

#6 - Dada una cierta cantidad de minutos (ingresada por teclado) hacer un 
# programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
minutos = int(input("Ingrese una cantidad de minutos "))
print(minutos//60, " horas y ", (minutos%60), " minutos")

#7 - Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada 
# venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego 
# de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.
def dinero_fin_mes(sueldo_base, n):
    comision = (sueldo_base*0.1)
    contador = 0
    dinero_ventas = 0
    while contador < n:
        dinero_ventas = dinero_ventas + comision
        contador += 1
    print("total dinero por comisiones: $" + str(dinero_ventas))
    print("total dinero ganado en el mes: $" + str((dinero_ventas + sueldo_base)))

dinero_fin_mes(100, 4)

#8 - Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada 
# respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta 
# está en blanco no se le suma ni se le resta.
cant_preguntas = int(input("cantidad de preguntas: "))
rtas_correctas = int(input("respuestas correctas: "))
rtas_incorrectas = int(input("respuestas incorrectas: "))
nota = rtas_correctas*4 - rtas_incorrectas
print("la nota final del alumno es ", nota, "/", cant_preguntas*4)

