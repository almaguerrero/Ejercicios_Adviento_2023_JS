"""
Hacer un programa que solicite un color por teclado
e imprima "puede pasar" si es amarillo, "no pasar" si es rojo
o "color inválido" si es cualquier color
"""
color = input('Dame un color:  ')
if color == "amarillo": 
    print("puede pasar")
elif color =="rojo":
    print("No puede pasar")
else:
    print("color inválido")