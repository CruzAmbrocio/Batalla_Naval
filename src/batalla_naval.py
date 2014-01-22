# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="adela"
__date__ ="$22/01/2014 10:32:04 AM$"

import random

tablero = []

for x in range(0,5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print " ".join(fila)

print "Juguemos a batalla naval!"
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)

for turno in range(4):
    adivina_fila = input("Adivina fila:")
    adivina_columna = input("Adivina columna:")
    if adivina_fila == barco_fila and adivina_columna == barco_col:
        print "Felicitaciones! Hundiste mi barco!"
        break
    else:
        if (adivina_fila < 0 or adivina_fila > 4) or (adivina_columna < 0 or adivina_columna > 4):
            print "Vaya, esto ni siquiera esta en el oceano."
        elif(tablero[adivina_fila][adivina_columna] == "X"):
            print "Ya dijiste esa."
        else:
            print "No impactaste mi barco!" 
            tablero[adivina_fila][adivina_columna] = "X"
    print_tablero(tablero)
    print "Estas en el turno:" + str(turno + 1) + " de 4"
    if turno == 3:
            print u"Termino el juego" 
