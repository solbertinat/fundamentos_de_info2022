class AnimalesAlados():  #generalizo lo que tienen en comun ambas clases
  def esta_feliz(self):
    return self.energia > 500

class Golondrina(AnimalesAlados):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
    if self.energia <= 0:
      print("No puede volar")
      print(self.energia)
    else:
      print("tiene", self.energia, "de energia")
  
  def enEquilibrio (self):
    if(self.energia > 150 and self.energia < 300):
      print("esta en equilibrio")
    else:
      print("no esta en equilibrio")

  def esta_debil(self):
    return self.energia < 10

class Dragon(AnimalesAlados):     
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

class AvesNoVoladoras:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def correr_en_circulos(self):
    self.energia -= 25

class Entrenador:
    """un entrenador tiene un equipo, y puede admitir nuevos miembros (animales alados) a su equipo"""
    def __init__(self, equipo):
      self.equipo = equipo

    def el_equipo(self):
      return self.equipo
    """son guetters, ambos hacen lo mismo"""

    def agregar_animal_alado(self, animal_alado):
      """este metodo toma un objeto, animal alado, que tendrá todos los atributos de esa clase"""
      self.equipo.append(animal_alado)

    def entrenar_dragon(self, dragon):
      for i in range(20):
        dragon.volar_en_circulos()
      dragon.comer_peces(3)
      """el entrenador entiende el mensaje entrenar dragon"""
    
    def entrenar_golondrina(self, golondrina):
      for i in range(20):
        golondrina.volar_en_circulos()
      golondrina.comer_alpiste(50)
    
    def entrenar_equipo(self):
      for dragon in self.equipo:
        self.entrenar_dragon(dragon)
      for golondrina in self.equipo:
        self.entrenar_golondrina(golondrina)
    """lo digo que entrene a cada miembro de su equipo"""

    def entrenamiento_intensivo(self):
      for animal_alado in self.equipo:
        while animal_alado.esta_debil is not True:
          animal_alado.volar_en_circulos()
      
pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador([roberta])

hipo.agregar_animal_alado(pepita)
hipo.agregar_animal_alado(chimuelo)
hipo.entrenamiento_intensivo()

print(pepita.esta_debil())
print(chimuelo.energia)