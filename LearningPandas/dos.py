import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

naranjas = pd.Series([10, 11, 12, 13, 14, 15, 16])
colores = pd.Series(["rojo", "negro", "azul", "amarillo", "violeta"])

print(naranjas)
print(colores)

#Ahora vamos a seleccionar los datos basados en su indice. 
print(naranjas[0], "nos regreas el valor 0 de nuestro objeto")
print(colores[1], "nos regresa el valor 1 de nuestro objeto")

#Ahora vamos a crear un diccionario, la diferencia es usando llaves {} en lugar de corchetes []
materias = pd.Series({"matematicas":80, 
                      "historia":100,
                      "geografía":90, 
                      "español":10, 
                      "filosofia":70})

print(materias)
print(materias["matematicas"], "nor regresa el valor de nuestra llave MATEMATICAS")

#Algunas de las funciones importantes que nos puedan llegar a servir son las siguientes
# .size
# .dtype
# .index

print(materias.size , "Esto nos indica el tamaño de nuestro objeto")
print(materias.dtype , "Esto nos da el TIPO de nuestro objeto")
print(materias.index , "Esto nos da el INDICE de nuestro objeto")

#Finalmente, mediante el indice, podemos hacer un  control de información mediante bucles y condicionales