'''
 Hacer un programa que muestre el siguiente dibujo.
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
'''
filas = input('dame las filas:  ')
columnas = int(filas) * 2
for numero in range(int(filas)):
    for i in range(columnas):
     print("*",end="")
    print("")