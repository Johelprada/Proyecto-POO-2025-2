from datetime import datetime

# Variables globales para almacenar productos y el historial
catalogo_productos = {}  # Diccionario que almacena todos los productos creados
historial_cambios = []   # Lista que registra todos los cambios realizados


class Producto:
    
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, categoria: str):
        """
        Este es el constructor de la clase Producto, con esto haremos nuestro producto
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.fecha_creacion = datetime.now()  # Registra cuando se creo el producto
    
    def modificar_stock(self, cantidad: int, operacion: str):
    
        stock_anterior = self.stock  # Guardamos el stock anterior para el historial
        
        if operacion == 'agregar':
            self.stock += cantidad
            accion = "agrego"
        elif operacion == 'retirar':
            # Verifica que haya suficiente stock antes de retirar
            if cantidad > self.stock:
                print(f"Error: Solo hay {self.stock} unidades disponibles")
                return False
            # Disminuye el stock
            self.stock -= cantidad
            accion = "retiro"
        else:
            print("Operacion no valida")
            return False
        
        # Registra el cambio en el historial con fecha y hora
        cambio = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Se {accion} {cantidad} unidades de '{self.nombre}' (Stock: {stock_anterior} -> {self.stock})"
        historial_cambios.append(cambio)
        print(f"Operacion exitosa: {cambio}")
        return True
    
    def actualizar_precio(self, nuevo_precio: float):

        precio_anterior = self.precio  # Guardamos el precio anterior para el historial
        self.precio = nuevo_precio
        
        # Registra el cambio de precio en el historial
        cambio = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Precio de '{self.nombre}' actualizado: ${precio_anterior:.2f} -> ${nuevo_precio:.2f}"
        historial_cambios.append(cambio)
        print(f"Precio actualizado: {cambio}")
    
    def __str__(self):
        """
        Metodo especial que define como se muestra el producto cuando se imprime este retorna una cadena con la informacion formateada del producto.
        """
        return f"[{self.codigo}] {self.nombre} - Stock: {self.stock} - Precio: ${self.precio:.2f} - Categoria: {self.categoria}"


# Funciones principales del sistema

def crear_producto(codigo: str, nombre: str, precio: float, stock: int, categoria: str):
   
    # Verifica si ya existe un producto con ese codigo
    if codigo in catalogo_productos:
        print(f"Error: Ya existe un producto con el codigo '{codigo}'")
        return None
    
    # Valida que precio y stock no sean negativos
    if precio < 0 or stock < 0:
        print("Error: El precio y el stock no pueden ser negativos")
        return None
    
    # Crea el nuevo producto
    producto = Producto(codigo, nombre, precio, stock, categoria)
    
    # Agrega el producto al catalogo usando el codigo como clave
    catalogo_productos[codigo] = producto
    
    # Registra la creacion del producto en el historial
    cambio = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Producto creado: {nombre} (Codigo: {codigo})"
    historial_cambios.append(cambio)
    print(f"Producto '{nombre}' creado exitosamente")
    
    return producto


def buscar_producto(codigo: str):
 
    return catalogo_productos.get(codigo, None)


def listar_productos():
  
    # Verifica si hay productos en el catalogo
    if not catalogo_productos:
        print("El catalogo esta vacio")
        return
    
    # Muestra el encabezado
    print("\n" + "="*70)
    print("CATALOGO DE PRODUCTOS")
    print("="*70)
    
    # Recorre todos los productos y los muestra
    for producto in catalogo_productos.values():
        print(producto)
    
    print("="*70)


def ver_historial():
    """
    Muestra el historial completo de todos los cambios realizados.
    """
    # Verifica si hay cambios registrados
    if not historial_cambios:
        print("No hay cambios registrados aun")
        return
    
    # Muestra el encabezado
    print("\n" + "="*70)
    print("HISTORIAL DE CAMBIOS")
    print("="*70)
    
    # Muestra cada cambio numerado
    for i, cambio in enumerate(historial_cambios, 1):
        print(f"{i}. {cambio}")
    
    print("="*70)


# Funciones del menu interactivo

def mostrar_menu():
 
    print("\n" + "="*50)
    print("SISTEMA DE INVENTARIO v2.1")
    print("="*50)
    print("1. Crear nuevo producto")
    print("2. Ver catalogo completo")
    print("3. Modificar stock de producto")
    print("4. Actualizar precio de producto")
    print("5. Ver historial de cambios")
    print("6. Salir")
    print("="*50)


def menu_crear_producto():
    """
    Menu interactivo para crear un nuevo producto.
    Solicita al usuario todos los datos necesarios.
    """
    print("\n--- CREAR NUEVO PRODUCTO ---")
    
    # Solicita los datos del producto
    codigo = input("Codigo del producto: ").strip()
    nombre = input("Nombre: ").strip()
    precio = float(input("Precio: $"))
    stock = int(input("Stock inicial: "))
    categoria = input("Categoria: ").strip()
    
    # Crea el producto con los datos ingresados
    crear_producto(codigo, nombre, precio, stock, categoria)


def menu_modificar_stock():
    """
    Menu interactivo para modificar el stock de un producto.
    """
    print("\n--- MODIFICAR STOCK ---")
    
    # Busca el producto por codigo
    codigo = input("Codigo del producto: ").strip()
    producto = buscar_producto(codigo)
    
    # Verifica si el producto existe
    if not producto:
        print(f"No se encontro producto con codigo '{codigo}'")
        return
    
    # Muestra la informacion del producto encontrado
    print(f"Producto encontrado: {producto}")
    
    # Solicita la operacion a realizar
    print("\n1. Agregar stock")
    print("2. Retirar stock")
    opcion = input("Selecciona operacion: ").strip()
    
    # Solicita la cantidad
    cantidad = int(input("Cantidad: "))
    
    # Valida que la cantidad sea positiva
    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        return
    
    # Ejecuta la operacion seleccionada
    if opcion == "1":
        producto.modificar_stock(cantidad, 'agregar')
    elif opcion == "2":
        producto.modificar_stock(cantidad, 'retirar')
    else:
        print("Opcion no valida")


def menu_actualizar_precio():
   
    print("\n--- ACTUALIZAR PRECIO ---")
    
    # Busca el producto por codigo
    codigo = input("Codigo del producto: ").strip()
    producto = buscar_producto(codigo)
    
    # Verifica si el producto existe
    if not producto:
        print(f"No se encontro producto con codigo '{codigo}'")
        return
    
    # Muestra la informacion del producto encontrado
    print(f"Producto encontrado: {producto}")
    
    # Solicita el nuevo precio
    nuevo_precio = float(input("Nuevo precio: $"))
    
    # Valida que el precio no sea negativo
    if nuevo_precio < 0:
        print("El precio no puede ser negativo")
        return
    
    # Actualiza el precio
    producto.actualizar_precio(nuevo_precio)


def main():
    """
    Funcion principal que ejecuta el programa, muestra el menu y las otras cosas

    """
    print("Bienvenido al Sistema de Inventario!")
    
    # Ciclo principal del programa
    while True:
        mostrar_menu()
        
        # Solicita la opcion del usuario
        opcion = input("\nSelecciona una opcion (1-6): ").strip()
        
        # Procesa la opcion seleccionada
        if opcion == "1":
            menu_crear_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            menu_modificar_stock()
        elif opcion == "4":
            menu_actualizar_precio()
        elif opcion == "5":
            ver_historial()
        elif opcion == "6":
            print("\nGracias por usar el sistema de inventario!")
            break  # Sale del ciclo y termina el programa
        else:
            print("Opcion no valida. Elige entre 1-6")
        
        # Pausa para que el usuario vea el resultado antes de continuar
        input("\nPresiona Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
