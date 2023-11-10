from prendas import *
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk

#-------------------
#PRUEBA DE INTERFAZ
#------------------

# Variables globales
# =============================================================
usuario_autenticado = False
estado_entry = "disabled"
# =============================================================
#Variables fijas
ventas = []
usuarios = { "D": "1",  }

#==================FUNCIONES DEL PROGRAMA=========================================

    #---------------Iniciar sesión y creación de usuarios------------------------------
def InicioSesion(usuarios,Nombre_usuario_String,Contraseña_usuario_String,Iniciar_sesion_interfaz):
    usuario_ingresado = Nombre_usuario_String.get()
    contraseña_ingresada = Contraseña_usuario_String.get()
        # Solicitar al usuario que ingrese un nombre de usuario
    

        # Verificar si el nombre de usuario ya existe en el diccionario
    if usuario_ingresado in usuarios:
        if contraseña_ingresada == usuarios[usuario_ingresado]: #ESTO SOLO COMPRUEBA SI EL USUARIO FUE ENCONTRAD
            messagebox.showinfo(title = " ", message = "bienvenido")
            #-----------Activar los entrys----------
            Buscar_ropa_entrada = Entry(Buscar_ropa, textvariable=codigo_buscado_var, state = "normal").grid(row=0, column=1, padx=6)
            Marca_prenda = Entry(Opcion1_Frame, textvariable=Marca_prenda_input,state = "normal").grid(row=3, column=0, padx=5, pady=2)
            Tipo_Prenda = Entry(Opcion1_Frame, textvariable=Tipo_prenda_input,state = "normal").grid(row=4, column=0, padx=10)
            Talla_Prenda = Entry(Opcion1_Frame, textvariable=Talla_prenda_input,state = "normal").grid(row=5, column=0, padx=10)
            Color_Prenda = Entry(Opcion1_Frame, textvariable=Color_prenda_input, state = "normal").grid(row=6, column=0, padx=10)
            Iniciar_sesion_interfaz.destroy()
            
        elif contraseña_ingresada != usuarios[usuario_ingresado]:
            print("sesión incorrecta")
            messagebox.showerror(title = "", message = "Contraseña incorrecta")
    else: #si el usuario no se encuentra
        messagebox.showerror(title = "", message = "Usuario no encontrado")
        
          

def crear_usuario(nombre_usuario, contraseña, usuarios):
    if nombre_usuario in usuarios:
        messagebox.showerror(message = "El nombre de usuario ya existe.")
        Interfaz_Registro()
    else:
        usuarios[nombre_usuario] = contraseña
        messagebox.showinfo(message = "¡Usuario creado con éxito!")

    #------------------------------------------------------      

def Ingreso_Ropa():
    marca = Marca_prenda_input.get()
    tipo = Tipo_prenda_input.get()
    color = Color_prenda_input.get()
    talla = Talla_prenda_input.get()
            
    Prenda_Nueva = Prendas(marca,tipo,color,talla)
    Prenda_Nueva.Asignar_Codigo()
    messagebox.showinfo(title = "", message = "Prenda añadida con exito")

        
        #Imprimir prendas creadas
    for prenda in Prendas.Prendas_Creadas:
            print(f"Marca: {prenda.marca}, Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}")
    Marca_prenda_input.set("")
    Tipo_prenda_input.set("")
    Talla_prenda_input.set("")
    Color_prenda_input.set("")



def Inventario_prendas():
    Inventario_Interfaz = Tk()
    Inventario_Interfaz.geometry("600x400")
    
    Inventario = LabelFrame(Inventario_Interfaz, text="Prendas guardadas")
    Inventario.pack(expand=YES, fill=BOTH)

    # Crear el Listbox
    Inventario_publico = Listbox(Inventario, font="Consolas 12", selectbackground="lightblue", selectmode="extended")
    
    # Configurar el Scrollbar
    scrollbar = Scrollbar(Inventario, orient=VERTICAL, command=Inventario_publico.yview)
    Inventario_publico.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=RIGHT, fill=Y)
    Inventario_publico.pack(expand=YES, fill=BOTH)

    for prenda in Prendas.Prendas_Creadas:
        info_str = f"Marca: {prenda.marca}\n Tipo: {prenda.tipo}\n Color: {prenda.color}\n Talla: {prenda.talla}\n Código: {prenda.Asignar_Codigo()}\n"
        Inventario_publico.insert(END, info_str)
        Inventario_publico.insert(END, "")  # Insertar una línea en blanco adicional para separar las prendas

    Inventario_Interfaz.mainloop()



def Mostrar_detalles():
        
    codigo_buscado = codigo_buscado_var.get()
    
    print("Código a buscar:", repr(codigo_buscado))  # Utilizar respr() para imprimir caracteres especiales

    print(Prendas.Prendas_Creadas)
    # Variable para realizar un seguimiento de si se encontró una coincidencia
    encontrada_coincidencia = False

    for prenda in Prendas.Prendas_Creadas:
        print("Código de la prenda:", repr(prenda.Asignar_Codigo()))

        if prenda.Asignar_Codigo() == codigo_buscado:
            ventana_detalle = Toplevel()
            ventana_detalle.geometry("300x200")
            ventana_detalle.title("Detalles de la prenda")

            Label(ventana_detalle, text=f"Tipo: {prenda.tipo}").pack()
            Label(ventana_detalle, text=f"Color: {prenda.color}").pack()
            Label(ventana_detalle, text=f"Marca: {prenda.marca}").pack()
            Label(ventana_detalle, text=f"Talla: {prenda.talla}").pack()
            Label(ventana_detalle, text=f"Código: {prenda.Asignar_Codigo()}").pack()

            # Marcamos que se encontró una coincidencia y rompemos el bucle
            encontrada_coincidencia = True
            break

    # Después de recorrer toda la lista, si no se encontró ninguna coincidencia, mostrar el mensaje
    if not encontrada_coincidencia:
        messagebox.showerror("Búsqueda de Prenda", "Prenda no encontrada")


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
    
def Iniciar_sesion():
    #Inicio sesión
    global Iniciar_sesion_interfaz
    Iniciar_sesion_interfaz = tk.Toplevel(Pantalla_principal)
    Iniciar_sesion_interfaz.attributes('-topmost', True)  # Asegurar que la ventana esté siempre en la parte superior
    
    
    Inicio_Sesion = Label(Iniciar_sesion_interfaz, text = "Iniciar sesión", font = "Consola 14 bold")
    Inicio_Sesion.grid(row=0, column=1, columnspan=2)

        #Nombre 
    Nombre_usuario = Label(Iniciar_sesion_interfaz, text = "Nombre de usuario", font= "consola 12")
    Nombre_usuario.grid(row=1, column=1,padx= 5)
    Nombre_usuario_String = StringVar()
    string_entry_usuario = Entry(Iniciar_sesion_interfaz, textvariable = Nombre_usuario_String)
    string_entry_usuario.grid(row=1, column=2)

        #Contraseña
    Contraseña_usuario = Label(Iniciar_sesion_interfaz, text = "Contraseña", font= "consola 12")
    Contraseña_usuario.grid(row=2, column=1)
    Contraseña_usuario_String = StringVar()
    string_entry_Contraseña = Entry(Iniciar_sesion_interfaz,  textvariable = Contraseña_usuario_String, show="*")
    string_entry_Contraseña.grid(row=2, column=2)

        #Iniciar sesion
    Boton_Iniciar_Sesion = Button(Iniciar_sesion_interfaz, text = "Iniciar sesión", command = lambda: InicioSesion(usuarios,Nombre_usuario_String,Contraseña_usuario_String,Iniciar_sesion_interfaz))
    Boton_Iniciar_Sesion.grid(row=3, column=1)
    Boton_Registrarse = Button(Iniciar_sesion_interfaz, text = "Registarse", command = Interfaz_Registro)
    Boton_Registrarse.grid(row=3, column=2)
    
#==========================================================================================

#==============================ROOT INTERFAZ======================
Pantalla_principal = Tk()
Pantalla_principal.title("Programa")



    #Propiedades de la pantalla principal
#Pantalla_principal.geometry("900x500")
Pantalla_principal.resizable(True,True)
#=================================================================
codigo_buscado_var = StringVar()


#==============================FRAMES======================
textoIngreso = Frame(Pantalla_principal)
textoIngreso.pack(fill=X)

#=================================================================


#==============================MENU======================
menu = Frame (pady= 40)
menu.pack(side=TOP, fill=X)

Codigo_buscado_ingresado = StringVar()
#==============INGRESAR UNA PRENDA================

#--------- ENTRADAS --------------
codigo_buscado_var = StringVar()
Marca_prenda_input = StringVar()
Tipo_prenda_input = StringVar()
Talla_prenda_input = StringVar()
Color_prenda_input = StringVar()
#------------------------------
    
#------Frame principal------------
Opcion1_Frame = LabelFrame(menu, width=50, height=80)
Opcion1_Frame.grid(row=0, column=0, pady=5, padx=10, sticky="ns")
#---------------------------------

#------Opciones----------
Label(Opcion1_Frame, text="Ingresar ropa", font="Arial 14 bold").grid(row=0, column=0, pady=(0, 5))

Buscar_ropa = Frame(Opcion1_Frame)
Buscar_ropa.grid(row=1, column=0)

Label(Buscar_ropa, text="Introduce el código de la prenda").grid(row=0, column=0, sticky="w")
Buscar_ropa_entrada = Entry(Buscar_ropa, textvariable=codigo_buscado_var, state = "disabled").grid(row=0, column=1, padx=6)
boton_buscar = Button(Buscar_ropa, text="Buscar", command=Mostrar_detalles)
boton_buscar.grid(row=0, column=2, sticky="e")

Label(Opcion1_Frame, text="Recuerde que debe ser mayúscula al inicio", font="Arial 9").grid(row=2, column=0, pady=3)

Label(Opcion1_Frame, text="Marca de la prenda").grid(row=3, column=0, sticky="w", pady=2)

Marca_prenda = Entry(Opcion1_Frame, textvariable=Marca_prenda_input,state = "disabled").grid(row=3, column=0, padx=5, pady=2)

Label(Opcion1_Frame, text="Tipo de prenda").grid(row=4, column=0, sticky="w")

Tipo_Prenda = Entry(Opcion1_Frame, textvariable=Tipo_prenda_input,state = "disabled").grid(row=4, column=0, padx=10)

Label(Opcion1_Frame, text="Talla de la prenda").grid(row=5, column=0, sticky="w")

Talla_Prenda = Entry(Opcion1_Frame, textvariable=Talla_prenda_input,state = "disabled").grid(row=5, column=0, padx=10)

Label(Opcion1_Frame, text="Color de la prenda").grid(row=6, column=0, sticky="w")

Color_Prenda = Entry(Opcion1_Frame, textvariable=Color_prenda_input, state = "disabled").grid(row=6, column=0, padx=10)

enviar_Datos_Prenda = Button(Opcion1_Frame, text="Enviar datos", command=Ingreso_Ropa)
enviar_Datos_Prenda.grid(row=7, column=0, pady=5, padx=3)
#-----------------------------------

#------------Botones-----------------
Ver_Inventario_boton = Button(Opcion1_Frame, text="Inventario", command=Inventario_prendas)
Ver_Inventario_boton.grid(row=8, column=0)
#--------------------------------------

    #============================================

# opcion3 = Label(menu, text ="Venta", font= "Arial 15")
# opcion3.pack(padx=5, pady=5)


#=================================================================
Iniciar_sesion()
#Bucle principal
Pantalla_principal.mainloop()





                

    
    

