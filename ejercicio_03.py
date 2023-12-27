"""
Hacer un programa que solicite una edad e imprima si es mayor de edad
 o menor de edad
"""
age = input('Introduce una edad:  ')
if int(age) >= 18: 
    print("Es mayor")
else:
    print("Es menor")