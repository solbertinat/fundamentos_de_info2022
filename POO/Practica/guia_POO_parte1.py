#1 - Dada la siguiente clase, identificá la interfaz y el estado de la misma
#interfaz: los mensajes que puede entender son energia(), comer(), acariciar() y estarDebil()
#estado: los atributos son alimento y caricias

#2 - Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera 
# que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.
# def volar(self, kms):
#     self.energia -= 10 + kms
#     if self.energia <= 0:
#       print("No puede volar")
#       print(self.energia)
#     else:
#       print("tiene", self.energia, "de energia")

#3 - Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que 
# le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje 
# de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.
# class Notebook:
#     def __init__(self, precio, modelo, marca):
#         self.precio = precio
#         self.modelo = modelo
#         self.marca = marca
    
#     def aplicar_dto(self, descuento):
#         self.precio -= self.precio*(descuento/100)
#         print("el valor final es: ", self.precio)

# apple = 1
# Macbook_air = Notebook(5000, 1, 10)
# print(Macbook_air.aplicar_dto(15))

#4 - Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor 
# que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone
# en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
# class Contador:
#     def __init__(self, valor):
#         self.valor = valor
 
#     def inc(self):
#         self.valor += 1
    
#     def dis(self):
#         self.valor -= 1

#     def reset(self):
#         self.valor == 0

#     def valorActual(self):
#         print(self.valor)

#     def valorNuevo(self, nuevoValor):
#         self.valor = nuevoValor
    
# contador = Contador(10)
# contador.inc() #11
# contador.inc() #12
# contador.dis() #11
# contador.inc() #12
# contador.valorActual() #12
# contador.valorNuevo(27)
# contador.dis() #26
# contador.dis() #25
# contador.valorActual() #25

#5 - Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando 
# que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" 
# o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando
# es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior 
# debería ser "disminución".
# class Contador:
#     def __init__(self, valor):
#         self.valor = valor
#         self.comando = ""
    
#     def inc(self):
#         self.valor += 1
#         self.comando = "incremento"
    
#     def dis(self):
#         self.valor -= 1
#         self.comando = "disminucion"

#     def reset(self):
#         self.valor == 0
#         self.comando = "reset"

#     def valorActual(self):
#         print(self.valor)

#     def valorNuevo(self, nuevoValor):
#         self.valor = nuevoValor
#         self.comando = "actualizacion"

#     def ultimoComando (self):
#         print(self.comando)

#6 - Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes: cargar(numero), sumar(numero), restar(numero), 
# multiplicar(numero) y valorActual()
# class Calculadora:
#     def __init__(self):
#         self.numero = 0

#     def cargar(self, carga):
#         self.numero = carga

#     def sumar(self, suma):
#         self.numero += suma

#     def restar(self, resta):
#         self.numero -= resta

#     def multiplicar(self, multiplicacion):
#         self.numero *= multiplicacion
    
#     def valorActual(self):
#         print(self.numero)

# calculadora = Calculadora()
# calculadora.cargar(0)
# calculadora.sumar(4)
# calculadora.multiplicar(5)
# calculadora.restar(8)
# calculadora.multiplicar(2)
# calculadora.valorActual() #24

#7 - Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como 
# CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El 
# CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
# por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando 
# solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la 
# misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los 
# coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.
class Gorriones:
    def __init__ (self):
        self.gramos = 0
        self.kms = 0
        self.vuelos = []
        self.comidas = []

    def volar(self, kms):
        self.kms += kms
        self.vuelos.append(kms)

    def comer(self, gramos):
        self.gramos += gramos
        self.comidas.append(gramos)

    def CSS(self):
        if self.gramos <= 0:
            return None
        else:
            return self.kms/self.gramos

    def CSSP(self):
        if self.gramos <= 0:
            return None
        else:
            return int(max(self.vuelos))/int(max(self.comidas))

    def CSSV(self):
        if self.gramos <= 0:
            return None
        else:
            return len(self.vuelos)/len(self.comidas)
    
    def enEquilibrio(self):
        if(self.CSS() > 0,5 and self.CSS() < 2):
            return True
        else:
            return False

# lila = Gorriones()
# lila.comer(35)
# lila.volar(80)
# lila.comer(70)
# lila.volar(120)
# print(lila.CSS())
# print(lila.CSSP())
# print(lila.CSSV())
# print(lila.enEquilibrio())