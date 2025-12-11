# Clase que gestiona las categorias del sistema
class GestorCategorias:
    """
     administra todas las categorias disponibles y permite crear, listar y validar categorias
    """
    def __init__(self):
        # Lista privada que almacena las categorias
        self._categorias = [] 
    
    # Funcion para crear categorias y modificarlas
    def crear_categoria(self, nombre_categoria: str = None):
        """
        Permite al usuario crear una nueva categoria y la agrega a la lista de categorias existentes
        """
        #  Algunas corroboraciones, como que se le de nombre, este vacia o si ya existe
        if nombre_categoria is None:
            print("\n--- CREAR NUEVA CATEGORIA ---")
            nombre_categoria = input("Nombre de la categoria: ").strip()
        
        if not nombre_categoria:
            print("Error: El nombre de la categoria no puede estar vacio")
            return None
        
        if nombre_categoria.lower() in [cat.lower() for cat in self._categorias]:
            print(f"Error: La categoria '{nombre_categoria}' ya existe")
            return None
        
        # Agregamos la categoria a la lista
        self._categorias.append(nombre_categoria)
        
        print(f"Categoria '{nombre_categoria}' creada exitosamente")
        
        #  Retornamos la categoria y el mensaje para el historial
        return nombre_categoria, f"Categoria creada: {nombre_categoria}"
    
    def listar_categorias(self):
        """
        Muestra todas las categorias disponibles en el sistema
        """
        if not self._categorias:
            print("\nNo hay categorias registradas aun")
            return
        
        print("\n" + "="*50)
        print("CATEGORIAS DISPONIBLES")
        print("="*50)
        for i, categoria in enumerate(self._categorias, 1):
            print(f"{i}. {categoria}")
        print("="*50)
    
    def seleccionar_categoria(self):
        """
        FUncion para crear una categoria nueva si no hay categorias, obliga a crear una
        """
        if not self._categorias:
            print("\nNo hay categorias disponibles. Debes crear una primero.")
            return self.crear_categoria()
        
        # Muestra las categorias existentes
        print("\n--- SELECCIONAR CATEGORIA ---")
        print("Categorias disponibles:")
        for i, categoria in enumerate(self._categorias, 1):
            print(f"{i}. {categoria}")
        print(f"{len(self._categorias) + 1}. Crear nueva categoria")
        
        opcion = input("\nSelecciona una opcion: ").strip()
        
        # Verifica si eligio crear nueva categoria o una ya existente
        if opcion == str(len(self._categorias) + 1):
            return self.crear_categoria()
        
        #Try para manejar erroes en conversion a enteros o si no hay un valor
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(self._categorias):
                #  Retornamos la categoria seleccionada
                return self._categorias[indice], None
            else:
                print("Opcion no valida")
                return None, None
        except ValueError:  
            print("Opcion no valida")
            return None, None
    
    # metodo para verificar si hay categorias
    def tiene_categorias(self):

        """Retorna True si hay al menos una categoria"""
        return len(self._categorias) > 0