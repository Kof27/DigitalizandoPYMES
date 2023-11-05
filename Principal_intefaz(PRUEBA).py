from prendas import *
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#-------------------
#PRUEBA DE INTERFAZ
#------------------

#=============================================================
#DA
#Funciones del programa
#Variables fijas
ventas = []
usuarios = { "D": "1",  }
def InicioSesion(usuarios):
    usuario_ingresado = Nombre_usuario_String.get()
    contraseña_ingresada = Contraseña_usuario_String.get()
        # Solicitar al usuario que ingrese un nombre de usuario
    

        # Verificar si el nombre de usuario ya existe en el diccionario
    if usuario_ingresado in usuarios:
        if contraseña_ingresada == usuarios[usuario_ingresado]:
            messagebox.showinfo(title = " ", message = "bienvenido")
           
        elif contraseña_ingresada != usuarios[usuario_ingresado]:
            messagebox.showerror(title = " ", message = "Contraseña o usuario incorrecto")
            
            
    
def crear_usuario(nombre_usuario, contraseña, usuarios):
    if nombre_usuario in usuarios:
        messagebox.showerror(message = "El nombre de usuario ya existe.")
        Interfaz_Registro()
    else:
        usuarios[nombre_usuario] = contraseña
        messagebox.showinfo(message = "¡Usuario creado con éxito!")
        

def Ingreso_Ropa():
    Ingresar_Ropa = str(input("¿Desea ingresar nuevos producto?s [S/N]"))
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
        

#Interfaz funciones
def Interfaz_Registro():
    # Crear una nueva ventana para el registro
    ventana_registro = Toplevel(Pantalla_principal)
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("200x200")
    ventana_registro.resizable(False,False)
    
    marco_registro = Frame(ventana_registro)
    marco_registro.pack(pady=20)

    nombre_label = Label(marco_registro, text="Nombre de usuario", font="consola 12")
    nombre_label.pack()

    nombre_usuario_registro = StringVar()
    entry_nombre_usuario = Entry(marco_registro, width=20, textvariable=nombre_usuario_registro)
    entry_nombre_usuario.pack()

    contraseña_label = Label(marco_registro, text="Contraseña", font="consola 12")
    contraseña_label.pack()

    contraseña_registro = StringVar()
    entry_contraseña_registro = Entry(marco_registro, width=20, textvariable=contraseña_registro, show="*")
    entry_contraseña_registro.pack()

    Enviar_Datos = Button(ventana_registro, text = "Registrarse", command = lambda: [crear_usuario(nombre_usuario_registro.get(),contraseña_registro.get(),usuarios), ventana_registro.destroy()])#El ventana_registro.destroy() es para cerrar la pestaña despues de dar el boton 

    Enviar_Datos.pack()
    

#==============================ROOT INTERFAZ======================
Pantalla_principal = Tk()
Pantalla_principal.title("Programa")

    #Propiedades de la pantalla principal
Pantalla_principal.geometry("300x300")
Pantalla_principal.resizable(False,False)
#=================================================================



#==============================FRAMES======================
marco1 = Frame(Pantalla_principal)
marco1.pack(pady = 20)

marco2 = Frame(Pantalla_principal)
marco2.pack(pady = 5)

marco3 = Frame(Pantalla_principal)
marco3.pack(pady = 5)
#=================================================================

#==============================PESTAÑAS======================
    #Inicio sesión
Inicio_Sesion = Label(marco1, text = "Iniciar sesión", font = "Consola 14 bold")
Inicio_Sesion.pack()

    #Nombre 
Nombre_usuario = Label(marco1, text = "Nombre de usuario", font= "consola 12") .pack()
Nombre_usuario_String = StringVar()
string_entry_usuario = Entry(marco1, width = 20, textvariable = Nombre_usuario_String).pack()

    #Contraseña
Contraseña_usuario = Label(marco1, text = "Contraseña", font= "consola 12") .pack()
Contraseña_usuario_String = StringVar()
string_entry_Contraseña = Entry(marco1, width = 20, textvariable = Contraseña_usuario_String, show="*").pack()

    #Iniciar sesion
Boton_Iniciar_Sesion = Button(marco1, text = "Iniciar sesión", command = lambda: InicioSesion(usuarios))
Boton_Iniciar_Sesion.pack(pady = 10)
Boton_Registrarse = Button(marco1, text = "Registarse", command = Interfaz_Registro)
Boton_Registrarse.pack(pady = 2)

#=================================================================


#Bucle principal
Pantalla_principal.mainloop()



                

    
    

