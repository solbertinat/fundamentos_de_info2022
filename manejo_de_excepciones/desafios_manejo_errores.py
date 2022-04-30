# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
from ast import excepthandler
import cmath

a = 3
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
try: 
    sol1 = (-b-cmath.sqrt(d))/(2*a) 
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
except SyntaxError:
    print("hay un error")

#Desafio I - el error era un SyntxError, ubicado en la linea 15, luego de (d). 
#Desafio II
def mitades(numero):
    print(numero/2)
#Desafio III
#la funcion anterior no tiene ningun problema con la division por cero puesto que siempre divide por dos
#en una funcion donde hay dos parametros (numerador y divisor):
def division(num, div):
    try:
        return(num/div)
    except ZeroDivisionError:   
        print("no se puede dividir un numero por cero")
