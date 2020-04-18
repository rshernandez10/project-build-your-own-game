# -*- coding: utf-8 -*-
"""Ahorcado

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DomDD_GcaV3i7EBeTtVXymoqnyqwJENA
"""

import random
import os

palabras = ["COMPUTADORA" , "BALONES" , "AUDIFONO", "TECLADO", "ESCRITORIO", "GOLAZO", "NETFLIX"
"AHORCADO", "BICICLETA", "ATINADO", "TELESCOPIO"]

palabra = list(random.choice(palabras))

print(palabra)

horca = ["          !=======|", #cuelga
         "                  |", #cabeza 
         "                  |", #brazos
         "                  |", #cuerpo
         "                  |" #piernas
         "    ______________|"] #piso

ahorcado = ["          !=======|", #cuelga
            "          :x      |", #cabeza 
            "         /|\      |", #brazos
            "          |       |", #cuerpo
            "          /\      |" #piernas
            "    ______________|"] #piso

ahorcado2 = ["          !=======|", #cuelga
         "         :x       |", #cabeza 
         "       / | \     |", #brazos
         "          |       |", #cuerPo
         "         / \      |", #piernas
         "    _______________|"] #piso

print(horca)
print(ahorcado)

letras_todas = []
fallos = 1

resultado = []

for i in range(len(palabra)):
    resultado.append("_")

while True:
   # os.system("cls")
    cls = lambda: os.system ("cls")
    cls()

    print ("AHORCADO")
    
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
    
    if fallos > 4:
        print("No has adivinado, la palabra es ")
        print("Game Over")
        break
        
    while True:
        letra_usuario_sin_formato = input("Selecciona una letra: ")
        letra_usuario = letra_usuario_sin_formato.upper()
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