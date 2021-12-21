import os
import time
import enum

condicion1, condicion2, condicion3 = True, True, True

if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

#--------------------< GRAFFITIS >--------------------#

def titulo():
    print("""
        \t███████╗██████╗ ██╗   ██╗██╗  ██╗██╗██████╗ ███████╗
        \t██╔════╝██╔══██╗██║   ██║██║ ██╔╝██║██╔══██╗██╔════╝
        \t█████╗  ██║  ██║██║   ██║█████╔╝ ██║██║  ██║███████╗
        \t██╔══╝  ██║  ██║██║   ██║██╔═██╗ ██║██║  ██║╚════██║
        \t███████╗██████╔╝╚██████╔╝██║  ██╗██║██████╔╝███████║
        \t╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝""")

def games_title():
    print("""
    \t     ██ ██    ██ ███████  ██████   ██████  ███████ 
    \t     ██ ██    ██ ██      ██       ██    ██ ██      
    \t     ██ ██    ██ █████   ██   ███ ██    ██ ███████ 
    \t██   ██ ██    ██ ██      ██    ██ ██    ██      ██ 
    \t █████   ██████  ███████  ██████   ██████  ███████\n""")

def rachas_title():
    print("""
    \t██████   █████   ██████ ██   ██  █████      ██████  ███████     ██████  ███████  ██████  ██████  ███    ███ ██████  ███████ ███    ██ ███████  █████  ███████ 
    \t██   ██ ██   ██ ██      ██   ██ ██   ██     ██   ██ ██          ██   ██ ██      ██      ██    ██ ████  ████ ██   ██ ██      ████   ██ ██      ██   ██ ██      
    \t██████  ███████ ██      ███████ ███████     ██   ██ █████       ██████  █████   ██      ██    ██ ██ ████ ██ ██████  █████   ██ ██  ██ ███████ ███████ ███████ 
    \t██   ██ ██   ██ ██      ██   ██ ██   ██     ██   ██ ██          ██   ██ ██      ██      ██    ██ ██  ██  ██ ██      ██      ██  ██ ██      ██ ██   ██      ██ 
    \t██   ██ ██   ██  ██████ ██   ██ ██   ██     ██████  ███████     ██   ██ ███████  ██████  ██████  ██      ██ ██      ███████ ██   ████ ███████ ██   ██ ███████\n""") 

def matematicas_title():
    print("""
    \t     ██ ██    ██ ███████  ██████   ██████  ███████               ███    ███  █████  ████████ ███████ ███    ███  █████  ████████ ██  ██████  █████  ███████ 
    \t     ██ ██    ██ ██      ██       ██    ██ ██                    ████  ████ ██   ██    ██    ██      ████  ████ ██   ██    ██    ██ ██      ██   ██ ██      
    \t     ██ ██    ██ █████   ██   ███ ██    ██ ███████     █████     ██ ████ ██ ███████    ██    █████   ██ ████ ██ ███████    ██    ██ ██      ███████ ███████ 
    \t██   ██ ██    ██ ██      ██    ██ ██    ██      ██               ██  ██  ██ ██   ██    ██    ██      ██  ██  ██ ██   ██    ██    ██ ██      ██   ██      ██ 
    \t █████   ██████  ███████  ██████   ██████  ███████               ██      ██ ██   ██    ██    ███████ ██      ██ ██   ██    ██    ██  ██████ ██   ██ ███████\n""")

def lengua_title():
    print("""
    \t     ██ ██    ██ ███████  ██████   ██████  ███████               ██      ███████ ███    ██  ██████  ██    ██  █████  
    \t     ██ ██    ██ ██      ██       ██    ██ ██                    ██      ██      ████   ██ ██       ██    ██ ██   ██ 
    \t     ██ ██    ██ █████   ██   ███ ██    ██ ███████     █████     ██      █████   ██ ██  ██ ██   ███ ██    ██ ███████ 
    \t██   ██ ██    ██ ██      ██    ██ ██    ██      ██               ██      ██      ██  ██ ██ ██    ██ ██    ██ ██   ██ 
    \t █████   ██████  ███████  ██████   ██████  ███████               ███████ ███████ ██   ████  ██████   ██████  ██   ██\n""")

def ciencia_title():
    print("""
    \t    
    \t     ██ ██    ██ ███████  ██████   ██████  ███████                ██████ ██ ███████ ███    ██  ██████ ██  █████  
    \t     ██ ██    ██ ██      ██       ██    ██ ██                    ██      ██ ██      ████   ██ ██      ██ ██   ██ 
    \t     ██ ██    ██ █████   ██   ███ ██    ██ ███████     █████     ██      ██ █████   ██ ██  ██ ██      ██ ███████ 
    \t██   ██ ██    ██ ██      ██    ██ ██    ██      ██               ██      ██ ██      ██  ██ ██ ██      ██ ██   ██ 
    \t █████   ██████  ███████  ██████   ██████  ███████                ██████ ██ ███████ ██   ████  ██████ ██ ██   ██\n""")

def casual_title():
    print("""
    \t     ██ ██    ██ ███████  ██████   ██████  ███████                ██████  █████  ███████ ██    ██  █████  ██      
    \t     ██ ██    ██ ██      ██       ██    ██ ██                    ██      ██   ██ ██      ██    ██ ██   ██ ██      
    \t     ██ ██    ██ █████   ██   ███ ██    ██ ███████     █████     ██      ███████ ███████ ██    ██ ███████ ██      
    \t██   ██ ██    ██ ██      ██    ██ ██    ██      ██               ██      ██   ██      ██ ██    ██ ██   ██ ██      
    \t █████   ██████  ███████  ██████   ██████  ███████                ██████ ██   ██ ███████  ██████  ██   ██ ███████\n""")

#--------------------< MENÚS >--------------------#

# Aquí se encuentran todos los menús de la aplicación, todos se encargan de pedir una opción para seguir navegando infinitamente hasta que se quiera salir de la aplicación
def listado_usuarios():
    from pathlib import Path
    
    if not Path('listado_usuarios.txt').exists():
        file = open("listado_usuarios.txt","w")
        file.write("admin:contrasena;admin")
        file.close()

def main_menu(logged,User_dates):
    os.system(var) # Borra el terminal
    condicion = True
    
    if logged == False: # Comprueba si el usuario está loggeado
        while condicion:
            titulo() # Imprime un graffiti con el título de Edukids
            time.sleep(.4)
            print("\t\t\t\tBienvenido a EDUKIDS\n")
            time.sleep(.4)
            print("\t\t1.Juegos\n")
            time.sleep(.4)
            print("\t\t2.Iniciar sesión / Registrarse\n")
            time.sleep(.4)
            print("\t\t3.Salir\n")
            time.sleep(.4)
            opc = input("\t\tIntroduce una opción:\t")

            while opc != "1" and opc != "2" and opc != "3": # Valida que la opción introducida sea correcta
                os.system(var)
                titulo()
                print("\t\t\t\tBienvenido a EDUKIDS\n")
                print("\t\t1.Juegos\n")
                print("\t\t2.Iniciar sesión / Registrarse\n")
                print("\t\t3.Salir\n")
                time.sleep(0.2)
                opc = input("\t\tIntroduce una opción válida:\t")
            
            condicion = False
    else:
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")
        monedas = valores_usuario[11]
        
        while condicion:
            titulo() # Imprime un graffiti con el título de Edukids
            time.sleep(.4)
            print("\t\t\t\tBienvenido a EDUKIDS\n")
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            time.sleep(.4)
            print("\t\t1.Juegos\n")
            time.sleep(.4)
            print("\t\t2.Estadísticas\n")
            time.sleep(.4)
            print("\t\t3.Salir\n")
            time.sleep(.4)
            opc = input("\t\tIntroduce una opción:\t")

            while opc != "1" and opc != "2" and opc != "3": # Valida que la opción introducida sea correcta
                os.system(var)
                titulo()
                print("\t\t\t\tBienvenido a EDUKIDS\n")
                print(f"{name.title()}: {monedas}* Coins".rjust(100))
                print("\t\t1.Juegos\n")
                print("\t\t2.Estadísticas\n")
                print("\t\t3.Salir\n")
                time.sleep(0.2)
                opc = input("\t\tIntroduce una opción válida:\t")
            
            condicion = False
    
    return int(opc)

def category_menu(logged,User_dates):
    os.system(var)
    condicion = True
    
    if logged == True:
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")
        monedas = valores_usuario[11]
        while condicion:
            games_title()
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            time.sleep(0.2)
            print("\t\t1.Matemáticas\n")
            time.sleep(0.2)
            print("\t\t2.Lengua\n")
            time.sleep(0.2)
            print("\t\t3.Ciencia\n")
            time.sleep(0.2)
            print("\t\t4.Casual\n")
            time.sleep(0.2)
            print("\t\t5.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción:\t")

            while opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5":
                os.system(var)
                games_title()
                print(f"{name.title()}: {monedas}* Coins".rjust(100))
                print("\t\t1.Matemáticas\n")
                print("\t\t2.Lengua\n")
                print("\t\t3.Ciencia\n")
                print("\t\t4.Casual\n")
                print("\t\t5.Volver\n")
                time.sleep(0.2)
                opc = input("\t\tIntroduce una opción válida:\t")
            
            condicion = False
        return int(opc)
    else:
        print(f"\tPara jugar a los juegos debes iniciar sesión\n")
        stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
        
        return 5

def login_register_menu():
    os.system(var) # Borra el terminal
    condicion = True
    
    while condicion:
            titulo() # Imprime un graffiti con el título de Edukids
            print("\t\t\t\tBienvenido a EDUKIDS\n")
            time.sleep(.4)
            print("\t\t1.Iniciar sesión\n")
            print("\t\t2.Registrarse\n")
            print("\t\t3.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción:\t")

            while opc != "1" and opc != "2" and opc != "3": # Valida que la opción introducida sea correcta
                os.system(var)
                titulo()
                print("\t\t\t\tBienvenido a EDUKIDS\n")
                print("\t\t1.Iniciar sesión\n")
                print("\t\t2.Registrarse\n")
                print("\t\t3.Volver\n")
                time.sleep(0.2)
                opc = input("\t\tIntroduce una opción válida:\t")
            
            condicion = False
            
    return int(opc)

def login():
    os.system(var)
    time.sleep(.4)
    print(f"\t\t\t\tIniciar sesión\n")
    time.sleep(.4)
    user = input(f"\tIntroduce tu nombre de usuario:\t").lower().strip()
    encontrado = False
    try:
        with open('listado_usuarios.txt') as f:
            for linea in f:
                datos_usuario = linea.split(":")
                if datos_usuario[0] == user:
                    encontrado = True
                    break
        f.close()
    except:
            print(f"Ha habido un error :(")
    else:
        if encontrado == True:
            password = input(f"\tIntroduce la contraseña para {datos_usuario[0]}:\t")
            valores_usuario = datos_usuario[1].split(";")
            
            if valores_usuario[1] == password:
                print(f"\n\tBienvenid@ {user.title()}, has iniciado sesión satisfactoriamente!!\n")
                stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
                logged = True
                logged_User = [logged, datos_usuario]
                return logged_User
            else:
                print(f"\tUsuario o contraseña erróneo\n")
                stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
                logged = False
                logged_User = [logged, datos_usuario]
                return logged_User
        else:
            print(f"\n\tUsuario no encontrado\n")
            stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
            logged = False
            datos_usuario = []
            logged_User = [logged, datos_usuario]
            return logged_User

def register():
    os.system(var)
    time.sleep(.4)
    print(f"\t\t\t\tRegistrarse\n")
    time.sleep(.4)
    user = input(f"\tIntroduce tu nombre de usuario:\t").lower().strip()
    encontrado = False
    try:
        with open('listado_usuarios.txt') as f:
            for linea in f:
                datos_usuario = linea.split(":")
                if datos_usuario[0] == user:
                    encontrado = True
                    break
    except:
            print(f"Ha habido un error :(")
    else:
        if encontrado == True:
            print(f"\n\tYa existe un usuario con ese nombre, inicia sesión o prueba con otro nombre de usuario")
            stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
        else:
            f = open('listado_usuarios.txt','a')
            password = input(f"\tIntroduce una contraseña para {user}:\t")
            # Se guarda en 'listado_usuarios.txt' los valores de: nombre, password, puntos de las categorias, monedas, racha, juegos bloqueado (0) / desbloqueado (1)
            f.write(f"{user}:contrasena;{password};PMates;{1};PLengua;{1};PCiencia;{1};PCasual;{1};Monedas;{0};Racha;{1};MG1;{1};MG2;{1};MG3;{0};MG4;{0};LG1;{1};LG2;{0};CG1;{1};CG2;{0};CG3;{0};\n")
            print(f"\n\tUsuario registrado con éxito, inicia sesión y empieza a jugar\n")
            stop = input("\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 

def estadisticas(User_dates):
    import matplotlib.pyplot as plt
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    PLengua = int(valores_usuario[5])
    PMates = int(valores_usuario[3])
    PCiencia = int(valores_usuario[7])
    PCasual = int(valores_usuario[9])
    
    categorias = ['Lengua', 'Matemáticas', 'Ciencia', 'Casual']
    puntos = [PLengua, PMates, PCiencia, PCasual]
    
    plt.figure()
    plt.title("Estadísticas")
    plt.pie(puntos,labels=categorias, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

def rachas(User_dates):
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    racha = valores_usuario[13]
    if int(racha) <= 25:
        os.system(var)
        rachas_title()
        print("".rjust(173,"-"))
        if racha == "1":
            coins = 50
            print("\n")
            print(f"!!! Bienvenido {name.title()} a Edukids ¡¡¡".center(170))
            print("\n")
            print(f"Cómo es la primera vez que entras a divertirte te daremos {coins}* Coins".center(170))
            print("\n")
        elif int(racha) <= 4:
            coins = 10
            print("\n")
            print(f"Es la vez nº{racha} que entras a divertirte, aquí tienes {coins}* Coins".center(170))
            print("\n")
        elif int(racha) >= 5:
            coins = 25
            print("\n")
            print(f"Es la vez nº{racha} que entras a divertirte te daremos {coins}* Coins".center(170))
            print("\n")
        print("".rjust(173,"-"))
        
        f = open('listado_usuarios.txt','r')
        
        contenido_linea = []
        for linea in f:
            datos_usuario = linea.split(":")
            valores_usuario = datos_usuario[1].split(";")
            
            if datos_usuario[0] == name:
                valores_usuario[13] = int(valores_usuario[13]) + 1
                valores_usuario[11] = int(valores_usuario[11]) + coins
                insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
                User_dates = insertamos.split(":")
            else:
                insertamos = linea
            contenido_linea.append(insertamos)
        f.close()
        
        f = open('listado_usuarios.txt','w')
        for ind, val in enumerate(contenido_linea):
            f.writelines(contenido_linea[ind])
        f.close()
        
        stop = input("\n\n\t\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
        
        return User_dates

def matematicas(User_dates):
    os.system(var)
    condicion = True
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    monedas = valores_usuario[11]

    while condicion:
        matematicas_title()
        print(f"{name.title()}: {monedas}* Coins".rjust(100))
        time.sleep(0.2)
        print("\t\t1.Buscanúmeros\n")
        time.sleep(0.2)
        print("\t\t2.Sucesiones numéricas\n")
        time.sleep(0.2)
        print("\t\t3.Operaciones\n")
        time.sleep(0.2)
        print("\t\t4.Problemas matemáticos\n")
        time.sleep(0.2)
        print("\t\t5.Volver\n")
        time.sleep(0.2)
        opc = input("\t\tIntroduce una opción:\t")

        while opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5":
            os.system(var)
            matematicas_title()
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            print("\t\t1.Buscanúmeros\n")
            print("\t\t2.Sucesiones numéricas\n")
            print("\t\t3.Operaciones\n")
            print("\t\t4.Problemas matemáticos\n")
            print("\t\t5.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción válida:\t")
        
        condicion = False

        return int(opc)

def lengua(User_dates):
    os.system(var)
    condicion = True
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    monedas = valores_usuario[11]
    
    while condicion:
        lengua_title()
        print(f"{name.title()}: {monedas}* Coins".rjust(100))
        time.sleep(0.2)
        print("\t\t1.Ahorcado\n")
        time.sleep(0.2)
        print("\t\t2.Sinónimos\n")
        time.sleep(0.2)
        print("\t\t3.Volver\n")
        time.sleep(0.2)
        opc = input("\t\tIntroduce una opción:\t")

        while opc != "1" and opc != "2" and opc != "3":
            os.system(var)
            lengua_title()
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            print("\t\t1.Ahorcado\n")
            print("\t\t2.Sinónimos\n")
            print("\t\t3.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción válida:\t")
        
        condicion = False

        return int(opc)

def ciencia(User_dates):
    os.system(var)
    condicion = True
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    monedas = valores_usuario[11]
    
    while condicion:
        ciencia_title()
        print(f"{name.title()}: {monedas}* Coins".rjust(100))
        time.sleep(0.2)
        print("\t\t1.Preguntas de ciencia\n")
        time.sleep(0.2)
        print("\t\t2.Fechas históricas\n")
        time.sleep(0.2)
        print("\t\t3.Continentes\n")
        time.sleep(0.2)
        print("\t\t4.Volver\n")
        time.sleep(0.2)
        opc = input("\t\tIntroduce una opción:\t")

        while opc != "1" and opc != "2" and opc != "3" and opc != "4":
            os.system(var)
            ciencia_title()
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            print("\t\t1.Preguntas de ciencia\n")
            print("\t\t2.Fechas históricas\n")
            print("\t\t3.Continentes\n")
            print("\t\t4.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción válida:\t")
        
        condicion = False

        return int(opc)

def casual(User_dates):
    os.system(var)
    condicion = True
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    monedas = valores_usuario[11]
    
    while condicion:
        casual_title()
        print(f"{name.title()}: {monedas}* Coins".rjust(100))
        time.sleep(0.2)
        print("\t\t1.Trivial\n")
        time.sleep(0.2)
        print("\t\t2.Volver\n")
        time.sleep(0.2)
        opc = input("\t\tIntroduce una opción:\t")

        while opc != "1" and opc != "2":
            os.system(var)
            casual_title()
            print(f"{name.title()}: {monedas}* Coins".rjust(100))
            print("\t\t1.Trivial\n")
            print("\t\t2.Volver\n")
            time.sleep(0.2)
            opc = input("\t\tIntroduce una opción válida:\t")
        
        condicion = False

        return int(opc)


#--------------------< JUEGOS >--------------------#
#--------------------< MATEMATICAS >--------------------#
def buscanumeros(User_dates):
    import random
    os.system(var) # Se encarga de borrar la terminal
    condicion = True
    
    print("""\n\tBienvenido al buscanúmeros
    \tTendrás que adivinar el número oculto del 1 a 100""")

    num_oculto = random.randint(1,100) # Se genera un número random de 1 a 100

    while condicion:
        num = input(f"\t\t---> Introduce  un número:\t")

        while not num.isnumeric(): # Valida que se introduzca un número y no un caractér
            num = input(f"\t\t---> Introduce  un número:\t")
        
        num = int(num)

        if num < num_oculto: # Se evalua si el número introducido es mayor o menor o menor que el oculto y te da una pista para hallarlo
            print(f"\t---> Incorrecto, el número oculto es mayor que {num}") 
        elif num > num_oculto:
            print(f"\t---> Incorrecto, el número oculto es menor que {num}")
        else:
            condicion = False
    
    print(f"\t---> Correcto, el número oculto es {num}, has ganado 25* Coins")
    
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[3]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + 25
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()

    stop = input("\t\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
    
    return User_dates

def sucesiones(User_dates):
    os.system(var)
    import random
    sucesion = []
    numero = int(random.uniform(1,10))
    sucesion.append(numero)
    pista = int(random.uniform(2,4))
    multiplicador = int(random.uniform(2,5))
    for i in range(pista):
        actual = sucesion[i] * multiplicador
        sucesion.append(actual) 
    print("""\n\tBienvenido a Sucesiones
    \tTendrás que hallar la lógica detras de la sucesión y calcular el siguiente número de la misma""")
    print(f"\n\t\t{sucesion}")
    inputMultiplicador = int(input('\t\t¿Cual es el multiplicador de esta sucesion?: '))
    siguienteV = int(input('\t\t¿Cual es el siguiente numero de la sucesion?: '))
    if multiplicador == inputMultiplicador and sucesion[-1]*multiplicador == siguienteV:
        print('\n\t\tEnhorabuena has acertado la sucesion, has ganado 30* Coins')
        
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")
        
        f = open('listado_usuarios.txt','r')
            
        contenido_linea = []
        for linea in f:
            datos_usuario = linea.split(":")
            valores_usuario = datos_usuario[1].split(";")
            
            if datos_usuario[0] == name:
                valores_usuario[3] = int(valores_usuario[3]) + 1
                valores_usuario[11] = int(valores_usuario[11]) + 30
                insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
                User_dates = insertamos.split(":")
            else:
                insertamos = linea
            contenido_linea.append(insertamos)
        f.close()
        
        f = open('listado_usuarios.txt','w')
        for ind, val in enumerate(contenido_linea):
            f.writelines(contenido_linea[ind])
            
        f.close()
        stop = input("\t\tPulsa enter...")
        return User_dates
    else:
        print('\t\tVuelva a intentarlo')
        stop = input("\t\tPulsa enter...")

def operaciones(User_dates):
    os.system(var)
    import random
    print("""\n\tBienvenido a operaciones
    \tTendrás que realizar operaciones básicas de suma. resta, multiplicación y división\n""")
    coins = 0
    for i in range(5):
        operando = int(random.uniform(0,3))
        num1 = int(random.uniform(1,20))
        num2 = int(random.uniform(1,20))
        match operando:
            case 0:
                resInput = float(input(f"\t\t{str(num1)} + {str(num2)}:\t"))
                resultado = num1 + num2
                if resultado == resInput:
                    print(f'\n\t\tHas acertado, 5* Coins\n')
                    coins = coins +  5
                else:
                    print(f'\n\t\tFallaste, el resultado es {num1 + num2}\n')
            case 1:
                resInput = float(input(f"\t\t{str(num1)} - {str(num2)}:\t"))
                resultado = num1 - num2
                if resultado == resInput:
                    print(f'\n\t\tHas acertado, 5* Coins\n')
                    coins = coins +  5
                else:
                    print(f'\n\t\tFallaste, el resultado es {num1 - num2}\n')
            case 2:
                resInput = float(input(f"\t\t{str(num1)} * {str(num2)}:\t"))
                resultado = num1 * num2
                if resultado == resInput:
                    print(f'\n\t\tHas acertado, 5* Coins\n')
                    coins = coins +  5
                else:
                    print(f'\n\t\tFallaste, el resultado es {num1 * num2}\n')
            case 3:
                resInput = float(input(f"\t\t{str(num1)} / {str(num2)}:\t"))    
                resultado = num1 / num2
                if resultado == resInput:
                    print(f'\n\t\tHas acertado, 5* Coins\n')
                    coins = coins +  5
                else:
                    print(f'\n\t\tFallaste, el resultado es {num1 / num2}\n')
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[3]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + coins
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()
    stop = input("\t\tPulsa enter...")
    
    return User_dates

def problemas(User_dates):
    os.system(var)
    import random

    print("""\n\tBienvenido a problemas matemáticos
    \tEn este juego tendrás que resolver un problema matemático\n""")
    problemas = (
    '\n\tEn un tren había 200 personas. Al llegar a la estación bajaron 95 y subieron al tren 30. ¿Cuántas personas iban en el tren al salir de la estación?: ',
    '\n\tGabriel se ha comprado cromos de futbolista para coleccionar. Ha comprado 42 cromos y los quiere repartir y pegar en 7 páginas de su cuaderno de cromos ¿Cuanto cromos podra poner en cada pagina?: ',
    '\n\tEn una panaderia, se hornean 2500 panes al dia. Esta mañana se han quemado 227 panes ¿Cuantos panes no se han quemado?: ',
    '\n\tSusana te ha preguntado a su profesora que número se obtiene si a 500000 le sumas 200, 40000, 70,5 y 8000 ¿Qué número se obtiene?: ',
    '\n\t¿Cuantas personas podran viajar sentados en 9 autocares si cada uno hay 54 asientos?: ',
    '\n\tMi hermano compro 18 lapices y 5 cuadernos. Cada lapiz costó 80 centimos y cada cuaderno 2€, ¿Cuanto pago por toda la compra?: '
    )
    resultados = (135,6,2273,548275,486,24.4)
    problema = int(random.uniform(0,(len(problemas)-1)))
    resultado = int(input(problemas[problema]))
    if resultado == resultados[problema]:
        print('\n\tEnhorabuena has acertado el problema, 40* Coins')
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")

        f = open('listado_usuarios.txt','r')

        contenido_linea = []
        for linea in f:
            datos_usuario = linea.split(":")
            valores_usuario = datos_usuario[1].split(";")

            if datos_usuario[0] == name:
                valores_usuario[3] = int(valores_usuario[3]) + 1
                valores_usuario[11] = int(valores_usuario[11]) + 40
                insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
                User_dates = insertamos.split(":")
            else:
                insertamos = linea
            contenido_linea.append(insertamos)
        f.close()

        f = open('listado_usuarios.txt','w')
        for ind, val in enumerate(contenido_linea):
            f.writelines(contenido_linea[ind])

        f.close()
        stop = input("\tPulsa enter...")
        return User_dates
    else:
        print('\n\tFallaste el resultado correcto era: '+str(resultados[problema]))
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")

        f = open('listado_usuarios.txt','r')

        contenido_linea = []
        for linea in f:
            datos_usuario = linea.split(":")
            valores_usuario = datos_usuario[1].split(";")

            if datos_usuario[0] == name:
                valores_usuario[3] = int(valores_usuario[3]) + 0
                valores_usuario[11] = int(valores_usuario[11]) + 0
                insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
                User_dates = insertamos.split(":")
            else:
                insertamos = linea
            contenido_linea.append(insertamos)
        f.close()

        f = open('listado_usuarios.txt','w')
        for ind, val in enumerate(contenido_linea):
            f.writelines(contenido_linea[ind])

        f.close()
        stop = input("\tPulsa enter...")
        return User_dates

#--------------------< LENGUA >--------------------#
def sinonimos(User_dates) :
  os.system(var)
  import random
  preguntas = {"\ngaraje\n" : ["a)calle \n","b)cochera \n", "c) casa \n", "b"],"\ngeneroso\n" : ["a)amable\n","b)humilde\n","c)sociable\n","b"],"\ngigante\n" :	["a)pequeño\n","b)delgado\n","c)enorme\n","c"],"\ngordo" :	["a)obeso\n","b)flaco\n","c)delgado\n","a"],"\nhumildad\n" :	["a)amabilidad\n","b)delgadez\n","c)modestia\n","c"],"\nidéntico\n" :	["a)distinto\n","b)igual\n","c)inteligente\n","b"],
                "\nidioma\n" :	["a)inglés\n", "b)español\n","c)lengua","c"],"\niluminar\n" :	["a)alumbrar\n","b)oscurecer\n","c)permanecer\n","a"],"\nimporte\n"	: ["a)valor\n","b)cuenta\n","c)dinero\n","a"],"\nincreíble" :	["a)aburrido\n","b)creíble\n","c)impresionante\n","c"],"\nindicio\n" :	["a)comienzo\n","b)final\n","c)pista\n","c"],
                "\norar\n" :	["a)hablar\n","b)rezar\n","c)susurrar\n","b"],"\npágina\n" :	["a)libro\n","b)cara\n","c)hoja\n","c"],"\nparar\n" :	["a)detener\n","b)seguir\n","c)empezar\n","a"],"\npartir\n" :	["a)dividir\n","b)unir\n","c)desplazar\n","a"],
                "\npaz\n"	: ["a)desorden\n","b)guerra\n","c)tranquilidad\n","c"],"\npelo\n" :	["a)cabeza\n","b)cara\n","c)cabello\n","c"]}
  
  preguntas_usadas = []

  while len(preguntas_usadas) < 5:
    num_pregunta = list(random.choice(list(preguntas.items())))
    if num_pregunta not in preguntas_usadas:
      preguntas_usadas.append(num_pregunta)

  print("Bienvenid@ a Sinónimos!")
  print("Selecciona la respuesta correcta\n")
  
  coins = 0
  while True :
    for i in range(0,5):
      respuestas = preguntas_usadas[0 + i]
      print(respuestas[0])
      respuesta = respuestas[1]
      print(respuesta[0])
      print(respuesta[1])
      print(respuesta[2])
      respuestaf = input("--->")
      respuestam = respuestaf.lower()
      if respuestam == respuesta[3]:
        print("\n¡Correcto! 5* Coins")
        coins += 5
      else:
        print("\nincorrecto")	 
    break
  name = User_dates[0]
  valores_usuario = User_dates[1].split(";")
  f = open('listado_usuarios.txt','r')
  contenido_linea = []
  for linea in f:
      datos_usuario = linea.split(":")
      valores_usuario = datos_usuario[1].split(";")
      if datos_usuario[0] == name:
          valores_usuario[3] = int(valores_usuario[5]) + 1
          valores_usuario[11] = int(valores_usuario[11]) + coins
          insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
          User_dates = insertamos.split(":")
      else:
          insertamos = linea
      contenido_linea.append(insertamos)
  f.close()
  f = open('listado_usuarios.txt','w')
  for ind, val in enumerate(contenido_linea):
      f.writelines(contenido_linea[ind])
  f.close()
  stop = input("\n\tPulsa enter...")
  return User_dates

def ahorcado(User_dates):
  os.system(var)
  import random
  def normalize(s):
      replacements = (
          ("á", "a"),
          ("é", "e"),
          ("í", "i"),
          ("ó", "o"),
          ("ú", "u"),)
  palabras = ["morsa", "proyector", "elefante","tigre","cocodrilo","abuelo","pantalla","pizarra","platano","reloj","zapato","muñeca","pelicula","hipopotamo","camiseta","pradera","laguna","pulsera","ordenador","acondicionamineto","escritura","manzana","abrigo"]
  palabra = random.choice(palabras)
  tupalabra = ''
  print("\tBienvenid@ al Ahorcado!")
  print("\tComienza a adivinar")
  vidas = 7
  
  while vidas > 0:
    fallas=0
    for letra in palabra:
      if letra in tupalabra :
        print(letra,end="")
      else:
        print("*", end="")
        fallas+=1
    if fallas==0:
        print("")
        print("\n\tFelicidades, ganaste 50* Coins!")
        name = User_dates[0]
        valores_usuario = User_dates[1].split(";")
        f = open('listado_usuarios.txt','r')
        contenido_linea = []
        for linea in f:
            datos_usuario = linea.split(":")
            valores_usuario = datos_usuario[1].split(";")
            if datos_usuario[0] == name:
                valores_usuario[3] = int(valores_usuario[5]) + 1
                valores_usuario[11] = int(valores_usuario[11]) + 50
                insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
                User_dates = insertamos.split(":")
            else:
                insertamos = linea
            contenido_linea.append(insertamos)
        f.close()
        f = open('listado_usuarios.txt','w')
        for ind, val in enumerate(contenido_linea):
            f.writelines(contenido_linea[ind])
        f.close()
        return User_dates
        break
    tuletra=input("\n\tIntroduce una letra:\t")
    tupalabra+=tuletra
    if tuletra not in palabra:
        vidas-=1
        print("\tEquivocación")
        print("\tTienes",+vidas,"vidas")
    if vidas == 1:
        print("""
                         ___
                        |   |
                       _O/  |
                        |   |
                       / \  |
                      ______|
          """)
    elif vidas == 2:
        print("""
                         ___
                        |   |
                       _O/  |
                        |   |
                         \  |
                      ______|
          """)
    elif vidas == 3:
        print("""
                         ___
                        |   |
                       _O/  |
                        |   |
                            |
                      ______|
          """)
    elif vidas == 4 :
       print("""
                         ___
                        |   |
                       _O/  |
                            |
                            |
                      ______|
          """)
    elif vidas == 5:
        print("""
                         ___
                        |   |
                        O/  |
                            |
                            |
                      ______|
          """)
    elif vidas == 6:
        print("""
                         ___
                        |   |
                        O   |
                            |
                            |
                      ______|
          """)
    if vidas == 0:
        print("\n\tPerdiste :(")
  else:
    print("\n\tGracias por participar")
  stop = input("\tPulsa enter...")

#--------------------< CIENCIA >--------------------#
# Los juegos de ciencias se basan en la misma función para hacer preguntas

def science_questions(User_dates):
    import random
    os.system(var)
    coins = 0
    print("""\n\tBienvenido a preguntas de ciencia
    \tTendrás que resolver 5 preguntas generelas de ciencia\n""")

    # En este diccionario se almacenan las preguntas
    # Formato de las preguntas número de pregunta : ['pregunta',número de opciones (3 o 2), 'a) ', 'b) ', 'c) ', 'la opción correcta']
    preguntas = { 
        1: ["¿Qué utilizan los peces para respirar?",3,"\n\ta) Pulmones","\n\tb) La boca", "\n\tc) Branquias", "c"],
        2: ["¿Cuál es el animal más alto de la Tierra de entre los que viven fuera del mar?",3,"\n\ta) La jirafa","\n\tb) El elefante", "\n\tc) El oso polar", "a"],
        3: ["¿Para qué sirve la raíz de las plantas?",3, "\n\ta) Para absorber agua de la tierra", "\n\tb) Para poder reproducirse", "\n\tc) Para hacer la fotosíntesis", "a"],
        4: ["¿Cómo se llaman los árboles que pierden la hoja?",2, "\n\ta) Árboles de hoja caduca", "\n\tb) Árboles de hoja perenne", "a"],
        5: ["¿El delfín es un pez o un mamífero?",2, "\n\ta) Pez", "\n\tb) Mamífero", "b"],
        6: ["¿Verdadero o falso? Todos los insectos tienen dos antenas y 6 patas",2,"a) Verdadero","b) Falso","b"]
    }

    preguntas_usadas = [] # Se crea una lista vacía para generar el orden de las preguntas sin que se repitan al ejecutarse

    while len(preguntas_usadas) < 5: 
        num_pregunta = random.randint(1,len(preguntas))

        if num_pregunta not in preguntas_usadas:
            preguntas_usadas.append(num_pregunta)

    for i in range(0,5): # Se generan 5 preguntas
        
        if preguntas[preguntas_usadas[i]][1] == 3: # Se evalua el número de opciones que tiene la pregunta en este caso 3

            # Se escribe la pregunta y sus opciones
            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}{preguntas[preguntas_usadas[i]][3]}{preguntas[preguntas_usadas[i]][4]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b" or respuesta == "c": # Evalua que el usuario introduzca 'a' 'b' o 'c'
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][5]: # Valida que la respuesta introducida es igual a la respuesta de la pregunta en el diccionario
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")

        elif preguntas[preguntas_usadas[i]][1] == 2: # Aquí se evalua el número de opciones que tiene la pregunta en este caso 2

            # Se escribe la pregunta y sus opciones
            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}\n{preguntas[preguntas_usadas[i]][3]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b":
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][4]:
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[7]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + coins
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()
    stop = input("\t\tPulsa enter...") # Esto detiene la función hasta que el usuario quiera continuar 
    return User_dates

def historic_dates(User_dates):
    import random
    os.system(var)
    coins = 0
    print("""\n\tBienvenido a fechas históricos
    \tTendrás que resolver 5 preguntas generelas de fechas históricas\n""")

    #formato de las preguntas número de pregunta : ['pregunta',número de opciones (3 o 2), 'a) ', 'b) ', 'c) ', 'la opción correcta']
    preguntas = { 
        1: ["Caída del Imperio Romano",3,"\n\ta) 318","\n\tb) 711", "\n\tc) 476", "b"],
        2: ["Actual Constitución Española",3,"\n\ta) 1978","\n\tb) 1975", "\n\tc) 1977", "a"],
        3: ["Descubrimiento de América",3, "\n\ta) 1592", "\n\tb) 1492", "\n\tc) 1612", "b"],
        4: ["Llegada de los romanos a la Península",3, "\n\ta) 218 a.c", "\n\tb) 218","\n\tc) 11", "a"],
        5: ["Entrada en circulación del euro",3, "\n\ta) 1999", "\n\tb) 2002","\n\tc) 2000", "c"],
        6: ["Segunda Guerra Mundial",3,"\n\ta) 1939-1945","\n\tb) 1936-1939", "\n\tc) 1929-1945", "a"],
        7: ["Rendición de Granada",3,"\n\ta) 1491","\n\tb) 1492", "\n\tc) 1612", "a"],
        8: ["Guerra civil española",3,"\n\ta) 1898-1908","\n\tb) 1975-1978", "\n\tc) 1936-1939", "c"]
    }

    preguntas_usadas = []

    while len(preguntas_usadas) < 5:
        num_pregunta = random.randint(1,len(preguntas))

        if num_pregunta not in preguntas_usadas:
            preguntas_usadas.append(num_pregunta)

    for i in range(0,5): #5 preguntas
        
        if preguntas[preguntas_usadas[i]][1] == 3:

            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}{preguntas[preguntas_usadas[i]][3]}{preguntas[preguntas_usadas[i]][4]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b" or respuesta == "c":
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][5]:
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")

        elif preguntas[preguntas_usadas[i]][1] == 2:

            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}{preguntas[preguntas_usadas[i]][3]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b":
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][4]:
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[7]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + coins
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()
    stop = input("\t\tPulsa enter...")
    return User_dates

def countries_questions(User_dates):
    import random
    os.system(var)
    coins = 0
    print("""\n\tBienvenido a geografía
    \tTendrás que resolver 5 preguntas generelas de geografia\n""")

    #formato de las preguntas número de pregunta : ['pregunta',número de opciones (3 o 2), 'a) ', 'b) ', 'c) ', 'la opción correcta']
    preguntas = { 
        1: ["¿Cual es la capital de Rumania?",3,"\n\ta) Bucarest ","\n\tb) Moscú", "\n\tc) Ankara", "a"],
        2: ["¿A que país pertenece la ciudad de Helsinki?",3,"\n\ta) Australia ","\n\tb) Estados unidos", "\n\tc) Finlandia", "c"],
        3: ["¿Que idioma es el más hablado en el mundo?",3, "\n\ta) Chino", "\n\tb) Ingles", "\n\tc) Hindi", "b"],
        4: ["¿Cuál es la actual capital de Brasil?",3, "\n\ta) Rio de Janeiro", "\n\tb) Tokio", "\n\tc) Paíis", "a"],
        5: ["¿Qué país es el más grande del planeta?",3, "\n\ta) EEUU", "\n\tb) Rusia", "\n\tc) Australia", "b"],
        6: ["¿En qué océano se encuentra Sri Lanka?",3, "\n\ta) Adriatico", "\n\tb) Índico", "\n\tc) Pacífico", "b"],
        7: ["¿Cómo se llama la capital de Mongolia?",3, "\n\ta) Ulaanbaatar ", "\n\tb) Osaka", "\n\tc) Bangkok", "a"],
        8: ["¿El vudú se considera una religión originaria en qué lugar?",3, "\n\ta)America ", "\n\tb) Oriente", "\n\tc) África Occidental", "c"],
        9: ["¿Cuál es la capital actual de Marruecos?",3, "\n\ta) Rabat", "\n\tb) Casa blanca", "\n\tc) Marrakech ", "a"],
        10: ["¿Qué idioma europeo es una lengua oficial en Sudáfrica?",3, "\n\ta) Español", "\n\tb) Afrikáans", "\n\tc) Frances", "b"]
    }

    preguntas_usadas = []

    while len(preguntas_usadas) < 5:
        num_pregunta = random.randint(1,len(preguntas))

        if num_pregunta not in preguntas_usadas:
            preguntas_usadas.append(num_pregunta)

    for i in range(0,5): #5 preguntas
        
        if preguntas[preguntas_usadas[i]][1] == 3:

            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}{preguntas[preguntas_usadas[i]][3]}{preguntas[preguntas_usadas[i]][4]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b" or respuesta == "c":
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][5]:
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")

        elif preguntas[preguntas_usadas[i]][1] == 2:

            print(f"\tPregunta {i+1}: {preguntas[preguntas_usadas[i]][0]}\n{preguntas[preguntas_usadas[i]][2]}{preguntas[preguntas_usadas[i]][3]}")
            condicion = True

            while condicion:
                respuesta = input("\n\t---> Introduce la respuesta:\t").lower()
                
                if respuesta == "a" or respuesta == "b":
                    condicion = False
                
            if respuesta == preguntas[preguntas_usadas[i]][4]:
                print("\n\t\t---> Correcto, 5* Coins\n")
                coins += 5
            else:
                print("\n\t\t---> Incorrecto\n")
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[7]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + coins
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()
    stop = input("\tPulsa enter...")
    return User_dates

#--------------------< CASUAL >--------------------#
def trivial(User_dates):
    os.system(var)
    import random
    coins = 0
    print("Bienvenido a Trivial Pursuit")
    diccionario = {"Cual es el Descubridor de America?" : "Cristobal Colón", "Quien fue el primer rey borbon?" : "Felipe V", 
                    "Donde esta Transilvania?" : "En Rumania", "Que Rio pasa por Paris?": "El Sena", "Cual es la raiz cuadrada de 100? " : "10",
                    "Quien fue una de las	personas mas importantes de las matematicas de España?" : "Torres Quevedo",
                    "Cual es el pasado del verbo coger?" : "Caught", "Que significa must?" : "Deber", "Cual es el arbol mas grande del mundo?" : "El Secuoya",
                    "Dí el nombre de la parte de la planta que esta bajo tierra" : "Raíz", "Que programa de programacion el icono es un gato?" : "Scratch",
                    "Que animal es el logo de Linux ?" : "Un pingüino", "Una persona importante en el mundo de Fisica, inventor de la teoría de la realtividad " : "Einstein",
                    "Cuantos generos de palanca hay?": "3", "Que músico se quedó sordo y compuso 9 sinfonías" : "Beethoven" ,
                    "Que palabra es : la" : "Un Artículo","Que tipo de palabra es : de" : "Una Preposición", "Cual es la capital de Alemania" : "Berlín",
                    "Cual es la capital de Islandia?" : "Reiquiavik", }
    
    for i in range(0,5):
        pregunta = list(random.choice(list(diccionario.items())))
        print(pregunta[0])
        respuesta = input("--->")
        respuestam = respuesta.lower()
        if respuesta == pregunta[1].lower():
            print("¡Correcto! 5* Coins")
            coins += 5
        else:
            print("incorrecto")
    name = User_dates[0]
    valores_usuario = User_dates[1].split(";")
    
    f = open('listado_usuarios.txt','r')
        
    contenido_linea = []
    for linea in f:
        datos_usuario = linea.split(":")
        valores_usuario = datos_usuario[1].split(";")
        
        if datos_usuario[0] == name:
            valores_usuario[3] = int(valores_usuario[9]) + 1
            valores_usuario[11] = int(valores_usuario[11]) + coins
            insertamos = f"{name}:{valores_usuario[0]};{valores_usuario[1]};{valores_usuario[2]};{valores_usuario[3]};{valores_usuario[4]};{valores_usuario[5]};{valores_usuario[6]};{valores_usuario[7]};{valores_usuario[8]};{valores_usuario[9]};{valores_usuario[10]};{valores_usuario[11]};{valores_usuario[12]};{valores_usuario[13]};{valores_usuario[14]};{valores_usuario[15]};{valores_usuario[16]};{valores_usuario[17]};{valores_usuario[18]};{valores_usuario[19]};{valores_usuario[20]};{valores_usuario[21]};{valores_usuario[22]};{valores_usuario[23]};{valores_usuario[24]};{valores_usuario[25]};{valores_usuario[26]};{valores_usuario[27]};{valores_usuario[28]};{valores_usuario[29]};{valores_usuario[30]};{valores_usuario[31]};\n"
            User_dates = insertamos.split(":")
        else:
            insertamos = linea
        contenido_linea.append(insertamos)
    f.close()
    
    f = open('listado_usuarios.txt','w')
    for ind, val in enumerate(contenido_linea):
        f.writelines(contenido_linea[ind])
        
    f.close()
    stop = input("\t\tPulsa enter...")
    return User_dates