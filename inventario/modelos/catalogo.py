from modelos.producto import Producto


# Clase que gestiona el catalogo completo de productos
class Catalogo:
    """
     Administra todos los productos del inventario y encapsula el diccionario de productos y sus operaciones
    """
    def __init__(self):
        #  Diccionario privado que almacena todos los productos
        self._productos = {}  
    
    # Funcion para crear un nuevo producto y agregarlo al catalogo
    def agregar_producto(self, codigo: str, nombre: str, precio: float, stock: int, categoria: str):
        # Verificamos si ya existe un producto con ese codigo en el catalogo
        if codigo in self._productos:
            print(f"Error: Ya existe un producto con el codigo '{codigo}'")
            return None
        
        # Verificamos que el precio y el stock no sean numeros negativos
        if precio < 0 or stock < 0:
            print("Error: El precio y el stock no pueden ser negativos")
            return None
        
        # Creamos un nuevo objeto Producto con los datos proporcionados
        producto = Producto(codigo, nombre, precio, stock, categoria)
        
        # Agregamos el producto al diccionario usando el codigo como clave
        self._productos[codigo] = producto
        
        print(f"Producto '{nombre}' creado exitosamente")
        
        #Retorna el producto y un mensaje para el historial
        return producto, f"Producto creado: {nombre} (Codigo: {codigo})"
    
    def buscar_producto(self, codigo: str):
         # Usamos el metodo get del diccionario que retorna el valor 
        return self._productos.get(codigo, None)
    
    # Metodo para eliminar un producto del catalogo
    def eliminar_producto(self, codigo: str):
        """
        Elimina un producto del catalogo usando su codigo y retorna el mensaje de eliminacion 
        """
        # Verifica si el producto existe en el catalogo
        if codigo not in self._productos:
            print(f"Error: No existe un producto con el codigo '{codigo}'")
            return None
        
        # Obtenemos el producto antes de eliminarlo
        producto = self._productos[codigo]
        nombre_producto = producto._nombre
        
        #  Elimina el producto del diccionario
        del self._productos[codigo]
        
        print(f"Producto '{nombre_producto}' eliminado exitosamente")
        
        # Esto retorna el mensaje para el historial
        return f"Producto eliminado: {nombre_producto} (Codigo: {codigo})"
    
    def listar_productos(self):

        # Verificamos si el diccionario de productos esta vacio
        if not self._productos:
            print("El catalogo esta vacio")
            return
        
        print("\n" + "="*70)
        print("CATALOGO DE PRODUCTOS")
        print("="*70)
        
          # Recorremos todos los productos del diccionario e imprimimos cada profucto
        for producto in self._productos.values():
            print(producto)
        print("="*70)
    
    #  Metodo para obtener todos los productos al exportarlo a excel

    def obtener_todos(self):
     
        return list(self._productos.values())