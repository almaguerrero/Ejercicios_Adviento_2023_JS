"""
crear una funcion EscribirCentrado, que reciba como parámetro un texto y lo escriba
centrado en la pantalla, suponiendo una anchura de 80 columnas
"""


def EscribirCentrado():
    texto = input('Ingresa un texto:  ')
    print(texto.center(80))

EscribirCentrado()
