"""
Crear una funcion que regrese el valor minimo y máximo
"""
def calcularMinMax():
    valores = [] 
    num_00 = int(input("Ingresa el número de valores: "))
    for i in range(num_00):
        valores.append(int(input(f"Ingresa el valor {i}: ")))
    
    print(f"el valor minimo es: {min(valores)}")
    print(f"el valor maximo es: {max(valores)}")

calcularMinMax()



