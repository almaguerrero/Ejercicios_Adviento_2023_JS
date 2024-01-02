"""
Fuuncion recursiva para calcular factorial de un 
numero
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Calculando el factorial de 5
resultado = factorial(5)
print(resultado)
