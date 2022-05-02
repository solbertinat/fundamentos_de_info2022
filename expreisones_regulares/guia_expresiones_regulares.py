#1 - Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
# Estos caracteres son a-z, A-Z y 0-9.
# import re
# string = input("Ingrese una cadena de caracteres:")
# patron = "[a-zA-Z0-9]"

# if re.search(patron, string) is not None:
#     print("hay al menos un caracter permitido")
# else:
#     print("no hay caracteres permititdos")

#2 - Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. 
# Estos caracteres son a-z, A-Z y 0-9.
# import re
# string = input("Ingrese una cadena de caracteres:")
# patron = "[a-zA-Z0-9]"

# if (len(string) == len(re.findall(patron, string))):
#     print("todos los caracteres son pemritidos")
# else:
#     print("al menos un caracter no es permitido")

#3 - Creá un programa que verifique las siguientes condiciones:
#       si un string dado tiene una h seguida de ninguna o más e.
#       si un string dado tiene una h seguida de una o más e.
# #       si un string dado tiene una h seguida de dos o tres e.
# import re
# string = input("ingrese una cadena de caracteres: ")

# patron1 = "(h(e*))"     #0 o mas coincidencias de e
# if re.search(patron1, string) is not None:
#     print("se cumple la condicion 1")
# else:
#     print("no se cumple la condicion 1")

# patron2 = "(h(e+))"     #una o mas ocurrencias de e
# if re.search(patron2, string) is not None:
#     print("se cumple la condicion 2")
# else:
#     print("no se cumple la condicion 2")

# patron3 = "(h(e{2,3}))"     #dos o tres veces de e
# if re.search(patron3, string) is not None:
#     print("se cumple la condicion 3")
# else:
#     print("no se cumple la condicion 3")

#4 -Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado 
# (el string no debe contener espacios).
# import re
# string = input("ingrese una cadena de caracteres: ")
# patron = "(\w*)_(\w*)"
# print(re.search(patron, string))

#5 - Escribí un programa que diga si un string empieza con un número específico.
# import re
# string = input("ingrese una cadena de caracteres: ")
# patron = "^3"

# if re.match(patron, string) is not None:
#     print("el string comienza con el numero 3")
# else:
#     print("el string no emieza con el numero 3")

#6 - Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
# import re
# strings = ["hola", "te", "hoy"]
# frase = "hola como te sentis hoy?"

# for palabra in strings:
#     patron = palabra
#     if re.search(patron, frase) is not None:
#         print("la palabra esta en la frase")
#     else:
#         print("la palabra no esta en la frase")

#7 - Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, 
# espacios y números.
# import re
# string = input("ingrese una frase: ")
# patron = "[a-zA-Z0-9(\s)]"
# coincidencias = []

# for caracter in string:
#     coincidencias.append(re.findall(patron, caracter))
    
# if len(coincidencias) == len(string):
#     print("todos los caracteres de la frase son o letras mayusculas, o letras minusculas, o numeros, o espacios")
# else:
#     print("al menos un caracter no es una letra mayuscula o minuscula, numero o espacio")

#8 - Escribí un programa que separe y devuelva los caracteres númericos de un string.
# import re
# string = input("escriba algo: ")
# patron = '\d'
# lista = []

# for caracter in string:
#     lista = re.findall(patron, string)

# print(lista)

#9 - Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
# import re
# string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
# patron = "-(.*?)-"

# print(re.findall(patron, string))

#10 - Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings 
# están delimitadas por los caracteres @ o &.
# import re
# string = "mi nombre es @sol@ @bertinat@, y soy estudiante de la carrera &administracion de empresas&"
# patron = "[@&](.*?)[@&]"
# lista = re.findall(patron, string)
# for substring in lista:
#     print(str(substring) + str(re.search(substring, string).span()))

#11 - Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string 
# empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
# import re
# lista_strings = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
# patron = "(P\w*)\s(P\w*)"

# for string in lista_strings:
#     coincidencia = re.search(patron, string)
#     if coincidencia is not None:
#         print(coincidencia.group())

#12 - Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la 
# barra vertical (|).
# import re
# string = "este documento se llama: expresiones_regulares.py"
# patron = "[\s_:]"
# print(re.sub(patron, "|", string))

#13 - Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re
def sustituir(str): 
    print(re.sub(r"\W", "_", str, 2))

sustituir("aeih$aes#vr6^^^")

#14 - Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
# import re
# string = "hola  mi nombre es    sol bertinat"
# patron = "[\s]"
# print(re.sub(patron, ";", string))

#15 - Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
mail = input("ingrese su email: ")
patron = "([a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+(@(gmail|hotmail|yahoo)\.com){1})" 
if re.search(patron, mail) is not None:
    print("la direccion de correo ingresada es valida")
else:
    print("la direccion de correo ingresada es invalida")

"""hacer que no sea valida si solo pongo por ej @gmail.com"""