"""
                                                                        COSAS A PRACTICAR
La parte del codigo que trabaja las especificaciones del excel esta casi que calcada de tutoriales y 
post de reddit, debo investigar mas sobre ella para poder justificarla correctamente
"""
"""
                                                                        COSAS A AGREGAR
        Tener en cuenta pep8
        especializarlo  tal vez
        Intentar para tener colas
        Q hago si me meten 4k datos y no puedo procesarlos o si el historial se vuelve muy grande?
"""
from modelos.catalogo import Catalogo
from modelos.categorias import GestorCategorias
from modelos.historial import Historial
from exportador import ExportadorExcel


# Clase principal que coordina todo el sistema de inventario
class SistemaInventario:
 
    def __init__(self):
    #Inicializamos todas las clases del sistema

        self.catalogo = Catalogo()
        self.categorias = GestorCategorias()
        self.historial = Historial()
        self.exportador = ExportadorExcel()
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("SISTEMA DE INVENTARIO v3.11")
        print("="*50)
        print("1. Crear nuevo producto")
        print("2. Ver catalogo completo")
        print("3. Modificar stock de producto")
        print("4. Actualizar precio de producto")
        print("5. Ver historial de cambios")
        print("6. Exportar catalogo a Excel")
        print("7. Gestionar categorias")
        print("8. Eliminar producto")
        print("9. Salir")
        print("="*50)
    
    def menu_crear_producto(self):
        print("\n--- CREAR NUEVO PRODUCTO ---")
        
        
        try:
            # Solicita los datos del producto y eliminamos espacios en blanco o converrtimos los numeros a numeros decimales o enteros segun sea necesairio
            codigo = input("Codigo del producto: ").strip()
            nombre = input("Nombre: ").strip()
            
           
            if not codigo or not nombre:
                print("Error: El codigo y nombre no pueden estar vacios")
                return
            
            precio = float(input("Precio: $"))
            stock = int(input("Stock inicial: "))
            
        except ValueError:
            print("Error: Debes ingresar numeros validos para precio y stock")
            return
        
        # Aqui se usa la funcion de seleccionar categoria y si no se selecciono o creo una categoria cancelamos la creacion
        resultado = self.categorias.seleccionar_categoria()
        
        #Verifica el resultado de seleccionar categoria
        if resultado is None:
            print("Creacion de producto cancelada")
            return
        
        #  Desempaqueta las categoria y mensajes del historial
        categoria, mensaje_cat = resultado
        
        if not categoria:
            print("Creacion de producto cancelada")
            return
        
        # Si se creo una categoria nueva, registramos en historial
        if mensaje_cat:
            self.historial.registrar_cambio(mensaje_cat)
        
        # Crea el producto y lo registra en historial
        resultado_producto = self.catalogo.agregar_producto(codigo, nombre, precio, stock, categoria)
        if resultado_producto:
            producto, mensaje = resultado_producto
            self.historial.registrar_cambio(mensaje)
    
    def menu_modificar_stock(self):
        print("\n--- MODIFICAR STOCK ---")
        
         # Buscamos el producto en el catalogo y verificamos si se encuentra
        codigo = input("Codigo del producto: ").strip()
        producto = self.catalogo.buscar_producto(codigo)
        
        if not producto:
            print(f"No se encontro producto con codigo '{codigo}'")
            return
        
        print(f"Producto encontrado: {producto}")
        
        print("\n1. Agregar stock")
        print("2. Retirar stock")
        opcion = input("Selecciona operacion: ").strip()
        
        try:
            # Solicitamos la cantidad, la convertimos a entero y verificamos algunas cosas
            cantidad = int(input("Cantidad: "))
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                return
        except ValueError:
            print("Error: Debes ingresar un numero valido")
            return
        
        #  Ejecuta la operacion y registra en el historial si fue exitosa
        if opcion == "1":
            resultado = producto.modificar_stock(cantidad, 'agregar')
            if resultado and resultado[0]:
                self.historial.registrar_cambio(resultado[1])
        elif opcion == "2":
            resultado = producto.modificar_stock(cantidad, 'retirar')
            if resultado and resultado[0]:
                self.historial.registrar_cambio(resultado[1])
        else:
            print("Opcion no valida")
    
    def menu_actualizar_precio(self):
        print("\n--- ACTUALIZAR PRECIO ---")
        
        codigo = input("Codigo del producto: ").strip()
        producto = self.catalogo.buscar_producto(codigo)
        
          # Verificamos si se encontro el producto
        if not producto:
            print(f"No se encontro producto con codigo '{codigo}'")
            return
        
        print(f"Producto encontrado: {producto}")
    
        try:
            # Solicitamos el nuevo precio y lo convertimos a decimal
            nuevo_precio = float(input("Nuevo precio: $"))
            
            if nuevo_precio < 0:
                print("El precio no puede ser negativo")
                return
        except ValueError:
            print("Error: Debes ingresar un numero valido")
            return
        
        # Actualizamos precio y registramos en historial
        mensaje = producto.actualizar_precio(nuevo_precio)
        self.historial.registrar_cambio(mensaje)
    
    #  Menu para gestionar categorias
    def menu_gestionar_categorias(self):
       
        while True:
            print("\n" + "="*50)
            print("GESTIONAR CATEGORIAS")
            print("="*50)
            print("1. Ver categorias existentes")
            print("2. Crear nueva categoria")
            print("3. Volver al menu principal")
            print("="*50)
            
            opcion = input("\nSelecciona una opcion (1-3): ").strip()
            
            if opcion == "1":
                self.categorias.listar_categorias()
            elif opcion == "2":
                #  Crea una categoria y la registra en el historial
                resultado = self.categorias.crear_categoria()
                if resultado:
                    categoria, mensaje = resultado
                    self.historial.registrar_cambio(mensaje)
            elif opcion == "3":
                break
            else:
                print("Opcion no valida. Elige entre 1-3")
            
            input("\nPresiona Enter para continuar...")
    
    #  metodo para eliminar un producto
    def menu_eliminar_producto(self):
      
        print("\n--- ELIMINAR PRODUCTO ---")
        
        #  Solicita el codigo del producto a eliminar
        codigo = input("Codigo del producto a eliminar: ").strip()
        
        # Busca el producto en el catalogo y verifica que exista
        producto = self.catalogo.buscar_producto(codigo)
        
        if not producto:
            print(f"No se encontro producto con codigo '{codigo}'")
            return
        
        #  Mostramos la informacion del producto encontrado y solicitamos confirmacion
        print(f"\nProducto encontrado:")
        print(producto)
        
        confirmacion = input("\nÂ¿Estas seguro de eliminar este producto? (s/n): ").strip().lower()
        
        # si confirma lo eliminarmos y registramos en el historial
        if confirmacion == 's':
            mensaje = self.catalogo.eliminar_producto(codigo)
            if mensaje:
                self.historial.registrar_cambio(mensaje)
        else:
            print("Eliminacion cancelada")
    
    #  Menu para exportar catalogo a Excel
    def menu_exportar(self):

        """Exporta el catalogo y registra en historial"""
        productos = self.catalogo.obtener_todos()
        mensaje = self.exportador.exportar_catalogo(productos)
        if mensaje:
            self.historial.registrar_cambio(mensaje)
    
    # Metodo principal que ejecuta el sistema
    def ejecutar(self):
        print("Bienvenido al Sistema de Inventario!")
        
        # Iniciamos un ciclo infinito para el menu
        while True:
            self.mostrar_menu()
            
            opcion = input("\nSelecciona una opcion (1-9): ").strip()
            
            if opcion == "1":
                self.menu_crear_producto()
            elif opcion == "2":
                self.catalogo.listar_productos()
            elif opcion == "3":
                self.menu_modificar_stock()
            elif opcion == "4":
                self.menu_actualizar_precio()
            elif opcion == "5":
                self.historial.ver_historial()
            elif opcion == "6":
                self.menu_exportar()
            elif opcion == "7":
                self.menu_gestionar_categorias()
            elif opcion == "8":
                self.menu_eliminar_producto()
            elif opcion == "9":
                print("\nGracias por usar el sistema de inventario!")
                break

            # Si elige cualquier otra opcion
            else:
                print("Opcion no valida. Elige entre 1-9")
            
            input("\nPresiona Enter para continuar...")




#  Punto de entrada del programa
if __name__ == "__main__":
    # Crea una instancia del sistema y lo ejecutamos
    sistema = SistemaInventario()
    sistema.ejecutar()