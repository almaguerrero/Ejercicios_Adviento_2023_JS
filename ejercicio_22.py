"""
Escribir dos funciones que permitan calcular:
la cantidad de segundos en tiempo dado en horas, minutos y segundos
la cantidad de horas, minutos y segundos de un tiempo dado en segundos
Escribe un programa principal con un menu donde se pueda elegir la opción de 
convertir a segundos,y convertir a horas minutos y segundos o salir del programa
"""
def secondsToHrs():
    segundos = float(input("Ingresa los segundos: "))
    horas = segundos //3600
    minutos = (segundos % 3600) //60
    segundos_resto = segundos % 60
    print(f"horas:  {horas}, minutos {minutos}, segundos {segundos_resto}")

def hrsToSeconds():
    horas = float(input("Ingresa las horas: "))
    minutos = float(input("Ingresa los minutos: "))
    segundos = float(input("Ingresa los segundos: "))
    print (f"la cantidad de segundos son: {(horas*3600)+ (minutos*60)+segundos}")

def main():
    menu = {
        1: secondsToHrs,
        2: hrsToSeconds
    }

    while True:
        print("Menu:    ")
        print("1.- Segundos a horas, minutos y segundos")
        print("2.- Horas, minutos y segundos a segundos")
        print("Presiona 3 para salir")
        seleccion = int(input("Selecciona una opción"))

        if seleccion == 3:
            break
        if seleccion == 1:
            secondsToHrs()
        if seleccion == 2:
            hrsToSeconds()

if __name__ == "__main__":
    main()



