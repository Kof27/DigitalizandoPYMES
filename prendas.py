import pandas as pd

class Prendas():
    Prendas_Creadas = []
    #se inicia de primero siempre que se ejecuta la clase
    def __init__(self,marca, tipo, color,talla):
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.talla = talla
        Prendas.Asignar_Codigo(self)
        
        Prendas.Prendas_Creadas.append(self)  # Añade el objeto a la lista
    def Asignar_Codigo(self):
        #se crea diccionarios con los digitos de cada valor
        codigo_marca = {
            "Adidas": 1,
            "Zara": 2,
            "H&B": 3
        }
        
        codigo_tipo = {
            "Blusa": 1,
            "Pantalón": 2,
            "Camiseta": 3
        }
        
        codigo_color = {
            "Azul": 1,
            "Rojo": 2,
            "Morado": 3
        }
        
        codigo_talla = {
            "M" : 1,
            "L" : 2,
            "XL" : 3
        }
        
        #el .get es para obtener el valor de un diccionario
        #el ",0" es para devolver 0 por si no se encuentra un valor
        codigo = str(str(codigo_marca.get(self.marca,0))+str(codigo_tipo.get(self.tipo))+str(codigo_color.get(self.color))+str(codigo_talla.get(self.talla)))

        return codigo

#sirve para imprimir la lista creada
for prenda in Prendas.Prendas_Creadas:
    print(f"Marca: {prenda.marca}, Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}")
    
    
#---------------
#Base de datos
#--------------

# Convertimos los objetos en diccionarios y los almacenamos en una lista
data = [vars(prenda) for prenda in Prendas.Prendas_Creadas]

# Creamos un DataFrame de pandas a partir de la lista de diccionarios
df = pd.DataFrame(data)

# Ahora puedes guardar el DataFrame en un archivo CSV o en cualquier otro formato soportado por pandas
df.to_csv('prendas.csv', index=False)