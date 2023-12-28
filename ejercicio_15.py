"""
Desarrolla una funcion que determine la tempertura media,
el usuario deberá ingresar el número de días y las temperaturas
"""
def Temp_media(): 
    temperaturas = []
    days = int(input("Ingresa el número de días: "))
    for i in range(days):
        #temperatura = 
        temperaturas.append(float(input(f"Ingresa la temperatura del día {i}: ")))
    
    media = sum(temperaturas)/days
    return media

print(f"Temperatura media es {Temp_media()}")
