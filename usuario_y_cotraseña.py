# Diccionario para almacenar nombres de usuario y contraseñas
usuarios = {}

def main():
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

