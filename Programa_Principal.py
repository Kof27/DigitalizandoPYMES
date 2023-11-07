from prendas import *
from tkinter import *
#------------------------

#-----------------------

#Variables fijas
ventas = []

def InicioSesion():
    usuarios = {
        "D": "1"
    }
    while True:
        # Solicitar al usuario que ingrese un nombre de usuario
        nombre_usuario = input("Ingresa tu nombre de usuario: ")

        # Verificar si el nombre de usuario ya existe en el diccionario
        if nombre_usuario in usuarios:
            print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
            contrasena = input("Ingresa tu contraseña: ")

            # Verificar la contraseña
            if contrasena == usuarios[nombre_usuario]:
                print("Acceso concedido.")
                break
            else:
                print("Contraseña incorrecta. Intenta de nuevo.")
        else:
            print("Nombre de usuario no encontrado. Crearemos uno nuevo.")
            contrasena = input("Crea una contraseña: ")
            usuarios[nombre_usuario] = contrasena
            print("¡Cuenta creada con éxito!")

        # Preguntar si el usuario desea modificar la contraseña
        cambiar_contrasena = input("¿Deseas cambiar tu contraseña? (Sí/No): ")
        if cambiar_contrasena.lower() == "si":
            nueva_contrasena = input("Ingresa tu nueva contraseña: ")
            usuarios[nombre_usuario] = nueva_contrasena
            print("Contraseña modificada con éxito.")

        # Preguntar si el usuario desea salir del programa
        salir = input("¿Quieres salir del programa? (Sí/No): ")
        if salir.lower() == "si":
            break

def Ingreso_Ropa():
    
    Ingresar_Ropa = str(input("¿Desea ingresar nuevos productos? [S/N]"))
    if Ingresar_Ropa.upper() == "S":
        marca = input(str("Introduce la marca: "))
        tipo = input(str("Introduce el tipo de prenda:"))
        color = input(str("Introduce el color de la prenda: "))
        talla = input(str("Introduce la talla de la prenda: "))
            
        Prenda_Nueva = Prendas(marca,tipo,color,talla)
        Prenda_Nueva.Asignar_Codigo()

        
        #Imprimir prendas creadas
        for prenda in Prendas.Prendas_Creadas:
            print(f"Marca: {prenda.marca}, Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}")
    elif Ingresar_Ropa == "N":
        print("Hasta luego")
        
    else:
        print("Valor no reconocido, vuelve a intentar")
        
def Buscar_Prenda_Por_Codigo():
    Codigo_a_buscar = input(str("Introduce el codigo de la prenda que buscas "))
    
    for prenda in Prendas.Prendas_Creadas:
        if prenda.Asignar_Codigo() == Codigo_a_buscar:
            print(f"Prenda encontrada - Marca: {prenda.marca}, "
                    f"Tipo: {prenda.tipo}, Color: {prenda.color}, "
                    f"Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}")
            return
        else:
            print("Prenda no encontrada")

def Generar_Venta():
    # Solicitar el nombre del cliente
    cliente = input("Nombre del cliente: ")

    # Solicitar el correo electrónico del cliente con validación básica
    while True:
        email_usuario = input("Por favor, introduce tu correo: ")
        if "@" in email_usuario and "." in email_usuario:
            print("Acceso garantizado")
            break
        else:
            print("Acceso no garantizado. El correo electrónico debe contener '@' y '.'.")

    # Mostrar la lista de prendas disponibles
    print("Lista de prendas disponibles:")
    for prenda in Prendas.Prendas_Creadas:
        print(f"Código: {prenda.Asignar_Codigo()}, Marca: {prenda.marca}, "
              f"Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}")

    # Solicitar al usuario que elija una prenda por su código
    codigo_a_vender = input("Introduce el código de la prenda que desea comprar: ")

    # Buscar la prenda en la lista
    prenda_a_vender = None
    for prenda in Prendas.Prendas_Creadas:
        if prenda.Asignar_Codigo() == codigo_a_vender:
            prenda_a_vender = prenda
            break

    # Si se encontró la prenda, generar un recibo y eliminar la prenda de la lista
    if prenda_a_vender:
        recibo = f"Recibo de Venta\nCliente: {cliente}\nCorreo: {email_usuario}\n" \
                 f"Prenda: {prenda_a_vender.marca} {prenda_a_vender.tipo} " \
                 f"{prenda_a_vender.color} {prenda_a_vender.talla}\n" \
                 f"Código: {prenda_a_vender.Asignar_Codigo()}"

        print(recibo)

        # Eliminar la prenda de la lista
        Prendas.Prendas_Creadas.remove(prenda_a_vender)
        print("Prenda vendida y eliminada de la lista.")
    else:
        print("Prenda no encontrada.")

#--------------
#Probar el codigo
def Test():
    InicioSesion()
    while True:
        Ingreso_Ropa()
        Buscar_Prenda_Por_Codigo()
        Generar_Venta()
                

Test()
    

