from datetime import datetime


# Clase que representa un producto individual en el inventario
class Producto:
    """
    Cada producto tiene: codigo, nombre, precio, stock, categoria y fecha de creacion que es lo que estamos asignando aquÃ­.
    """
    # Metodo constructor que se ejecuta al crear un nuevo objeto Producto
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, categoria: str):
        # Asignamos el codigo, nombre, precio, categoria, stock, y fecha de creacion del producto 
        self._codigo = codigo  
        self._nombre = nombre  
        self._precio = precio  
        self._stock = stock    
        self._categoria = categoria  
        self._fecha_creacion = datetime.now()  
         #self.proveedor = ""  

    # Metodo para modificar el stock del producto
    def modificar_stock(self, cantidad: int, operacion: str):
        stock_anterior = self._stock  # Guardamos el stock anterior para el historial
        
        if operacion == 'agregar':
            self._stock += cantidad
            accion = "agrego"
        elif operacion == 'retirar':
            # Verificamos que haya suficiente stock disponible
            if cantidad > self._stock:
                print(f"Error: Solo hay {self._stock} unidades disponibles")
                return False
             # Restamos la cantidad del stock actual
            self._stock -= cantidad
            accion = "retiro"
            #Si la operacion no es valida
        else:
            print("Operacion no valida")
            return False
        
        # Retorna el mensaje de cambio para que el historial lo registre
        cambio = f"Se {accion} {cantidad} unidades de '{self._nombre}' (Stock: {stock_anterior} -> {self._stock})"
        print(f"Operacion exitosa: {cambio}")
        return True, cambio  
    
    # Metodo para actualizar el precio del producto
    def actualizar_precio(self, nuevo_precio: float):
        #guardamos el precio actual antes de cambiarlo al nuevo
        precio_anterior = self._precio
        self._precio = nuevo_precio
        
       # Retorna el mensaje de cambio para que el historial lo registre
        cambio = f"Precio de '{self._nombre}' actualizado: ${precio_anterior:.2f} -> ${nuevo_precio:.2f}"
        print(f"Precio actualizado: {cambio}")
        return cambio  
         #def calcular_valor_total(self):
    #    return self.precio * self.stock
    
    # Definimos como se muestra el producto cuando usamos print
    def __str__(self):
        return f"[{self._codigo}] {self._nombre} - Stock: {self._stock} - Precio: ${self._precio:.2f} - Categoria: {self._categoria}"