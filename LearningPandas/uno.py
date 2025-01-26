#This is a simple pprogram to remember how to use the Pandas library

#Initially we need to import all the libraries needed,

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#We need to cal a database with a CSV format, so. 

#Pandas es una librería especializada en el manejo de datos, sirve para 
#Manipular, mnomdelar, modelar y preparar los datos. 
#Pero los datos tienen que estar ya centralizados. 


'''
Nos permite leer datos de CSV, Excel, y SQL

Hay diferentes estructuras de datos
Series: Almmacena cualquier tipo de datos, tiene una secuencia ordenada, desde 0
básicamente se basa en indices
Data Frame: conjunto de series, Estructura bidimensional con columnas que pueden ser también 
de cualquier tipo
'''#Primeros pasos Vamos a generar una serie, llamado Naranjas 


naranjas = pd.Series([1, 2, 3, 4, 5]) #Vamos a generar una seria vacía
#Recordar que se llena conuna lista de Python
print(naranjas)

mazanas = pd.Series([1, 2, 3, 4, 5])
print(mazanas)

