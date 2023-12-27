"""
Hacer un programa que imprima una tabla de multiplicar del 2 al 9.
Cada uno debe mostrar sus valores multiplcaodr del 2 al 9
"""
for numero in range(2, 10):
    print("tabla del: ", numero)
    for i in range(1,10):
     print(f"{numero} x {i}",numero*i)