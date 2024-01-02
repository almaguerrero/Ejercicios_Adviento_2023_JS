"""
crear una función qeu calcule MCD de dos números 
por el método de Euclides
"""
def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Ejemplo de uso
numero1 = 87
numero2 = 18
mcd_resultado = calcular_mcd(numero1, numero2)

print(f"El MCD de {numero1} y {numero2} es: {mcd_resultado}")

