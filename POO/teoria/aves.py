class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia < 10

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia < 50


class AnimalesAlados():  #generalizo lo que tienen en comun ambas clases
  def esta_feliz(self):
    return self.energia > 500

class Entrenador:
    """un entrenador tiene un equipo, y puede admitir nuevos miembros (animales alados) a su equipo"""
    def __init__(self, equipo):
      self.equipo = equipo

    def el_equipo(self):
      return self.equipo
    """son guetters, ambos hacen lo mismo"""

    def agregar_animal_alado(self, dragon):
      """este metodo toma un objeto, animal alado, que tendrá todos los atributos de esa clase"""
      self.equipo.append(dragon)

    def entrenar_dragon(self, dragon):
      for i in range(20):
        dragon.volar_en_circulos()
      dragon.comer_peces(3)
      """el entrenador entiende el mensaje entrenar dragon"""
    
    def entrenar_equipo(self):
      for dragon in self.equipo:
        self.entrenar_dragon(dragon)
    """lo digo que entrene a cada miembro de su equipo"""


pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador([roberta])