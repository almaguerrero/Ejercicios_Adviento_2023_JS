"""
Hacer un programa que muestra este dibujo
* * * * *
* * * * 
* * *
* *
*
"""
filas = input('dame renglones:  ')
tamano = 5

# Imprimir triángulo invertido de asteriscos
for i in range(tamano, 0, -1):
    for j in range(tamano - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")
    print()