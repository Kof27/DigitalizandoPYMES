from prendas import *
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
from tkinter import PhotoImage, Tk, Label



#-------------------
#PRUEBA DE INTERFAZ
#------------------

# Variables globales
# =============================================================
usuario_autenticado = False
estado_entry = "disabled"
global ActualizarTabla
# =============================================================
#Variables fijas
ganancias = 0

usuarios = { "D": "1", "Tester" : "54321" }

#==================FUNCIONES DEL PROGRAMA=========================================

# Función para actualizar la visibilidad de la Listbox
def actualizar_visibilidad():
    if usuario_autenticado:
        Inventario_publico.pack(ipadx=300, ipady=80)
    else:
        Inventario_publico.pack_forget()
        
    #---------------Iniciar sesión y creación de usuarios------------------------------
def InicioSesion(usuarios,Nombre_usuario_String,Contraseña_usuario_String,Iniciar_sesion_interfaz):
    global usuario_autenticado
    usuario_ingresado = Nombre_usuario_String.get()
    contraseña_ingresada = Contraseña_usuario_String.get()
        # Solicitar al usuario que ingrese un nombre de usuario
    

        # Verificar si el nombre de usuario ya existe en el diccionario
    if usuario_ingresado in usuarios:
        if contraseña_ingresada == usuarios[usuario_ingresado]: #ESTO SOLO COMPRUEBA SI EL USUARIO FUE ENCONTRAD
            messagebox.showinfo(title = " ", message = "bienvenido")
            usuario_autenticado = True
            actualizar_visibilidad()
            Iniciar_sesion_interfaz.destroy()
            #-----------Activar los entrys----------
            Buscar_ropa_entrada = Entry(Buscar_ropa, textvariable=codigo_buscado_var, state = "normal",font = "Sans-Serif-Collection 15").grid(row=0, column=1, padx=6)
            Marca_prenda = Entry(Opcion1_Frame,bg="white", textvariable=Marca_prenda_input,state = "normal",font = "Sans-Serif-Collection 15").grid(row=3, column=0, padx=5, pady=2)
            Tipo_Prenda = Entry(Opcion1_Frame, bg="white",textvariable=Tipo_prenda_input,state = "normal",font = "Sans-Serif-Collection 15").grid(row=4, column=0, padx=10)
            Talla_Prenda = Entry(Opcion1_Frame,bg="white", textvariable=Talla_prenda_input,state = "normal",font = "Sans-Serif-Collection 15").grid(row=5, column=0, padx=10)
            Color_Prenda = Entry(Opcion1_Frame, bg="white",textvariable=Color_prenda_input, state = "normal",font = "Sans-Serif-Collection 15").grid(row=6, column=0, padx=10)
            Precio_Prenda = Entry(Opcion1_Frame, bg="white",textvariable=Precio_prenda_input, state = "normal",font = "Sans-Serif-Collection 15").grid(row=7, column=0, padx=10)
            actualizar_visibilidad()
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
    #Diccionarios creados para codigo
    codigo_marca = {
            "Adidas": 1,
            "Zara": 2,
            "H&B": 3,
            "Nike" : 4,
            "Puma" : 5,
            "Levi's" : 6,
            "Converse" : 7,
            "Vans" : 8,
            "Tommy Hilfiger" : 9,
            "Calvin Klein" : 10,
            "Ralph Lauren" : 11,
            "Reebok" : 12,
            "Lacoste" : 13,
        }  
        
    codigo_tipo = {
        "Camiseta": "C",
        "Pantalón": "P",
        "Blusa": "B",
        "Chaqueta": "CH",
        "Vestido": "V",
        "Sudadera": "S",
        "Falda": "F",
        "Camisa": "CA",
        "Chaleco": "CHA",
        "Jeans": "J",
        "Leggings": "L",
        "Traje": "T",
        "Jersey": "JER",
        "Abrigo": "A",
        "Sombrero": "SO"
        }
        
    codigo_color = {
        "Rojo": 1,
        "Azul": 2,
        "Verde": 3,
        "Negro": 4,
        "Blanco": 5,
        "Gris": 6,
        "Amarillo": 7,
        "Rosa": 8,
        "Morado": 9,
        "Naranja": 10,
        "Marrón": 11,
        "Celeste": 12,
        "Turquesa": 13,
        "Beige": 14,
        "Oro": 15,
        "Plata": 16
        }
        
    codigo_talla = {
        "XS": "X",
        "S": "S",
        "M": "M",
        "L": "L",
        "XL": "X",
        "XXL": "XX",
        "XXXL": "XXX",
        "4XL": "4X",
        "5XL": "5X"
        }
    
    
    marca = Marca_prenda_input.get()
    tipo = Tipo_prenda_input.get()
    color = Color_prenda_input.get()
    talla = Talla_prenda_input.get()
    precio = Precio_prenda_input.get()
            
        # Comprobación para campos en blanco
    if not marca or not tipo or not color or not talla or not precio:
        messagebox.showerror(title="", message="Por favor, complete todos los campos.")
        return

    #comprobación por si no existe en los diccionarios
    if marca not in codigo_marca:
        messagebox.showerror(title="", message=f"La marca '{marca}' no se encuentra registrada.")
        return
    elif tipo not in codigo_tipo:
        messagebox.showerror(title="", message=f"El tipo '{tipo}' no se encuentra registrada.")
        return
    elif color not in codigo_color:
        messagebox.showerror(title="", message=f"El color '{color}' no se encuentra registrada.")
        return
    elif talla not in codigo_talla:
        messagebox.showerror(title="", message=f"La talla '{talla}' no se encuentra registrada.")
        return
        
        #Imprimir prendas creadas
    for prenda in Prendas.Prendas_Creadas:
            print(f"Marca: {prenda.marca}, Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}, precio: {prenda.precio}")
    
    Prenda_Nueva = Prendas(marca,tipo,color,talla,precio)
    Prenda_Nueva.Asignar_Codigo()
    messagebox.showinfo(title = "", message = "Prenda añadida con exito")
    
    Marca_prenda_input.set("")
    Tipo_prenda_input.set("")
    Talla_prenda_input.set("")
    Color_prenda_input.set("")
    Precio_prenda_input.set("")

    actualizar_inventario()



def Mostrar_detalles():
    codigo_buscado = codigo_buscado_var.get()

    print("Código a buscar:", repr(codigo_buscado))

    print(Prendas.Prendas_Creadas)

    coincidencias = []

    for prenda in Prendas.Prendas_Creadas:
        print("Código de la prenda:", repr(prenda.Asignar_Codigo()))

        if prenda.Asignar_Codigo() == codigo_buscado:
            coincidencias.append(prenda)

    if coincidencias:
        ventana_detalle = Toplevel()
        ventana_detalle.title("Detalles de la prenda")
        ventana_detalle.attributes('-topmost', True)
    
        # Configurar Scrollbar
        scrollbar = Scrollbar(ventana_detalle)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Crear un marco interior para colocar widgets
        marco_interior = Frame(ventana_detalle)
        marco_interior.pack(expand=True, fill=BOTH)

        # Configurar la Listbox dentro del marco interior
        detalles_listbox = Listbox(marco_interior, yscrollcommand=scrollbar.set, font="Sans-Serif-Collection 12")
        detalles_listbox.pack(expand=True, fill=BOTH)

        # Configurar la barra de desplazamiento
        scrollbar.config(command=detalles_listbox.yview)

        for prenda in coincidencias:
            detalles_listbox.insert(END, f"Código: {prenda.Asignar_Codigo()}")
            detalles_listbox.insert(END, f"Tipo: {prenda.tipo}")
            detalles_listbox.insert(END, f"Color: {prenda.color}")
            detalles_listbox.insert(END, f"Marca: {prenda.marca}")
            detalles_listbox.insert(END, f"Talla: {prenda.talla}")
            detalles_listbox.insert(END, f"Precio: ${prenda.precio}")
            detalles_listbox.insert(END, "-------------------")

        # Ajustar la ventana al contenido
        ventana_detalle.geometry("400x300")

    else:
        messagebox.showinfo("Detalles de la prenda", "No se encontraron prendas con ese código.")


def Generar_Venta():
    
    global ganancias
    # Solicitar el nombre del cliente
    cliente = Nombre_cliente.get()

    Token = False
    # Solicitar el correo electrónico del cliente con validación básica
    while True:
        email_usuario = Correo_cliente.get()
        if len(email_usuario) == 2:
            messagebox.showerror(message ="Email inválido")
            break
        elif "@" in email_usuario and "." in email_usuario:
            print("Acceso garantizado")
            Token = True
            break
        else:
            messagebox.showerror(message = "Acceso no garantizado. El correo electrónico debe contener '@' y '.'." )
            Correo_cliente.set("")
            break
        
    if Token:
        # Mostrar la lista de prendas disponibles
        print("Lista de prendas disponibles:")
        for prenda in Prendas.Prendas_Creadas:
            print(f"Código: {prenda.Asignar_Codigo()}, Marca: {prenda.marca}, "
                f"Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}")

        # Solicitar al usuario que elija una prenda por su código
        codigo_a_vender = Codigo_a_vender.get()

        # Buscar la prenda en la lista
        prenda_a_vender = None
        for prenda in Prendas.Prendas_Creadas:
            if prenda.Asignar_Codigo() == codigo_a_vender:
                prenda_a_vender = prenda
                break
        # Si se encontró la prenda, generar un recibo y eliminar la prenda de la lista
        cliente = Nombre_cliente.get()
        email_usuario = Correo_cliente.get()
        codigo_a_vender = Codigo_a_vender.get()


    if prenda_a_vender:
        # Actualizar la Listbox de Recibo con la información de la venta
        Recibo.delete(0, END)
        Recibo.delete(0, END)
    
        TituloRecibo = "Recibo"
        DatosCliente = f"Cliente: {cliente}" 
        CorreoCliente = f"Correo: {email_usuario}"
        MarcaPrenda =f"Prenda: {prenda_a_vender.marca}" 
        TipoPrenda = f"Tipo: {prenda_a_vender.tipo}"
        TallaPrenda = f"Talla: {prenda_a_vender.talla}"
        ColorPrenda = f"Color: {prenda_a_vender.color}" 
        CodigoPrenda =f"Código: {prenda_a_vender.Asignar_Codigo()}"
        PrecioPrenda = f"Precio: {prenda_a_vender.precio}"
                 
        Recibo.insert(END, TituloRecibo,DatosCliente,CorreoCliente,CodigoPrenda,MarcaPrenda,TipoPrenda,TallaPrenda,ColorPrenda,PrecioPrenda)
        messagebox.showinfo("Venta realizada", "Venta registrada con éxito.")

        Prendas.Prendas_Creadas.remove(prenda_a_vender)
        print("Prenda vendida y eliminada de la lista.")
        actualizar_inventario()
        ganancias += prenda_a_vender.precio
        Ganancias_label.config(text=f"Ganancias: ${ganancias}")
        
    else:
        messagebox.showerror("Error", "Prenda no encontrada.")


       

            
    
    
#Interfaz funciones
def Interfaz_Registro():
    # Crear una nueva ventana para el registro
    ventana_registro = Toplevel(Pantalla_principal, bg = "white")
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("400x220")
    ventana_registro.resizable(False,False)
    ventana_registro.attributes('-topmost', True)
    
    marco_registro = Frame(ventana_registro, bg = "white")
    marco_registro.pack(pady=20)

    nombre_label = Label(marco_registro, text="Nombre de usuario", font = "Sans-Serif-Collection 15", bg = "white")
    nombre_label.pack()

    nombre_usuario_registro = StringVar()
    entry_nombre_usuario = Entry(marco_registro, width=20, textvariable=nombre_usuario_registro,font = "Sans-Serif-Collection 15",bg = "#febf97")
    entry_nombre_usuario.pack(pady=4)

    contraseña_label = Label(marco_registro, text="Contraseña", font = "Sans-Serif-Collection 15", bg = "white")
    contraseña_label.pack()

    contraseña_registro = StringVar()
    entry_contraseña_registro = Entry(marco_registro, width=20, textvariable=contraseña_registro, show="*",font = "Sans-Serif-Collection 15",bg = "#febf97")
    entry_contraseña_registro.pack(pady=4)

    Enviar_Datos = Button(ventana_registro, text = "Registrarse", command = lambda: [crear_usuario(nombre_usuario_registro.get(),contraseña_registro.get(),usuarios), ventana_registro.destroy()],font = "Sans-Serif-Collection 15",bg = "#f5ecb7")#El ventana_registro.destroy() es para cerrar la pestaña despues de dar el boton 

    Enviar_Datos.pack(pady=4)
    
def Iniciar_sesion():
    #Inicio sesión
    global Iniciar_sesion_interfaz
    Iniciar_sesion_interfaz = tk.Toplevel(Pantalla_principal, bg = "white")
    Iniciar_sesion_interfaz.title("Iniciar sesión")
    Iniciar_sesion_interfaz.attributes('-topmost', True)  # Asegurar que la ventana esté siempre en la parte superior    
    Iniciar_sesion_interfaz.resizable(False,False)
    Inicio_Sesion = Label(Iniciar_sesion_interfaz, text = "Iniciar sesión", font = "Sans-Serif-Collection 16 bold", bg = "white")
    Inicio_Sesion.grid(row=0, column=1, columnspan=2, pady = 10)
        #Nombre 
    Nombre_usuario = Label(Iniciar_sesion_interfaz, text = "Nombre de usuario", font = "Sans-Serif-Collection 15", bg = "white")
    Nombre_usuario.grid(row=1, column=1,padx= 5)
    Nombre_usuario_String = StringVar()
    string_entry_usuario = Entry(Iniciar_sesion_interfaz, textvariable = Nombre_usuario_String,font = "Sans-Serif-Collection 15",bg = "#febf97")
    string_entry_usuario.grid(row=1, column=2,padx = 10)

        #Contraseña
    Contraseña_usuario = Label(Iniciar_sesion_interfaz, text = "Contraseña", font = "Sans-Serif-Collection 15",bg = "white")
    Contraseña_usuario.grid(row=2, column=1, pady= 2)
    Contraseña_usuario_String = StringVar()
    string_entry_Contraseña = Entry(Iniciar_sesion_interfaz,  textvariable = Contraseña_usuario_String, show="*",font = "Sans-Serif-Collection 15",bg = "#febf97")
    string_entry_Contraseña.grid(row=2, column=2, pady= 2,padx = 10)

        #Iniciar sesion
    Boton_Iniciar_Sesion = Button(Iniciar_sesion_interfaz, text = "Iniciar sesión", command = lambda: InicioSesion(usuarios,Nombre_usuario_String,Contraseña_usuario_String,Iniciar_sesion_interfaz),font = "Sans-Serif-Collection 15",bg = "#f5ecb7")
    Boton_Iniciar_Sesion.grid(row=3, column=1, pady= 5)
    Boton_Registrarse = Button(Iniciar_sesion_interfaz, text = "Registarse", command = Interfaz_Registro,font = "Sans 15",bg = "#f5ecb7")
    Boton_Registrarse.grid(row=3, column=2, pady= 5)
    
def actualizar_inventario():
    # Primero, limpiamos el Listbox
    Inventario_publico.delete(0, END)
    numeroinicial = 0
    # Luego, agregamos las prendas actuales
    for prenda in Prendas.Prendas_Creadas:
        numeroinicial+=1
        info_str = f"{numeroinicial} -> Código: {prenda.Asignar_Codigo()}\n Precio: ${prenda.precio}\n Marca: {prenda.marca}\n Tipo: {prenda.tipo}\n Color: {prenda.color}\n Talla: {prenda.talla}\n"
        Inventario_publico.insert(END, "", info_str)
        # Inventario_publico.insert(END, "")  # Insertar una línea en blanco adicional para separar las prendas

def Borrar_campos():
    Nombre_cliente.set("")   
    Correo_cliente.set("")   
    Codigo_a_vender.set("")   
    Numero_cliente.set("")  
    
def salirprograma():
    Pantalla_principal.destroy() 
    
#==========================================================================================

#==============================ROOT INTERFAZ======================
Pantalla_principal = Tk()
Pantalla_principal.title("Programa")
Pantalla_principal.attributes('-fullscreen', True)
Pantalla_principal.configure(background="#f1c40f")


Pantalla_principal.resizable(False,False)
#=================================================================
codigo_buscado_var = StringVar()


#==============================FRAMES======================
textoIngreso = Frame(Pantalla_principal, background="#f1c40f")
textoIngreso.pack(fill=X)

#=================================================================


#==============================MENU======================
menu = Frame (pady= 10, background="#f1c40f")
menu.pack(side=TOP, fill=X)
Button(Pantalla_principal, text = "Salir del programa", font="Sans-Serif-Collection 18 bold", command = salirprograma).pack(pady=5)
Codigo_buscado_ingresado = StringVar()

#==============INGRESAR UNA PRENDA================

#--------- ENTRADAS --------------
codigo_buscado_var = StringVar()
Marca_prenda_input = StringVar()
Tipo_prenda_input = StringVar()
Talla_prenda_input = StringVar()
Color_prenda_input = StringVar()
Precio_prenda_input = IntVar()
#------------------------------

#------Frame principal------------
Opcion1_Frame = LabelFrame(menu, relief = GROOVE, background="#f39c12")
Opcion1_Frame.pack(side = "left",padx = 20)
#---------------------------------

#------Opciones----------
Label(Opcion1_Frame, text="Ingresar ropa", bg="#f39c12",font="Sans-Serif-Collection 14 bold").grid(row=0, column=0, pady=(0, 5))

Buscar_ropa = Frame(Opcion1_Frame,bg="#f39c12")
Buscar_ropa.grid(row=1, column=0, )

Label(Buscar_ropa, text="Introduce el código de la prenda",bg="#f39c12",font = "Sans-Serif-Collection 15").grid(row=0, column=0, sticky="w",)
Buscar_ropa_entrada = Entry(Buscar_ropa, textvariable=codigo_buscado_var, state = "disabled",bg="#e67e22").grid(row=0, column=1, padx=6)
boton_buscar = Button(Buscar_ropa, text="Buscar", bg="#f39c12",command=Mostrar_detalles,font = "Sans-Serif-Collection 15")
boton_buscar.grid(row=0, column=2, sticky="e")


Label(Opcion1_Frame, bg="#f39c12",text="Recuerde que debe ser mayúscula al inicio", font="Sans-Serif-Collection 11").grid(row=2, column=0, pady=3)

Label(Opcion1_Frame, bg="#f39c12",text="Marca de la prenda", font = "Sans-Serif-Collection 15").grid(row=3, column=0, sticky="w", pady=2)

Marca_prenda = Entry(Opcion1_Frame, textvariable=Marca_prenda_input,state = "disabled",bg="#e67e22").grid(row=3, column=0, padx=5, pady=2)

Label(Opcion1_Frame, text="Tipo de prenda",bg="#f39c12", font = "Sans-Serif-Collection 15").grid(row=4, column=0, sticky="w")

Tipo_Prenda = Entry(Opcion1_Frame, textvariable=Tipo_prenda_input,state = "disabled",bg="#e67e22").grid(row=4, column=0, padx=10)

Label(Opcion1_Frame, text="Talla de la prenda", bg="#f39c12",font = "Sans-Serif-Collection 15").grid(row=5, column=0, sticky="w")

Talla_Prenda = Entry(Opcion1_Frame, textvariable=Talla_prenda_input,state = "disabled",bg="#e67e22").grid(row=5, column=0, padx=10)

Label(Opcion1_Frame, text="Color de la prenda",bg="#f39c12", font = "Sans-Serif-Collection 15").grid(row=6, column=0, sticky="w")

Color_Prenda = Entry(Opcion1_Frame, textvariable=Color_prenda_input, state = "disabled",bg="#e67e22").grid(row=6, column=0, padx=10)

Label(Opcion1_Frame, text="Precio", bg="#f39c12",font = "Sans-Serif-Collection 15").grid(row=7, column=0, sticky="w")

Precio_Prenda = Entry(Opcion1_Frame, textvariable=Precio_prenda_input, state = "disabled",bg="#e67e22").grid(row=7, column=0, padx=10)

enviar_Datos_Prenda = Button(Opcion1_Frame, text="Enviar datos", command=Ingreso_Ropa,font = "Sans-Serif-Collection 15",bg="#f39c12")
Label(Opcion1_Frame, text = "Si no se registra la prenda, revise que el precio solo contenga numeros.", bg="#f39c12", font = "Sans-Serif-Collection 9").grid(row = 9, column = 0)
enviar_Datos_Prenda.grid(row=8, column=0, pady=5, padx=3)


#-----------------------------------

#---------Inventario-----------
Inventario = LabelFrame(Opcion1_Frame, text="Prendas guardadas",bg="#f39c12", relief = RAISED)
Inventario.grid(row = 10, column = 0, columnspan= 5,)

# Crear el Listbox
Inventario_publico = Listbox(Inventario, font="Consolas 9", selectbackground="lightblue", selectmode="extended")

    
# Configurar el Scrollbar
scrollbar = Scrollbar(Inventario, orient=VERTICAL, command=Inventario_publico.yview)
Inventario_publico.configure(yscrollcommand=scrollbar.set)
    
scrollbar.pack(side=RIGHT, fill=Y)
Inventario_publico.pack_forget()

#-----------------------------

#==================Generar venta==================
Opcion2_Frame = LabelFrame(menu, relief = GROOVE, background = "#f39c12")


Datos_del_cliente = Frame(Opcion2_Frame, bg = "#f39c12")
#---------- ENTRADAS --------------------------
Nombre_cliente = StringVar()
Correo_cliente = StringVar()
Codigo_a_vender = StringVar()
Numero_cliente = StringVar()
#-------------------------------------------

Label(Datos_del_cliente, text = "Venta", font = "Sans-Serif-Collection 20 bold",bg = "#f39c12").pack(ipadx = 40)
Nombre_cliente_preguntar = Label(Datos_del_cliente, text = "Nombre del cliente",bg = "#f39c12", font = "Sans-Serif-Collection 15")
Nombre_cliente_entrada = Entry (Datos_del_cliente, bg="white", textvariable = Nombre_cliente, font = "Sans-Serif-Collection 15",state = "normal")

Correo_cliente_preguntar = Label(Datos_del_cliente, text = "Correo del cliente",bg = "#f39c12", font = "Sans-Serif-Collection 15")
Correo_cliente_entrada = Entry(Datos_del_cliente, bg="white",textvariable = Correo_cliente, font = "Sans-Serif-Collection 15",state = "normal")

Codigo_vender = Label(Datos_del_cliente,text = "Codigo de la prenda a vender",bg = "#f39c12", font = "Sans-Serif-Collection 15")
Codigo_a_vender_entrada = Entry(Datos_del_cliente,bg="white", textvariable = Codigo_a_vender, font = "Sans-Serif-Collection 15",state = "normal")


Enviar_Datos_Clientes = Button(Datos_del_cliente, text= "Venta", command = Generar_Venta, font = "Sans-Serif-Collection 15",bg = "#f39c12")
Borrar_Datos = Button(Datos_del_cliente, text = "Borrar campos", command = Borrar_campos, font = "Sans-Serif-Collection 15",bg = "#f39c12")

# Crear el Listbox
Recibo = Listbox(Datos_del_cliente, font="Consolas 12", selectbackground="lightblue", selectmode="extended")
    
# Configurar el Scrollbar
scrollbar = Scrollbar(Datos_del_cliente, orient=VERTICAL, command=Recibo.yview)
Recibo.configure(yscrollcommand=scrollbar.set)
    
scrollbar.pack(side=RIGHT, fill=Y)

# Crear la etiqueta para mostrar las ganancias
Ganancias_label = Label(Datos_del_cliente, text="Ganancias: $0", font="Sans-Serif-Collection 12",bg = "#f39c12")

#--------IMPRIMIR EN PANTALLA-------------------
Nombre_cliente_preguntar.pack(ipadx= 20, pady= 2)
Nombre_cliente_entrada.pack()

Correo_cliente_preguntar.pack(ipadx= 20,pady= 2)
Correo_cliente_entrada.pack()



Codigo_vender.pack(ipadx= 20,pady= 2)
Codigo_a_vender_entrada.pack()

Enviar_Datos_Clientes.pack(pady= 5)
Borrar_Datos.pack()

Recibo.pack(ipadx = 60)

Ganancias_label.pack()

Datos_del_cliente.grid(row=0, column= 0)

Opcion2_Frame.pack(side = "left", padx = 40)


#--------------------------------------------------
#=================================================

#=================================================================
actualizar_inventario()
Iniciar_sesion()
#Bucle principal
Pantalla_principal.mainloop()





                

    
    

