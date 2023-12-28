"""
Crear un programa que pida dos números y vea si el primera numero es 
múltiplo del segundo
"""
def Multi(num1,num2):
    if numero1 % numero2 == 0:
       print(f"{numero1} es múltiplo de {numero2}.")
    else:
       print(f"{numero1} no es múltiplo de {numero2}.")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
Multi(numero1,numero2)