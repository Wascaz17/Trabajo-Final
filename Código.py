
# JSON
import json, pygame, random

archivo_partida = "Partida.json"
class Criatura:

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo = ''):

    #Etsadisticas de la criatura no numericas y estados base
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.Frase = ""
    
    self.vivo = True
    self.cansado = False

    #Etsadisticas numericas base de la criatura definidas al crearla
    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    #Etsadisticas de la criatura que dependen de la subclase
    self.cardio = 0.6
    self.escalador_vida = 0.2
    self.escalador_ataque = 0.25
    self.escalador_estamina = 0.1
    self.escalador_velocidad = 0.05
    self.escalador_escudo = 0.01
    self.clase = ''
    
    #Etsadisticas finales de la criatura tras el calculo de las stats base
    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidadMax = self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel - 1/self.escudo_base)
    self.tamaño = (10 + (self.nivel * 0.1))
    self.color = (133,108,34)

  # Metodo para poder ver las stats de una criatura en cualquier momento
  def muestra_stats(self):
    Stats = f"|STATS| ❤️{round(self.vida,1)} 🗡️{round(self.ataque,1)} 🟢{round(self.estamina,1)} 🛡️{round(self.escudo,1)} 💨{round(self.velocidad,1)} 💥{round(self.potencial,1)} "
    self.Stats = Stats

  # Metodo dunder para mostrar informacion de la criatura
  def __str__(self):

    # Lista de tipos (de momento meramente estetico)
    tipos = ["🔥", "💧", "🌿", "⚡", "🪨", "❄️", "👊", "🔮", "🪽", "🫧"]

    if self.tipo == "Fuego":
      tipo_emoji = tipos[0]

    elif self.tipo == "Agua":
      tipo_emoji = tipos[1]

    elif self.tipo == "Planta":
      tipo_emoji = tipos[2]

    elif self.tipo == "Electrico":
      tipo_emoji = tipos[3]

    elif self.tipo == "Roca":
      tipo_emoji = tipos[4]

    elif self.tipo == "Hielo":
      tipo_emoji = tipos[5]

    elif self.tipo == "Lucha":
      tipo_emoji = tipos[6]

    elif self.tipo == "Magia":
      tipo_emoji = tipos[7]

    elif self.tipo == "Volador":
      tipo_emoji = tipos[8]

    elif self.tipo == "Veneno":
      tipo_emoji = tipos[9]

    else:
      tipo_emoji = "❓"

    # Lista de emojis para representar graficamente el nivel de una criatura y poder hacerte una idea rapida de lo duerte que es
    rangos = ["🥚", "💩", "👺", "😈", "💪", "🔱", "🧿", "🗿", "💎", "🐐", "👑"]

    if self.nivel < 5:
      rango = rangos[0]

    elif self.nivel < 10:
      rango = rangos[1]

    elif self.nivel < 20:
      rango = rangos[2]

    elif self.nivel < 30:
      rango = rangos[3]

    elif self.nivel < 40:
      rango = rangos[4]

    elif self.nivel < 50:
      rango = rangos[5]

    elif self.nivel < 60:
      rango = rangos[6]

    elif self.nivel < 70:
      rango = rangos[7]

    elif self.nivel < 80:
      rango = rangos[8]

    elif self.nivel < 90:
      rango = rangos[9]

    else:
      rango = rangos[10]

    logos = ["❔", "🐲", "🧌", "🧚🏼"]

    if self.clase == "dragon":
      logo = logos[1]

    elif self.clase == "ogro":
      logo = logos[2]

    elif self.clase == "hada":
      logo = logos[3]

    else:
      logo = logos[0]

    # Fases que representan la evolucion de la criatura, parecidas al juego Invizimals 
    fases = ["Chiqui", "", "Maxi"]

    if self.nivel < 30:
      fase = fases[0]

    elif self.nivel < 60:
      fase = fases[1]

    elif self.nivel < 90:
      fase = fases[2]

    else:
      fase = fases[2]

    # Varias variables para de representar mas adelante informacion de la criatura relevante
    self.nombreCompleto = f"{fase}{self.nombre}" 

    self.Banner = f"{logo} {self.nombreCompleto} ({tipo_emoji}) [N.{self.nivel}{rango}]"

    self.muestra_stats()

    return f"{self.Banner} {self.Stats}"
  
  # Frase que diran las criaturas antes de comenzar una batalla, al estilo Mortal Kombat, que varian segun la subclase
  def saludo(self):
    self.Frase = "[👋] Hola"
    print(self.Frase)

  # Metodo para calcular el daño que provoca una criatura, que tiene un porcentaje bonus dependiente de un valor aleatorio y su potencial, una mezcla de las IVs y Daño Especial de POkemon
  def daño(self):
    return self.ataque * (1 + (self.potencial * random.uniform(0, 0.10))) # Usare a lo largo de este codigo random.uniform() para poder poner rangos distintos de (0, 1)

  # Metodo para que se informe cuando una criatura muere
  def muerte(self):
    self.vivo = False
    self.vida = 0
    self.Frase = f"[☠️] {self.nombreCompleto} la ha palmado... RIP 💀"
    print(self.Frase)

  # Metodo necesario para que al subir de nivel, cambien las estadisticas
  def recalcular_stats(self):

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.vivo = True
    self.cansado = False
    return self

  # Metodo dunder paar subir de nivel 
  def __mul__(self, subida):
    incremento = int(subida) # El nivel es discreto, por lo que debe ser un entero
    self.nivel += incremento
    self.recalcular_stats()
    
    # El escudo maximo no debe llegar a 100, porque si no la criatura seria invulnerable al tener un 100% de negacion de daño
    if self.escudo > 95:
      self.escudo = 95
    if self.nivel > 100:
      self.nivel = 100
    self.Frase = f"\n[✨] {self.nombreCompleto} sube {incremento} niveles y ahora es [N.{self.nivel}]"
    print(self.Frase)

    print(f"  Nuevas {self.Stats}") ####volver aquí a ver lo de varios mensajes
    return self

  
  # Metodo al que llamar cusando una criatura gane una batalla, y que ademas suba un nivel al hacerlo
  def victoria(self):
    self.Frase = f"\n[🏆] {self.nombreCompleto} GANA LA BATALLA 🎉"
    print(self.Frase)
    self * 1
    self.recalcular_stats()
    return self 
  
  # Metodo dunder para poder definir el ataque de una criatura a otra
  def __sub__(self, enemigo):  

    if self.vivo == False:
      self.Frase = f"\n[☠️] {self.nombreCompleto} no puede atacar porque esta muerto."
      print(self.Frase)
      return self, enemigo # En este codigo habra varios metodos con returns necesarios para evitar errores como que no se actualice la vida de una criatura

    if self.cansado:
      self.Frase = f"\n[🥵] {self.nombreCompleto} esta demasiado cansado para atacar"
      print(self.Frase)
      return self, enemigo

    if enemigo.vivo == False:
      self.Frase = f"\n[😫] {enemigo.nombreCompleto} ya esta muerto, {self.nombreCompleto} respeta su cadaver"
      print(self.Frase)
      return self, enemigo

    # Calculo del daño real del ataque y definicion del ataque
    daño_base = self.daño()
    daño_efectivo = daño_base * (1 - (enemigo.escudo / 100))
    enemigo.vida -= daño_efectivo

    # Varias condiciones necesarias para evitar cosas como vida negativa
    if self.vida <= 0:
      self.vida = 0  
      self.vivo = False

    if self.estamina <= 0:
      self.estamina = 0
      self.cansado = True

    else:
      self.cansado = False

    if enemigo.vida <= 0:
      enemigo.vida = 0

    # Calculo del coste energetico de un ataque
    self.estamina -= 0.7 * (self.estamina_base * (1 + self.escalador_estamina * self.nivel) * (20/100) * (self.cardio) ** -1)
    self.Frase = f"\n[💢] {self.nombreCompleto} ataca a {enemigo.nombreCompleto} y hace -{round(daño_efectivo,1)}❤️"
    print(self.Frase)

    if enemigo.vida <= 0:
      enemigo.muerte()
      self.victoria()

      return self, enemigo

    if self.estamina <= 0:
      self.cansado = True
      self.Frase = f"[🥵] {self.nombreCompleto} se ha quedado reventao tras el ataque y debe descansar"
      print(self.Frase)

    if self.escudo > 85:
      self.escudo = 85

    if enemigo.escudo > 90:
      enemigo.escudo = 90

    return self, enemigo


  # Metodo para que una criatura se cure vida (y/o estanima en alguna subclase)
  def __add__(self, cantidad):
    if self.escudo > 85:
      self.escudo = 85

    if self.vivo:
      cantidad_estamina = cantidad * 0.1
      self.vida += cantidad
      self.estamina += cantidad_estamina
      print(self.Frase)

      # Como self.vida es la vida en cualquier momento de la criatura, la vida maxima es la vida calculada, lo mismo con cualquier stat. Por eso tengo que poner que tras recuperar stats, solo pueda llegar al maximo
      if self.vida >= (self.vidaMax):
        self.vida = (self.vidaMax)

      self.Frase = f"\n[💖] {self.nombreCompleto} se cura +{round(cantidad,1)}❤️\n[💚] y recupera +{round(cantidad_estamina,1)}🟢"
      if self.estamina > self.estaminaMax:
        self.estamina = self.estaminaMax
    
    if self.estamina > 0:
     self.cansado = False

    return self
  
class Dragon(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Fuego'): # Por defecto, los dragones son tipo fuego
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False   

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    # Varias de estas variables son diferentes para cada clase, y estan ajustadas en base a lo que me parece balanceado, pero puede que clase dragon haya que nerfearla si reciclo parte de este codigo para el trabajo final
    self.escalador_vida = 0.35   
    self.escalador_ataque = 0.29  
    self.escalador_estamina = 0.08 
    self.escalador_velocidad = 0.08
    self.escalador_escudo = 0.09 

    self.clase = "dragon"
    self.cardio = 0.6

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (10 + (self.nivel * 0.1))

    self.color = (133,48,34)

  def __sub__(self, enemigo):
    
    if self.vivo and enemigo.vivo:
      self.estamina += 0.10 * self.estaminaMax

      if self.estamina > self.estaminaMax:
        self.estamina = self.estaminaMax
      if self.estamina > self.estaminaMax: 
        self.cansado = False

      Criatura.__sub__(self, enemigo)
      print(self.Frase)
    return self, enemigo

  def saludo(self):
    self.Frase = f"🐲 De las llamas naci y en cenizas te convertire"
    print(self.Frase) # Suena a algo que un dragon diria, pero igual hace falta cambiarlo porque no todo dragon escupe fuego, si hay uno tipo hielo por ejemplo

class Ogro(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Roca'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False
    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    self.escalador_vida = 0.26   
    self.escalador_ataque = 0.35  
    self.escalador_estamina = 0.17 
    self.escalador_velocidad = 0.05
    self.escalador_escudo = 0.07  

    self.clase = "ogro"
    self.cardio = 0.5
  
    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (10 + (self.nivel * 0.1))

    self.color = (102,133,34)

  def __sub__(self, enemigo):

    # Vamos a hacer que una de las peculiaridades de los ogros sea que se puedan enfadar y asi mejorar sus atributos durante una ronda
    enfado = random.uniform(0,0.6)

    # Enfado es un numero que representa lo enfadado que esta el ogro
    if enfado > 0.45 or self.vida <= 0.25 * (self.vidaMax): # Que se pueda enfadar aleatoriamente, pero que siempre se enfade si llega a menos de un 25% de su vida maxima
      print(f"[😡] {self.nombreCompleto} se ha cabreado") ####volver aqui

      # Atacar enfadado hace mas daño pero a cambio le cuesta parte de su estamina en el momento, y cuanto mas enfadado mas daño hace pero tambien le resta mas estamina
      daño_base = self.daño()
      daño_enfadado = daño_base * (1 - (enemigo.escudo / 100)) * (1 + enfado * 1/2)
      enemigo.vida -= daño_enfadado
      self.estamina -= enfado * 0.5 * self.estamina  
      self.Frase = f"\n[💢] {self.nombreCompleto} se cabrea y ataca a {enemigo.nombreCompleto} y hace -{round(daño_enfadado,1)}❤️" 
    Criatura.__sub__(self, enemigo)

    # Los ogros no pueden atacar si su estamina es menor que un 20% de su maximo
    if self.estamina <= 0.15 * (self.estamina_base * (1 + self.escalador_estamina * self.nivel)): 
      self.cansado = True

    return self, enemigo


  # Otra cosa diferente de los ogros es que el + les recupera la estamina (para balancear que gastan mas al atacar enfadados y que se cansan al 20% de su estamina) pero a cambio pierden vida en el proceso
  def __add__(self, cantidad):

    if self.vivo:
      cantidad_vida = cantidad * 0.3
      cantidad_estamina = cantidad
      self.vida += -(cantidad_vida)
      self.estamina += cantidad_estamina

      if self.vida >= (self.vidaMax):

        self.vida = (self.vidaMax)

      if self.estamina >= (self.estamina_base * (1 + self.escalador_estamina * self.nivel)):
        self.estamina = (self.estamina_base * (1 + self.escalador_estamina * self.nivel))      
    
      self.Frase = f"\n[🩸] {self.nombreCompleto} sacrifica -{round(cantidad_vida,1)}❤️ y \n[💚] {self.nombreCompleto} recupera +{round(cantidad_estamina,1)}🟢"

    return self
  
  # Me he inventado estas palabras, pero suena a como creo que hablaria un ogro
  def saludo(self):
    self.Frase = "🧌 Paluka mastola goltopo su..."
    print(self.Frase)

class Hada(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Magia'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    self.escalador_vida = 0.27   
    self.escalador_ataque = 0.30  
    self.escalador_estamina = 0.08 
    self.escalador_velocidad = 0.37
    self.escalador_escudo = 0.06  

    self.clase = "hada"
    self.cardio = 0.9

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (10 + (self.nivel * 0.1))

    self.color = (133,34,100)

  # Las hadas, para compensar que suelen tener menos vida y estamina, el + les sube estamina tambien
  def __add__(self, cantidad):

    if self.vivo:
      self.vida += cantidad * 4
      self.estamina += cantidad * 0.5
      cantidad_estamina = cantidad * 0.5
      self.Frase = f"\n[💖] {self.nombreCompleto} se cura +{round(cantidad,1)}❤️\n[💚] y recupera +{round(cantidad_estamina,1)}🟢"
      if self.estamina > self.estaminaMax:
        self.estamina = self.estaminaMax
      if self.vida > self.vidaMax:
        self.vida = self.vidaMax
      

    return self

  def saludo(self):
    self.Frase = "🧚🏻‍♀️ Me gustaria volver a mi bosque antes de la hora del te"
    print(self.Frase)

class Golem(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Roca'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    self.escalador_vida = 0.10
    self.escalador_ataque = 0.26
    self.escalador_estamina = 0.12
    self.escalador_velocidad = 0.02
    self.escalador_escudo = 0.18

    self.clase = "golem"
    self.cardio = 0.3

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (12 + (self.nivel * 0.12))

    self.color = (90, 100, 90)

  def __add__(self, cantidad):
    if self.vivo:

      self.vida += cantidad * 0.1
      self.escudo += 3

      if self.vida > self.vidaMax:
          self.vida = self.vidaMax

      if self.escudo > 90:
          self.escudo = 90

      self.Frase = f"\n[💖] {self.nombreCompleto} se cura +{round(cantidad * 0.1,1)}❤️ y endurece +3🛡️"
    return self


  def saludo(self):
    self.Frase = "🗿 ..."
    print(self.Frase)

class Chupasangre(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Veneno'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    self.escalador_vida = 0.24
    self.escalador_ataque = 0.33
    self.escalador_estamina = 0.10
    self.escalador_velocidad = 0.14
    self.escalador_escudo = 0.05

    self.clase = "chupasangre"
    self.cardio = 0.95

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (10 + (self.nivel * 0.1))

    self.color = (120, 30, 40)

  def __sub__(self, enemigo):
    Criatura.__sub__(self, enemigo)

    if self.vivo and enemigo.vivo:
      
      robo = 0.05 * enemigo.vidaMax
      enemigo.vida -= robo
      self.vida += robo
      if self.vida > self.vidaMax:
        self.vida = self.vidaMax
      self.Frase = f"[🩸] {self.nombreCompleto} absorbe +{round(robo,1)}❤️"
      print(self.Frase)

    return self, enemigo

  def saludo(self):
    self.Frase = f"Chupar es mi pasion"
    print(self.Frase)

class Pez(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Agua'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    self.escalador_vida = 0.22
    self.escalador_ataque = 0.28
    self.escalador_estamina = 0.20
    self.escalador_velocidad = 0.25
    self.escalador_escudo = 0.04

    self.clase = "pez"
    self.cardio = 1.2

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (8 + (self.nivel * 0.08))

    self.color = (20, 130, 120)

  def __sub__(self, enemigo):
    # Reduce menos estamina por ataque
    if enemigo.estamina >= enemigo.estaminaMax * 0.2:
      enemigo.estamina -= enemigo.estaminaMax * 0.4
    Criatura.__sub__(self, enemigo)
    return self, enemigo

  def saludo(self):
    self.Frase = f"🐠 gluglu glu... glu"
    print(self.Frase)

class Bombastico(Criatura):

  def __init__(self, Nombre, Nivel, Vida_base, Ataque_base, Estamina_base, Velocidad_base, Escudo_base, Potencial, Tipo='Fuego'):
    self.nombre = Nombre
    self.tipo = Tipo
    self.nivel = Nivel
    self.potencial = Potencial
    self.vivo = True
    self.cansado = False

    self.vida_base = Vida_base
    self.ataque_base = Ataque_base
    self.estamina_base = Estamina_base
    self.velocidad_base = Velocidad_base
    self.escudo_base = Escudo_base

    # Escaladores pensados para un atacante arriesgado
    self.escalador_vida = 0.25 
    self.escalador_ataque = 0.45
    self.escalador_estamina = 0.18
    self.escalador_velocidad = 0.05
    self.escalador_escudo = 0.05   

    self.clase = "bombastico"
    self.cardio = 0.8

    self.vidaMax = self.vida = self.vida_base * (1 + self.escalador_vida * self.nivel)
    self.ataqueMax = self.ataque = self.ataque_base * (1 + self.escalador_ataque * self.nivel - 1/self.ataque_base)
    self.estaminaMax = self.estamina = self.estamina_base * (1 + self.escalador_estamina * self.nivel)
    self.velocidad = self.velocidad_base * (1 + self.escalador_velocidad * self.nivel)
    self.escudo = self.escudo_base * (1 + self.escalador_escudo * self.nivel)
    self.tamaño = (12 + (self.nivel * 0.1))

    self.color = (255, 100, 0)

  def __sub__(self, enemigo):

    daño_bomba = self.ataque * random.uniform(1.2, 1.7) * (1 - (enemigo.escudo / 100)) 
    enemigo.vida -= daño_bomba
    # Autodaño
    self.vida -= random.uniform(0.15, 0.35) * self.vidaMax

    self.Frase = f"[💥] {self.nombreCompleto} explota sobre {enemigo.nombreCompleto} haciendo -{round(daño_bomba,1)}❤️ pero pierde vida"
    print(self.Frase)
    Criatura.__sub__(self, enemigo)
    return self, enemigo

  def saludo(self):
    self.Frase = f"💣 ¡EXPLOTACION, DE CUALQUIER TIPO!"
    print(self.Frase)

# Lista de criaturas nivel 100 (usar en modo vresus)
CriaturaVersus1 = Dragon("Draconio", 100, 240, 45, 45, 35, 5, 4)
CriaturaVersus2 = Pez("Pececito", 100, 180, 40, 60, 50, 3, 4)
CriaturaVersus3 = Ogro("Paco", 100, 200, 50, 40, 30, 4, 4)
CriaturaVersus4 = Bombastico("Bum", 100, 160, 70, 30, 25, 3, 4)
CriaturaVersus5 = Hada("Aurora", 100, 120, 35, 55, 45, 2, 4)
CriaturaVersus6 = Chupasangre("Succionio", 100, 200, 40, 50, 40, 2, 4)
CriaturaVersus7 = Golem("Rocky", 100, 250, 30, 40, 30, 7, 4)
CriaturaVersus8 = Criatura("Random", 100, 220, 60, 50, 40, 4, 4)

# Lista de criaturas nivel 1 (usar en modo historia)
CriaturaBase1 = Dragon("Draconio", 1, 240, 45, 45, 35, 5, 4)
CriaturaBase2 = Pez("Pececito", 1, 180, 40, 60, 50, 3, 4)
CriaturaBase3 = Ogro("Paco", 1, 200, 50, 40, 30, 4, 4)
CriaturaBase4 = Bombastico("Bum", 1, 160, 70, 30, 25, 3, 4)
CriaturaBase5 = Hada("Aurora", 1, 120, 35, 55, 45, 2, 4)
CriaturaBase6 = Chupasangre("Succionio", 1, 200, 40, 50, 40, 2, 4)
CriaturaBase7 = Golem("Rocky", 1, 250, 30, 40, 30, 7, 4)
CriaturaBase8 = Criatura("Random", 1, 220, 60, 50, 40, 4, 4)

# Lista de clases (usar en modo historia)
CriaturaClase1 = Dragon("Draconio", 1, 240, 45, 45, 35, 5, 4)
CriaturaClase2 = Pez("Pececito", 1, 180, 40, 60, 50, 3, 4)
CriaturaClase3 = Ogro("Paco", 1, 200, 50, 40, 30, 4, 4)
CriaturaClase4 = Bombastico("Bum", 1, 160, 70, 30, 25, 3, 4)
CriaturaClase5 = Hada("Aurora", 1, 120, 35, 55, 45, 2, 4)
CriaturaClase6 = Chupasangre("Succionio", 1, 200, 40, 50, 40, 2, 4)
CriaturaClase7 = Golem("Rocky", 1, 250, 30, 40, 30, 7, 4)
CriaturaClase8 = Criatura("Random", 1, 220, 60, 50, 40, 4, 4)
# Listas de criaturas
listaClasesHistoria = [CriaturaClase1, CriaturaClase2, CriaturaClase3, CriaturaClase4,CriaturaClase5, CriaturaClase6, CriaturaClase7, CriaturaClase8]
listaCriaturasBase = [CriaturaBase1, CriaturaBase2, CriaturaBase3, CriaturaBase4,CriaturaBase5, CriaturaBase6, CriaturaBase7, CriaturaBase8]
listaVersus = [CriaturaVersus1, CriaturaVersus2, CriaturaVersus3, CriaturaVersus4,CriaturaVersus5, CriaturaVersus6, CriaturaVersus7, CriaturaVersus8]

# Normas del juego

# Un algoritmo simple para que dependiendo de factores como su propia vida, o si el enemigo esta mas debil, la criatura decida si atacar o recuperarse (subir vida/estamina), con un porcentaje de aleatoriedad que hace que un mismo enfrentamiento pueda tener diversos resultados
def Decision(peleador,enemigo):

  RNG1 = random.uniform(0, 1)

  if peleador.vida >= ((85/100) * peleador.vidaMax) and peleador.estamina >= ((20/100) * peleador.estaminaMax): 
    peleador - enemigo

  elif peleador.vida >= ((50/100) * peleador.vidaMax) and RNG1 >= 0.4:
    peleador - enemigo

  elif peleador.vida >= ((25/100) * peleador.vidaMax) and RNG1 >= 0.75:
    peleador - enemigo

  elif enemigo.vida >= ((25/100) * enemigo.vidaMax) and RNG1 >= 0.25:
    peleador - enemigo

  elif peleador.estamina >= 0:
    peleador + (random.uniform(0.05, 0.15)* peleador.vidaMax)
  else:
    peleador + (random.uniform(0.05, 0.15)* peleador.vidaMax)

# -------------------------------- COSAS COMUNES A VARIOS METODOS PYGAME ---------------

WIDTH, HEIGHT = 1430, 800
colorSuelo = (55,8,8)
colorAmbiente = (8, 5, 20)
colorMargenes = (175,150,150)
colorBlanco = (255,255,255)

particulitas = []
for _ in range(80):
  x = random.randint(0, WIDTH)
  y = random.randint(0, HEIGHT)
  vx = random.uniform(-1.5, 1.5)
  vy = random.uniform(-1.5, 1.5)
  size = random.randint(1, 7)
  particulitas.append([x, y, vx, vy, size])
  
# -------------------------------- COSAS COMUNES A VARIOS METODOS PYGAME ---------------

def GenerarParticulas(pantalla,color):
  for p in particulitas:
    p[0] += p[2]
    p[1] += p[3]

    # Reaparecer si salen de pantalla
    if p[0] < 0 or p[0] > WIDTH or p[1] < 0 or p[1] > HEIGHT:
        p[0] = random.randint(0, WIDTH)
        p[1] = random.randint(0, HEIGHT)
      
  for p in particulitas:
    x, y, _, _, size = p
    pygame.draw.circle(pantalla, color, (int(x), int(y)), size)

def Batalla(peleador1, peleador2):
  pygame.init()
  pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Batalla")
  clock = pygame.time.Clock()

  fuenteMensajes = pygame.font.SysFont("Karmatic Arcade", 30)
  fuenteCuadroTexto = pygame.font.SysFont("Karmatic Arcade", 40)
  fuenteInterfaz = pygame.font.SysFont("Karmatic Arcade", 20)
  fuenteBarras = pygame.font.SysFont("Karmatic Arcade", 10)
  
  estado = "decideJugador"  
  
  str(peleador1)
  str(peleador2) #volver aqui (pasar al innit)

  
  r = 1
  running = True
  while running:

    # Dibujar
    pantalla.fill(colorAmbiente) # Fondo
    GenerarParticulas(pantalla, (150 + int(x / WIDTH * 100), 40, 40))  # degradado simple

    # Suelo
    pygame.draw.rect(pantalla, (colorSuelo), (0,  HEIGHT * 1/3, WIDTH, HEIGHT * 3/4)) 
    pygame.draw.rect(pantalla, (175,80,80), (30,  HEIGHT * 1/3 + 30, WIDTH - 60, HEIGHT * 3/4 - 60)) 
    # Peleadores
    pygame.draw.circle(pantalla, (0,0,0), (WIDTH//4, HEIGHT-200), 125)
    pygame.draw.circle(pantalla, peleador1.color, (WIDTH//4, HEIGHT-200), 120) # Imagen Jugador 1
 
    pygame.draw.circle(pantalla, (0,0,0), (WIDTH-WIDTH//4, 200), 125) 
    pygame.draw.circle(pantalla, peleador2.color, (WIDTH-WIDTH//4, 200), 120) # Imagen Jugador 2

    # Barras de estadísticas
    barraVidaAncho = 300
    barraVidaAlto = 25

    barraStaAncho = 180
    barraStaAlto = 15

    # Jugador

    estaminaMax1 = peleador1.estamina_base * (1 + peleador1.escalador_estamina * peleador1.nivel)
    
    pygame.draw.rect(pantalla, (15,10,40), (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 170, barraVidaAncho + 40, 150))
    # Margenes Cuadrado Enemigo
    pygame.draw.line(pantalla, colorMargenes, (WIDTH - 20, HEIGHT * 3/4 - 170 + 150), (WIDTH - 20, HEIGHT * 3/4 - 170), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 170 + 150), (WIDTH - 20, HEIGHT * 3/4 - 170 + 150), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 170), (WIDTH - 20, HEIGHT * 3/4 - 170), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 170), (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 170 + 150), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH - barraVidaAncho - 60, HEIGHT * 3/4 - 105), (WIDTH - 20, HEIGHT * 3/4 - 105), 5)
    # Texto Cuadrado Enemigo
    pantalla.blit(fuenteInterfaz.render(f"{peleador1.nombreCompleto} N.{peleador1.nivel}", True, peleador1.color), (WIDTH - barraVidaAncho - 40, HEIGHT * 4/6 - 80))

    pygame.draw.rect(pantalla, (50,10,20), (WIDTH - barraVidaAncho - 40, HEIGHT * 4/6 - 20, barraVidaAncho, barraVidaAlto)) # vida maxima
    pygame.draw.rect(pantalla, (200,10,50),(WIDTH - barraVidaAncho - 40, HEIGHT * 4/6 - 20, (barraVidaAncho*(peleador1.vida/peleador1.vidaMax)), barraVidaAlto)) # vida restante
    pantalla.blit(fuenteBarras.render(f"{int(peleador1.vida)}", True, colorBlanco), (WIDTH - barraVidaAncho + 80, HEIGHT * 4/6 - 15)) #mostrar cantidad

    pygame.draw.rect(pantalla, (50,50,20), (WIDTH - barraStaAncho - 40, HEIGHT * 4/6 + barraVidaAlto -10, barraStaAncho, barraStaAlto)) #estamina maxima
    pygame.draw.rect(pantalla, (200,200,50),(WIDTH - barraStaAncho - 40, HEIGHT * 4/6 + barraVidaAlto -10, (barraStaAncho * (peleador1.estamina/estaminaMax1)), barraStaAlto)) # estamina restante
    pantalla.blit(fuenteBarras.render(f"{int(peleador1.estamina)}", True, colorAmbiente), (WIDTH - barraStaAncho/2 - 60, HEIGHT * 4/6 + 15)) #mostrar cantidad

    # Enemigo

    estaminaMax2 = peleador2.estamina_base * (1 + peleador2.escalador_estamina * peleador2.nivel)

    pygame.draw.rect(pantalla, (15,10,40), (20, 20, barraVidaAncho + 40, 150)) # Cuadrado Enemigo
    # Margenes Cuadrado Enemigo
    pygame.draw.line(pantalla, colorMargenes, (20, 20), (barraVidaAncho + 40 + 20, 20), 5)
    pygame.draw.line(pantalla, colorMargenes, (20, 20), (20, 150 + 20), 5)
    pygame.draw.line(pantalla, colorMargenes, (barraVidaAncho + 40 + 20, 20), (barraVidaAncho + 40 + 20, 150 + 20), 5)
    pygame.draw.line(pantalla, colorMargenes, (20, 150 + 20), (barraVidaAncho + 40 + 20, 150 + 20), 5)
    pygame.draw.line(pantalla, colorMargenes, (20, 85), (barraVidaAncho + 40 + 20, 85), 5)
    # Texto Cuadrado Enemigo
    pantalla.blit(fuenteInterfaz.render(f"{peleador2.nombreCompleto} N.{peleador2.nivel}", True, peleador2.color), (40, 40))

    pygame.draw.rect(pantalla, (50,10,20), (40, HEIGHT/12 + 40, barraVidaAncho, barraVidaAlto)) # vida maxima
    pygame.draw.rect(pantalla, (200,10,50),(40,HEIGHT/12 + 40, (barraVidaAncho*(peleador2.vida/peleador2.vidaMax)), barraVidaAlto)) # vida restante
    pantalla.blit(fuenteBarras.render(f"{int(peleador2.vida)}", True, colorBlanco), (barraVidaAncho - 130, HEIGHT/12 + 45)) #mostrar cantidad

    pygame.draw.rect(pantalla, (50,50,20), (40, HEIGHT/12 + 40 + barraVidaAlto + 10 , barraStaAncho, barraStaAlto)) #estamina maxima
    pygame.draw.rect(pantalla, (200,200,50),(40,HEIGHT/12 + 40 + barraVidaAlto + 10, (barraStaAncho * (peleador2.estamina/estaminaMax2)), barraStaAlto)) # estamina restante
    pantalla.blit(fuenteBarras.render(f"{int(peleador2.estamina)}", True, colorAmbiente), (barraVidaAncho - 190, HEIGHT/12 + 75)) #mostrar cantidad

    # Cuadro de texto
    pygame.draw.rect(pantalla, (15,10,40), (0, HEIGHT - HEIGHT//4, WIDTH, HEIGHT//4))
    pygame.draw.line(pantalla, colorMargenes, (WIDTH, HEIGHT), (WIDTH, HEIGHT * 3/4), 5)
    pygame.draw.line(pantalla, colorMargenes, (0, HEIGHT), (0, HEIGHT * 3/4), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH, HEIGHT * 3/4), (0, HEIGHT * 3/4), 5)
    pygame.draw.line(pantalla, colorMargenes, (WIDTH, HEIGHT), (0, HEIGHT), 5)

    # Mensaje
    if estado in ("mensajeJugador", "mensajeIA"):
      texto = fuenteMensajes.render(mensaje, True, (255,255,255))
      pantalla.blit(texto, (40, HEIGHT - HEIGHT//4 + 50))
    
    # decideJugador
    if estado == "decideJugador":
      
      pantalla.blit(fuenteCuadroTexto.render("W - ATACAR", True, (255,80,80)), (WIDTH * 0.05, HEIGHT * 0.85))
      pantalla.blit(fuenteCuadroTexto.render("A - RECUPERAR", True, (80,255,80)), (WIDTH * 0.70, HEIGHT * 0.85))
      pantalla.blit(fuenteCuadroTexto.render("S - HUIR", True, (80,80,255)), (WIDTH//2 - 100, HEIGHT * 0.91))
      pantalla.blit(fuenteCuadroTexto.render(f"RONDA {r}", True, (255,255,255)), (WIDTH//2 - 110, HEIGHT * 0.78))
      pygame.draw.line(pantalla, colorMargenes, (WIDTH * 1/3, HEIGHT), (WIDTH * 1/3, HEIGHT * 3/4), 5)
      pygame.draw.line(pantalla, colorMargenes, (WIDTH * 2/3, HEIGHT), (WIDTH * 2/3, HEIGHT * 3/4), 5)
      pygame.draw.line(pantalla, colorMargenes, (WIDTH * 2/3, HEIGHT * 7/8), (WIDTH * 1/3, HEIGHT * 7/8), 5)

    # Eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
          peleador1.recalcular_stats()
          peleador2.recalcular_stats()
          MenuVersus()

      # Estado: decideJugador
      if estado == "decideJugador":
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:  # Atacar
            peleador1 - peleador2
            mensaje = peleador1.Frase
            estado = "mensajeJugador"

          elif event.key == pygame.K_a:  # Curarse
            cantidad = random.uniform(0.1,0.05)*peleador1.vidaMax
            peleador1 + cantidad
            mensaje = peleador1.Frase
            estado = "mensajeJugador"

          elif event.key == pygame.K_s:
            if random.uniform(0,1) >= 0.5:
              running = False
              MenuVersus()
            else:
              mensaje = f"{peleador1.nombreCompleto} falla en la huida y pierde el turno"
              estado = "mensajeJugador"          

      # Estado: mensajeJugador
      elif estado == "mensajeJugador": 
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            estado = "decideIA"

      # Estado: mensajeIA
      elif estado == "mensajeIA":
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            r = r+1
            estado = "decideJugador"

    # Estado: decideIA
      if estado == "decideIA":
        if peleador2.vivo:
          if ((peleador2.velocidad)/(peleador1.velocidad)) >= 5:
            Decision(peleador2,peleador1)
            Decision(peleador2,peleador1)
          else:
            Decision(peleador2,peleador1)
          mensaje = peleador2.Frase
          estado = "mensajeIA"
        else:
          estado = "mensajeIA"

      # Final Batalla
      if not peleador1.vivo or not peleador2.vivo:
          ganador = peleador1 if peleador1.vivo else peleador2
          mensaje = f"🏆 {ganador.nombreCompleto} gana la batalla!   Pulsa RSHIFT"
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
              return

      
    pygame.display.flip()
    clock.tick(60)

  pygame.quit()

def BatallaVersus(peleador1, peleador2):
  Batalla(peleador1, peleador2)
  MenuVersus()

def SeleccionPersonaje(pantalla):
  # Dibujar Contendientes: 

  FuenteSeleccion= pygame.font.SysFont("Karmatic Arcade", 19)
  
  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 2/10, HEIGHT * 1/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus1.color, (WIDTH * 2/10, HEIGHT * 1/5), WIDTH * 1/16)
  Seleccionable1 =  FuenteSeleccion.render(f"-1- {CriaturaVersus1.nombre} N.{CriaturaVersus1.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable1, (WIDTH * 2/10 - 120, HEIGHT * 1/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 4/10, HEIGHT * 1/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus2.color, (WIDTH * 4/10, HEIGHT * 1/5), WIDTH * 1/16)
  Seleccionable2 =  FuenteSeleccion.render(f"-2- {CriaturaVersus2.nombre} N.{CriaturaVersus2.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable2, (WIDTH * 4/10 - 120, HEIGHT * 1/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 6/10, HEIGHT * 1/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus3.color, (WIDTH * 6/10, HEIGHT * 1/5), WIDTH * 1/16)
  Seleccionable3 =  FuenteSeleccion.render(f"-3- {CriaturaVersus3.nombre} N.{CriaturaVersus3.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable3, (WIDTH * 6/10 - 100, HEIGHT * 1/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 8/10, HEIGHT * 1/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus4.color, (WIDTH * 8/10, HEIGHT * 1/5), WIDTH * 1/16)
  Seleccionable4 =  FuenteSeleccion.render(f"-4- {CriaturaVersus4.nombre} N.{CriaturaVersus4.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable4, (WIDTH * 8/10 - 100, HEIGHT * 1/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 2/10, HEIGHT * 3/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus5.color, (WIDTH * 2/10, HEIGHT * 3/5), WIDTH * 1/16)
  Seleccionable5 =  FuenteSeleccion.render(f"-5- {CriaturaVersus5.nombre} N.{CriaturaVersus5.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable5, (WIDTH * 2/10 - 120, HEIGHT * 3/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 4/10, HEIGHT * 3/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus6.color, (WIDTH * 4/10, HEIGHT * 3/5), WIDTH * 1/16)
  Seleccionable6 =  FuenteSeleccion.render(f"-6- {CriaturaVersus6.nombre} N.{CriaturaVersus6.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable6, (WIDTH * 4/10 - 120, HEIGHT * 3/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 6/10, HEIGHT * 3/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus7.color, (WIDTH * 6/10, HEIGHT * 3/5), WIDTH * 1/16)
  Seleccionable7 =  FuenteSeleccion.render(f"-7- {CriaturaVersus7.nombre} N.{CriaturaVersus7.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable7, (WIDTH * 6/10 - 120, HEIGHT * 3/5 + WIDTH * 1/16 + 30))

  pygame.draw.circle(pantalla, (0,0,0), (WIDTH * 8/10, HEIGHT * 3/5), WIDTH * 1/16 + 10) 
  pygame.draw.circle(pantalla, CriaturaVersus8.color, (WIDTH * 8/10, HEIGHT * 3/5), WIDTH * 1/16)
  Seleccionable8 =  FuenteSeleccion.render(f"-8- {CriaturaVersus8.nombre} N.{CriaturaVersus8.nivel}", True, colorBlanco)
  pantalla.blit(Seleccionable8, (WIDTH * 8/10 - 120, HEIGHT * 3/5 + WIDTH * 1/16 + 30))
    
# Lista de criaturas nivel 100 (usar en modo vresu
# Listas de criaturas
listaClasesAventura = [CriaturaClase1, CriaturaClase2, CriaturaClase3, CriaturaClase4,
                      CriaturaClase5, CriaturaClase6, CriaturaClase7, CriaturaClase8]
listaCriaturasBase = [CriaturaBase1, CriaturaBase2, CriaturaBase3, CriaturaBase4,
                      CriaturaBase5, CriaturaBase6, CriaturaBase7, CriaturaBase8]
listaVersus = [CriaturaVersus1, CriaturaVersus2, CriaturaVersus3, CriaturaVersus4,
               CriaturaVersus5, CriaturaVersus6, CriaturaVersus7, CriaturaVersus8]
i = 0
while i < len(listaCriaturasBase):
    listaCriaturasBase[i].indiceBase = i
    i += 1
# Menu 2.0

def PantallaTitulo():
  pygame.init()

  pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("MaxiChiqui")
  clock = pygame.time.Clock()
  running = True

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit(); return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          MenuPrincipal(); return

    # Dibujar pantalla general
    pantalla.fill(colorAmbiente)

    # Fuentes
    FuenteTitulo = pygame.font.SysFont("Glastone 3D Demo ExtrudeRight", 150)
    FuenteSubtitulo = pygame.font.SysFont("Karmatic Arcade", 30)

    Subtitulo = FuenteSubtitulo.render("Pulsa Espacio", True, (255, 220, 220))
    Titulo = FuenteTitulo.render("MaxiChiqui", True, (255, 220, 240))
    SombraTitulo = FuenteTitulo.render("MaxiChiqui", True, (130, 10, 120))
    
    # Lo que se muestra
    pantalla.blit(Subtitulo, (575,450))
    
    GenerarParticulas(pantalla, ((150 + int(x / WIDTH * 100), 70, 120)))

    pantalla.blit(SombraTitulo, (364,189))
    pantalla.blit(Titulo, (375,200))
      
    pygame.display.flip()
    clock.tick(60)      

  pygame.quit()

def MenuPrincipal():
  pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()
  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit(); return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1: 
          MenuHistoria()
        if event.key == pygame.K_2: 
          MenuVersus()
        if event.key == pygame.K_3: 
          pygame.quit()
        if event.key == pygame.K_ESCAPE: 
          PantallaTitulo()

    # Dibujar pantalla general
    pantalla.fill(colorAmbiente)

    FuenteTitulo = pygame.font.SysFont("Glastone 3D Demo ExtrudeRight", 150)
    FuenteSubtitulo = pygame.font.SysFont("Karmatic Arcade", 30)

    Frase1 = FuenteSubtitulo.render("1 -- Modo Historia", True, (120, 255, 130))
    Frase2 = FuenteSubtitulo.render("2 -- Modo Versus", True, (130, 120, 255))
    Frase3 = FuenteSubtitulo.render("3 -- Salir", True, (255, 120, 130))
    Titulo = FuenteTitulo.render("Menu Principal", True, (155, 220, 240))
    SombraTitulo = FuenteTitulo.render("Menu Principal", True, (30, 10, 120))
    
    pantalla.blit(Frase1, (545,500))
    pantalla.blit(Frase2, (545,550))
    pantalla.blit(Frase3, (545,600))

    GenerarParticulas(pantalla, (120, 170, 150 + int(x / WIDTH * 100)))
    
    pantalla.blit(SombraTitulo, (244,189))
    pantalla.blit(Titulo, (255,200))
        
    pygame.display.flip()
    clock.tick(60)      

  pygame.quit()
  

def MenuVersus():
  pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()
  running = True
  estado = "menuVersus"

  # Fuentes
  FuenteTitulo = pygame.font.SysFont("Glastone 3D Demo ExtrudeRight", 150)
  FuenteSubtitulo = pygame.font.SysFont("Karmatic Arcade", 30)

  # Textos
  Frase1 = FuenteSubtitulo.render("1 -- Enfrentarse a IA", True, (120, 220, 220))
  Frase2 = FuenteSubtitulo.render("2 -- Jugador vs Jugador", True, (255, 120, 130))
  Frase3 = FuenteSubtitulo.render("¡Peleador 1 Seleccionado!", True, (80, 80, 255))
  Frase4 = FuenteSubtitulo.render("¡Peleador 2 Seleccionado!", True, (255, 80, 80))
  Frase5 = FuenteSubtitulo.render("SELECCIONA PELEADOR", True, (colorBlanco))

  Titulo = FuenteTitulo.render("Modo Versus", True, (220, 240, 155))
  SombraTitulo = FuenteTitulo.render("Modo Versus", True, (80, 80, 10))

  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          MenuPrincipal()

      # Estados
      if event.type == pygame.KEYDOWN:
        if estado == "menuVersus":
          if event.key == pygame.K_1:
            estado = "seleccionarP1"

        elif estado == "seleccionarP1":
          if event.key == pygame.K_1:
            peleadorVersus1 = CriaturaVersus1
            estado = "siguiente1"
          elif event.key == pygame.K_2:
            peleadorVersus1 = CriaturaVersus2
            estado = "siguiente1"
          elif event.key == pygame.K_3:
            peleadorVersus1 = CriaturaVersus3
            estado = "siguiente1"
          elif event.key == pygame.K_4:
            peleadorVersus1 = CriaturaVersus4
            estado = "siguiente1"
          elif event.key == pygame.K_5:
            peleadorVersus1 = CriaturaVersus5
            estado = "siguiente1"
          elif event.key == pygame.K_6:
            peleadorVersus1 = CriaturaVersus6
            estado = "siguiente1"
          elif event.key == pygame.K_7:
            peleadorVersus1 = CriaturaVersus7
            estado = "siguiente1"
          elif event.key == pygame.K_8:
            peleadorVersus1 = CriaturaVersus8
            estado = "siguiente1"

        elif estado == "siguiente1":
          if event.key == pygame.K_RETURN:
            estado = "seleccionarP2"

        elif estado == "seleccionarP2":
          if event.key == pygame.K_1:
            peleadorVersus2 = CriaturaVersus1
            estado = "siguiente2"
          elif event.key == pygame.K_2:
            peleadorVersus2 = CriaturaVersus2
            estado = "siguiente2"
          elif event.key == pygame.K_3:
            peleadorVersus2 = CriaturaVersus3
            estado = "siguiente2"
          elif event.key == pygame.K_4:
            peleadorVersus2 = CriaturaVersus4
            estado = "siguiente2"
          elif event.key == pygame.K_5:
            peleadorVersus2 = CriaturaVersus5
            estado = "siguiente2"
          elif event.key == pygame.K_6:
            peleadorVersus2 = CriaturaVersus6
            estado = "siguiente2"
          elif event.key == pygame.K_7:
            peleadorVersus2 = CriaturaVersus7
            estado = "siguiente2"
          elif event.key == pygame.K_8:
            peleadorVersus2 = CriaturaVersus8
            estado = "siguiente2"

        elif estado == "siguiente2":
          if event.key == pygame.K_RETURN:
            estado = "batallaVersus"

        elif estado == "batallaVersus":
          Batalla(peleadorVersus1, peleadorVersus2)
          running = False

    # Dibujar
    pantalla.fill(colorAmbiente)
    GenerarParticulas(pantalla, (200, 150, 120))

    if estado == "menuVersus":
      pantalla.blit(Frase1, (505, 500))
      pantalla.blit(Frase2, (505, 550))
      pantalla.blit(SombraTitulo, (294, 189))
      pantalla.blit(Titulo, (305, 200))

    elif estado == "seleccionarP1":
      SeleccionPersonaje(pantalla)
      pantalla.blit(Frase5, (WIDTH/2 - 250, HEIGHT * 5/6))

    elif estado == "siguiente1":
      pantalla.blit(Frase3, (WIDTH/2 - 250, HEIGHT * 1/2))

    elif estado == "seleccionarP2":
      SeleccionPersonaje(pantalla)
      pantalla.blit(Frase5, (WIDTH/2 - 250, HEIGHT * 5/6))

    elif estado == "siguiente2":
      pantalla.blit(Frase4, (WIDTH/2 - 250, HEIGHT * 1/2))

    pygame.display.flip()
    clock.tick(60)

  pygame.quit()

def MenuHistoria():
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # Imputs

    while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
              ModoHistoriaJuego()
            if event.key == pygame.K_ESCAPE:
              MenuPrincipal()

      # Dibujar pantalla general
      pantalla.fill(colorAmbiente)

      FuenteTitulo = pygame.font.SysFont("Glastone 3D Demo ExtrudeRight", 150)
      FuenteSubtitulo = pygame.font.SysFont("Karmatic Arcade", 30)

      Frase1 = FuenteSubtitulo.render("1 -- Nueva Partida", True, (220, 190, 120))
      Frase2 = FuenteSubtitulo.render("2 -- Cargar Partida", True, (190, 120, 220))
      Titulo = FuenteTitulo.render("Modo Historia", True, (120, 240, 155))
      SombraTitulo = FuenteTitulo.render("Modo Historia", True, (10, 80, 12))
      
      pantalla.blit(Frase1, (505,500))
      pantalla.blit(Frase2, (505,550))

      GenerarParticulas(pantalla, (100, 150  + int(x / WIDTH * 100), 120))

      pantalla.blit(SombraTitulo, (274,189))
      pantalla.blit(Titulo, (285,200))
         
      pygame.display.flip()
      clock.tick(60)      

    pygame.quit()


def GenerarTablero(criaturaJugador):
    filas, columnas = 10, 10
    tamañoCelda = 60
    offsetX = WIDTH // 2 - (columnas * tamañoCelda) // 2
    offsetY = HEIGHT // 2 - (filas * tamañoCelda) // 2

    # Crear matriz vacía
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Posición inicial del jugador
    x_cell, y_cell = 0, 0
    tablero[y_cell][x_cell] = 1

    # Generar enemigos
    enemigos = []
    cantidadEnemigos = 2

    while len(enemigos) < cantidadEnemigos:
        ex = int(random.uniform(0, columnas))
        ey = int(random.uniform(0, filas))

        if tablero[ey][ex] == 0:
            tablero[ey][ex] = 2
            eleccion = int(random.uniform(1, 8))
            base = listaClasesAventura[eleccion]

            enemigo = base
            enemigo.nivel = criaturaJugador.nivel + int(random.uniform(-2, 2))
            enemigo.recalcular_stats()

            enemigos.append({
                "criatura": enemigo,
                "x_cell": ex,
                "y_cell": ey
            })

    return tablero, enemigos, filas, columnas, tamañoCelda, offsetX, offsetY, x_cell, y_cell


def JugarModoHistoria(pantalla, clock, criaturaJugador,tablero, enemigos,filas, columnas,tamañoCelda, offsetX, offsetY,x_cell, y_cell):

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, x_cell, y_cell, enemigos

            if event.type == pygame.KEYDOWN:
                nuevoX, nuevoY = x_cell, y_cell

                if event.key == pygame.K_w:
                    nuevoY -= 1
                elif event.key == pygame.K_s:
                    nuevoY += 1
                elif event.key == pygame.K_a:
                    nuevoX -= 1
                elif event.key == pygame.K_d:
                    nuevoX += 1
                elif event.key == pygame.K_ESCAPE:
                    MenuPrincipal()
                    return False, x_cell, y_cell, enemigos

                if 0 <= nuevoX < columnas and 0 <= nuevoY < filas:
                    valorDestino = tablero[nuevoY][nuevoX]

                    if valorDestino != 4:
                        tablero[y_cell][x_cell] = 0

                    x_cell, y_cell = nuevoX, nuevoY

                    if valorDestino != 4:
                        tablero[y_cell][x_cell] = valorDestino + 1
                    else:
                        tablero[y_cell][x_cell] = 1

                    # Batalla
                    if tablero[y_cell][x_cell] == 3:
                        i = 0
                        while i < len(enemigos):
                            e = enemigos[i]
                            if e["x_cell"] == x_cell and e["y_cell"] == y_cell:
                                Batalla(criaturaJugador, e["criatura"])
                                if criaturaJugador.vivo:
                                    enemigos.pop(i)
                                    tablero[y_cell][x_cell] = 1

                                    if len(enemigos) == 0:
                                        sx = int(random.uniform(0, columnas))
                                        sy = int(random.uniform(0, filas))
                                        while tablero[sy][sx] != 0:
                                            sx = int(random.uniform(0, columnas))
                                            sy = int(random.uniform(0, filas))
                                        tablero[sy][sx] = 4
                                else:
                                    return False, x_cell, y_cell, enemigos
                            i += 1

                    # Nueva mazmorra
                    if tablero[y_cell][x_cell] == 4:
                        tablero, enemigos, filas, columnas, tamañoCelda, offsetX, offsetY, x_cell, y_cell = GenerarTablero(criaturaJugador)

        # Dibujar tablero
        pantalla.fill(colorAmbiente)
        for y in range(filas):
            for x in range(columnas):
                rect = pygame.Rect(
                    offsetX + x * tamañoCelda,
                    offsetY + y * tamañoCelda,
                    tamañoCelda,
                    tamañoCelda
                )
                pygame.draw.rect(pantalla, colorMargenes, rect, 1)

                valor = tablero[y][x]
                if valor == 1:
                    pygame.draw.circle(pantalla, criaturaJugador.color, rect.center, tamañoCelda // 2 - 5)
                elif valor == 2:
                    for e in enemigos:
                        if e["x_cell"] == x and e["y_cell"] == y:
                            pygame.draw.circle(pantalla, e["criatura"].color, rect.center, tamañoCelda // 2 - 5)
                elif valor == 4:
                    pygame.draw.rect(pantalla, (0, 200, 0), rect)

        pygame.display.flip()
        clock.tick(60)

    return True, x_cell, y_cell, enemigos



def ModoHistoriaJuego(criaturaJugador):
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    tablero, enemigos, filas, columnas, tamañoCelda, offsetX, offsetY, x_cell, y_cell = GenerarTablero(criaturaJugador)

    jugando = True
    while jugando:
        jugando, x_cell, y_cell, enemigos = JugarModoHistoria(
            pantalla, clock, criaturaJugador,
            tablero, enemigos,
            filas, columnas,
            tamañoCelda, offsetX, offsetY,
            x_cell, y_cell
        )

    pygame.quit()



def SeleccionHistoria():
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_8:
                    indice = event.key - pygame.K_1
                    jugador = listaClasesAventura[indice]
                    ModoHistoriaJuego(jugador)
                    running = False

                if event.key == pygame.K_ESCAPE:
                    MenuHistoria()

        pantalla.fill(colorAmbiente)
        GenerarParticulas(pantalla, (250, 180, 60))

        fuente = pygame.font.SysFont("Karmatic Arcade", 25)
        texto = fuente.render("ELIGE TU CRIATURA (1-8)", True, colorBlanco)
        pantalla.blit(texto, (WIDTH // 2 - 200, 80))

        i = 0
        while i < len(listaClasesAventura):
            c = listaClasesAventura[i]
            pygame.draw.circle(
                pantalla,
                c.color,
                (200 + (i % 4) * 300, 250 + (i // 4) * 200),
                40
            )
            nombre = fuente.render(f"{i+1} - {c.nombre}", True, colorBlanco)
            pantalla.blit(nombre, (160 + (i % 4) * 300, 300 + (i // 4) * 200))
            i += 1

        pygame.display.flip()
        clock.tick(60)


# Pruebas
PantallaTitulo()

#Pruebas

PantallaTitulo()

