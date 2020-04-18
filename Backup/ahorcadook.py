# -*- coding: utf-8 -*-
"""AhorcadoOK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H0yQhN7XpSTZrhNlEbzA-JJlJT_77r0e
"""

def principal():

  import random
  import os

  palabras = ["COMPUTADORA" , "BALONES" , "AUDIFONO", "TECLADO", "ESCRITORIO", "GOLAZO", "NETFLIX",
  "AHORCADO", "BICICLETA", "ATINADO", "TELESCOPIO"]

  palabra = list(random.choice(palabras))

  #status = os.system("clear")
  #print(status)

  print(palabra)

  horca = ["          !=======|", #cuelga
          "                  |", #cabeza 
          "                  |", #brazos
          "                  |", #cuerpo
          "                  |", #piernas
          "    ______________|"] #piso

  ahorcado = ["          !=======|", #cuelga
              "          0       |", #cabeza 
              "         /|\      |", #brazos
              "          |       |", #cuerpo
              "         | |      |", #piernas
              "    _____-__-_____|"] #piso

  letras_todas = []
  fallos = 1

  resultado = []

  for i in range(len(palabra)):
      resultado.append("_")

  while True:
      os.system("clear")

      print ("******************")
      print ("**** AHORCADO ****")
      print ("******************")
      print ("                   ")
      print("Adivina la palabra, ingresando las letras de los espacios en blanco")
      print("Vocales sin acentos, ñ, o caracteres especiales")
      print("Tienes un máximo de 5 intentos")

  
      print ("                   ")
      print ("                   ")
      
      for i in range(fallos):
          print(ahorcado[i])
      for i in range(len(horca)-fallos):
          print(horca[i-fallos])

      print()

      print( "    ", end= "  ")
      for i in resultado:
            print(i, end=" ")

      print()
      print()

      if resultado == palabra:
          print("Has ganado")
          break
      
      if fallos > 1:
          print("No has adivinado, la palabra es", "".join(palabra))
          print("Game Over")
          break
          
      while True:
          letra_usuario = input("Selecciona una letra: ") .upper()
          #letra_usuario = letra_usuario_sin_formato.upper()
          if len(letra_usuario) != 1: #si es distinto 
              print("No es una letra. Ingresa una letra nuevamente: ")
          elif letra_usuario in letras_todas:
              print ("Letra repetida. Ingresa otra: ")
          elif  letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                print("No es una letra. Ingresa una letra nuevamente: ")
          else:
                letras_todas.append(letra_usuario)
                break

      for i in range(len(palabra)):
          if palabra[i] == letra_usuario:
              resultado[i] = letra_usuario

      if letra_usuario not in palabra:
          fallos += 1
    
      print()
      print()

  reiniciar = input("Jugar de nuevo? Oprime S para reiniciar u otra opcion para cerrar: ").upper()
 # if(len(reiniciar) != 1:
 #    print("No es una letra. ¿Jugar de nuevo?: ")
  if reiniciar == "S":
    principal()
  else:
    exit()

principal()