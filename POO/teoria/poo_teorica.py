from aves import pepita, anastasia, roberta, chimuelo, hipo
#Desafio 1
#1 - Creá a la golondrina maria con 42 puntos de energía inicial
#esto esta en aves
#maria = Golondrina(42)

#2 - Creá al dragón chimuelo, con 200 dientes y 1000 de energía inicial
#esto esta en aves
#chimuleo = Dragon(200, 1000)

#3 - Definí el método esta_debil, que nos dice si nuestras "aves" tiene menos de 10 puntos de energía
# (golondrinas) o menos de 50 puntos de energía (dragones)
#esto va dentro de la clase golondirna en aves 
# def esta_debil(self):
#     return self.energia < 10
#esto va dentro de la clase dragon en aves 
# def esta_debil(self):
#    return self.energia < 50

#4 - Definí el método esta_feliz, que nos dice si nuestras "aves" tiene más de 500 puntos de energía 
# (sin importar de qué clase sean)
#esto va dentro de golondrinas y dragon, o crear otra clase que generalice: animales alados
# def esta_feliz(self):
#     return self.energia > 500

#5 - Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos 
# entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta 
# saciarse (3 peces)
# class Entrenador:
#     """un entrenador tiene un equipo, y puede admitir nuevos miembros (animales alados) a su equipo"""
#     def __init__(self, equipo):
#         self.equipo = equipo

#     def agregar_animal_alado(self, animal_alado):
#         """este metodo toma un objeto, animal alado, que tendrá todos los atributos de esa clase"""
#         self.equipo.append(animal_alado)

print(hipo)
print(hipo.equipo)
print(hipo.el_equipo())

        # def agregar_dragon(self, dragon):
        #     """este metodo toma un objeto, animal alado, que tendrá todos los atributos de esa clase"""
        #     self.equipo.append(dragon)

        # def entrenar_dragon(self, dragon):
        #     for i in range(20):
        #     dragon.volar_en_circulos()
        #     dragon.comer_peces(3)

        # def entrenar_equipo(self):
        #     for dragon in self.equipo:
        #     self.entrenar_dragon(dragon)

print(hipo.agregar_animal_alado(chimuelo))
print(hipo.equipo)
print("energia chimuelo energia", chimuelo.energia)
hipo.entrenar_dragon(chimuelo)
print("energia chimuelo despues", chimuelo.energia)

hipo.entrenar_equipo()
print("energia roberta despues", roberta.energia)
print("energia chimuelo despues", chimuelo.energia)

#crear algo generico que sea comer para unir --> cambiarlo para ser polimorfico