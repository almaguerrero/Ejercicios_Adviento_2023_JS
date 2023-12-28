"""
Crear una funcion ConvertirEspaciado que reciba como parámetro un texto y devuelve 
una cadena con un espacio adicional dentras de cada letra
"""
def ConvertirEspaciado(texto):
    text_space = ""
    for letra in texto:
        text_space += letra + " "
    
    return text_space



texto_ori = input("Ingresa texto : ")
print(ConvertirEspaciado(texto_ori))