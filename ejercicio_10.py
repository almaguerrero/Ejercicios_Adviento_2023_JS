"""
Hacer un programa que muestre el siguiente dibujo
* * * * * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * *
"""


filas = input('dame las filas:  ')
columnas = int(filas) * 2
for i in range(int(filas)):
    for j in range(columnas):
     if i ==0 or i == int(filas)-1 or j==0 or j==columnas-1:
        print("* ",end="")
     else:
        print(" ",end=" ")
    
    print()