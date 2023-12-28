"""
Crear una subrutina llamada login que recibe un nombre de usuario y una contraseña y devuelve
true si el nombre del usuario es usuario1 y la contraseña es asdasd. Además recibe el número 
de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este
valor. Crear un programa principal donde se pida un nombre de usuario y una contraseña
y se intente hacer login, solamente tenemos tres oportunidades
"""
def Login(user,password,attemps):
    if user == "usuario1" and password == "asdasd":
        print("login exitoso")
        return True
    else:
        print("INCORRECTO")
        attemps[0]+=1
        return False

def main():
    max_intentos = 3
    intentos = [0]  
    while intentos[0]<max_intentos:
        usuario_input = input("Nombre del usuario: ")
        pass_input = input("Contraseña: ")
        if Login(usuario_input,pass_input,intentos):
            break
        else:
            print(f"Intentos restantes : {max_intentos-intentos[0]}")
    
    if intentos[0]>= max_intentos:
        print("Numero de intentos alcanzados. Acceso denegado")

main()
