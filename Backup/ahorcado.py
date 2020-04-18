# -*- coding: utf-8 -*-
"""Ahorcado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rshernandez10/ahorcado/blob/master/Ahorcado.ipynb
"""

import random
import os

palabras = ["COMPUTADORA" , "BALONES" , "AUDIFONO", "TECLADO", "ESCRITORIO", "GOLAZO", "NETFLIX"
"AHORCADO", "BICICLETA", "ATINADO", "TELESCOPIO"]

palabra = list(random.choice(palabras))

horca = ["          !=======|", #cuelga
         "                  |", #cabeza 
         "                  |", #brazos
         "                  |", #cuerpo
         "                  |", #piernas
         "__________________|"] #piso

figura = ["         !=======|", #cuelga
         "         :x       |", #cabeza 
         "        / | \     |", #brazos
         "          |       |", #cuerPo
         "         / \      |", #piernas
         "__________________|"] #piso

letras_selecc = []
errores = 1

resultado = []

for i in range(len(palabra)):
  resultado.append("_")

while True:

  os.system("cls")

print(palabra)
print ("AHORCADO")
print("------------------------------------------------------------")
print("El juego se trata de completar una palabra partiendo de una única letra (sin acentos).") 
print("Cada letra correcta se va colocando en los espacios. Cada error, va dibujando la figura del ahorcado (intentos máximos: 4)")      
print("El juego termina cuando:")
print("    El jugador completa la palabra.")
print("    El jugador llega al número máximo de intentos, mostrando la figura del ahorcado completa.")

for i in range(errores):
    print(figura[i])
    for i in range(len(horca)-errores):
        print(horca[i-errores])

    print()

    print( "    ", end= "  ")
    for i in resultado:
      print(i, end=" ")

    print()
    print()

    if resultado == palabra:
      print("Has ganado")
      break
    
    if errores > 5:
      print("No has adivinado, la palabra es ")
      print("Game Over")
      break

while True:
    letra_ingresada = input("Selecciona una letra: ")
    letra_ingresada_mayusc = letra_ingresada.upper()
    if len(letra_ingresada_mayusc) != 1: #si es distinto 
      print("No es una letra. Ingresa una letra nuevamente: ")
    elif letra_ingresada_mayusc in letras_selecc:
      print ("Letra repetida. Ingresa otra: ")
    elif  letra_ingresada_mayusc not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
      print("No es una letra. Ingresa una letra nuevamente: ")
    else:
      letras_selecc.append(letra_ingresada_mayusc)
      break

for i in range(len(palabra)):
  if palabra[i] == letra_ingresada_mayusc:
    resultado[i] = letra_ingresada_mayusc

  if letra_ingresada_mayusc not in palabra:
    fallos += 1
  
  print()
  print()

print (palabras)