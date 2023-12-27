"""
Hacer un programa que cuente desde 
el 1 al 100 e imprima solo
los numeros divisibles por 2 y 5
"""
for numero in range(1, 101):
    if numero % 2 == 0 and numero % 5 == 0:
        print(numero)