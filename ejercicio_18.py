"""
Diseñar una función que calcule el área y el perímetro de una circunferencia.
"""
import math

def area(radio):
    return (math.pi * radio**2)

def perimetro(radio):
    return (2 * math.pi * radio)

radio_ = float(input("Ingresa el radio de la circunferencia:   "))

print(f"El área es: {area(radio_)}")
print(f"El perimetro es: {perimetro(radio_)}")