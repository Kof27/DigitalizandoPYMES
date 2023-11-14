# import pandas as pd

class Prendas():
    Prendas_Creadas = []
    ventas = []
    #se inicia de primero siempre que se ejecuta la clase
    def __init__(self,marca, tipo, color,talla,precio):
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.talla = talla
        self.precio = precio
        Prendas.Asignar_Codigo(self)
        
        Prendas.Prendas_Creadas.append(self)  # Añade el objeto a la lista
    def Asignar_Codigo(self):
        #se crea diccionarios con los digitos de cada valor
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
        
        #el .get es para obtener el valor de un diccionario
        #el ",0" es para devolver 0 por si no se encuentra un valor
        codigo = str(str(codigo_marca.get(self.marca,0))+str(codigo_tipo.get(self.tipo))+str(codigo_color.get(self.color))+str(codigo_talla.get(self.talla)))

        return codigo


#sirve para imprimir la lista creada
for prenda in Prendas.Prendas_Creadas:
    print(f"Marca: {prenda.marca}, Tipo: {prenda.tipo}, Color: {prenda.color}, Talla: {prenda.talla}, Código: {prenda.Asignar_Codigo()}")
    
# Prenda 1
prenda1 = Prendas("Adidas", "Camiseta", "Rojo", "M", 45000)

# Prenda 2
prenda2 = Prendas("Zara", "Pantalón", "Azul", "S", 65000)

# Prenda 3
prenda3 = Prendas("H&B", "Blusa", "Negro", "L", 55000)

# Prenda 4
prenda4 = Prendas("Nike", "Chaqueta", "Gris", "XL", 90000)

# Prenda 5
prenda5 = Prendas("Puma", "Vestido", "Blanco", "S", 75000)

# Prenda 6
prenda6 = Prendas("Levi's", "Sudadera", "Rojo", "M", 80000)

# Prenda 7
prenda7 = Prendas("Converse", "Falda", "Azul", "S", 60000)

# Prenda 8
prenda8 = Prendas("Vans", "Camisa", "Negro", "L", 70000)

# Prenda 9
prenda9 = Prendas("Tommy Hilfiger", "Chaleco", "Gris", "XL", 85000)

# Prenda 10
prenda10 = Prendas("Calvin Klein", "Jeans", "Negro", "M", 95000)

# Prenda 11
prenda11 = Prendas("Ralph Lauren", "Leggings", "Azul", "S", 70000)

# Prenda 12
prenda12 = Prendas("Reebok", "Traje", "Verde", "L", 110000)

# Prenda 13
prenda13 = Prendas("Lacoste", "Jersey", "Blanco", "XL", 90000)

# Prenda 14
prenda14 = Prendas("Adidas", "Abrigo", "Negro", "M", 120000)

# Prenda 15
prenda15 = Prendas("Zara", "Sombrero", "Marrón", "L", 35000)

# Prenda 16
prenda16 = Prendas("H&B", "Chaleco", "Gris", "S", 60000)

# Prenda 17
prenda17 = Prendas("Nike", "Sudadera", "Azul", "L", 85000)

# Prenda 18
prenda18 = Prendas("Puma", "Jersey", "Verde", "M", 80000)

# Prenda 19
prenda19 = Prendas("Levi's", "Pantalón", "Negro", "XL", 70000)

# Prenda 20
prenda20 = Prendas("Converse", "Chaqueta", "Rojo", "S", 90000)


#---------------
#Base de datos
#--------------

# # Convertimos los objetos en diccionarios y los almacenamos en una lista
# data = [vars(prenda) for prenda in Prendas.Prendas_Creadas]

# # Creamos un DataFrame de pandas a partir de la lista de diccionarios
# df = pd.DataFrame(data)

# # Ahora puedes guardar el DataFrame en un archivo CSV o en cualquier otro formato soportado por pandas
# df.to_csv('prendas.csv', index=False)