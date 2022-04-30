#1 - Dadas las siguientes clases responder: cuales son sus estados, cuales son sus interfaces, 
# ¿Comparten interfaz?, ¿Son polimórficas?
#clase Perro:
    #estados: alimento, caricias
    #interfaces: energia(), comer(), acariciar(), estaDebil() y pasear()
#clase Gato:
    #estados: alimento, caricias
    #interfaces: energia(), comer(), acariciar(), caricias() y estaDebil()
#comparten 4 interfaces: energia(), comer(), acariciar() y estaDebil(), pero tienen otras que
#son propias de cada clase (pasear() para Perro, y cariricas() para Gato)
#Si, son polimorficas, ya que comparten interfaces, pero deberia haber una tercer clase que 
# permita usar sus interfaces de manera intercambiable

#2 - Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina 
# está en equilibrio. Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.
# def enEquilibrio (self):
#     if(self.energia > 150 and self.energia < 300):
#       print("esta en equilibrio")
#     else:
#       print("no esta en equilibrio")

#3 - Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves 
# puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, 
# cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: 
# hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:
    #implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), 
    # realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba 
    # sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo 
    # tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().
    #comprobar el código que se escribió con esta secuencia:
    # definir un ornitólogo, dos golondrinas y dos gorriones,
    # inicializar las aves con valores conocidos,
    # decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
    # decirle al ornitólogo que realice su rutina sobre aves,
    # verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio 
        # el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
# from guia_POO_parte1 import Gorriones
# from aves import Golondrina

# class Ornitologo():
#     def __init__(self):
#         self.aves_en_estudio = []

#     def estudiarAve(self, Ave):
#         self.aves_en_estudio.append(Ave)

#     def avesEnEstudio(self):
#         print(self.aves_en_estudio)
    
#     def realizarRutinaSobreAves(self):
#         for Ave in self.aves_en_estudio:
#             Ave.comer(80)
#             Ave.volar(70)
#             Ave.comer(10)
    
#     def avesEnEquilibrio(self):
#         for Ave in self.aves_en_estudio:
#             print(Ave.enEquilibrio())

# ulises = Ornitologo()
# lila = Gorriones()
# pepita = Golondrina(100)
# maria = Golondrina(200)
# lolo = Gorriones()

# ulises.estudiarAve(lila)
# ulises.estudiarAve(maria)
# ulises.estudiarAve(lolo)
# ulises.avesEnEstudio() 
# """faltaria que devuelva el nombre, no el objeto"""
# ulises.realizarRutinaSobreAves()
# ulises.avesEnEquilibrio()
# pepita.enEquilibrio()


#4 - ...
# class MedioDeTransporte:
#   def __init__(self, combustible):
#     self.combustible = combustible
    
#   def cargar_combustible(self, cantidad):
#     self.combustible += cantidad
    
#   def entran_personas(self, personas):
#     return personas <= self.maximo_personas() 
  
# class Auto(MedioDeTransporte):
#   def recorrer(self, km):
#     self.combustible -= (km/2)
    
#   def maximo_personas(self):
#     return 5
  
# class Moto(MedioDeTransporte):
#   def recorrer(self, km):
#     self.combustible -= km
    
#   def maximo_personas(self):
#     return 2


