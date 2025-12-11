# PROYECTO POO- GRUPO: Solitare code


"Con inventory ni una tuerca se pierde

inventory es una herramienta moderna y gratuita para gestionar inventario y productos en almacenes de cualquier tamaño
¡organiza tu mundo como si fuera el fin del mundo!"


"Tecnología del mañana, ¡hoy mismo en su almacén! Con inventory, el futuro de la logística... está asegurado."
## Descripcion General
Este proyecto simula un sistema de gestión de inventarios,no se enfoca en una area en especifico ya que esta diseñado para que cada persona pueda tomarlo y modificiarlo segun sus necesidades, fue desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El sistema permite:
- Registrar productos.
- Asignarles registro y categoria.
- modificar precios y stock.
- Mantener un registro de todos los movimientos realizados.
- Observar el atologo completo.
## Enfoque de la solucion
Primero se abordo el problema desde un punto de vista utilitarista.

1. Se penso en cuales deberian ser los primeros procesos que debia poder realizar el inventario.
2. Se pensaron las clases y el como podrian estar relacionadas entre si.
3. Se generaron funciones especificas para hacer cosas tales como : generar registros, generar productos etc.
4. Una vez comprobado que las funciones hicieran su trabajo de forma indivudual se fueron organizando mediante las clases propuestas anteriormente, aunque durante el proceso hubieron algunos cambios y cosas eliminadas.
5. Se pulio el acabado y se organizo en paquetes para facilidad de futuras ediciones, cambios y mejoras.

## Diagrama de clases
Este diagrama muestra el diagrama actual del proyecto.

```mermaid
classDiagram
    class Producto {
        -str _codigo
        -str _nombre
        -float _precio
        -int _stock
        -str _categoria
        -datetime _fecha_creacion
        +__init__(codigo, nombre, precio, stock, categoria)
        +modificar_stock(cantidad, operacion) tuple
        +actualizar_precio(nuevo_precio) str
        +__str__() str
    }

    class Catalogo {
        -dict _productos
        +__init__()
        +agregar_producto(codigo, nombre, precio, stock, categoria) tuple
        +buscar_producto(codigo) Producto
        +eliminar_producto(codigo) str
        +listar_productos()
        +obtener_todos() list
    }

    class GestorCategorias {
        -list _categorias
        +__init__()
        +crear_categoria(nombre_categoria) tuple
        +listar_categorias()
        +seleccionar_categoria() tuple
        +tiene_categorias() bool
    }

    class Historial {
        -list _cambios
        +__init__()
        +registrar_cambio(descripcion)
        +ver_historial()
        +obtener_cambios() list
    }

    class ExportadorExcel {
        +__init__()
        +exportar_catalogo(productos) str
        -_aplicar_formato(ws)
    }

    class SistemaInventario {
        -catalogo
        -categorias
        -historial
        -exportador
        +__init__()
        +mostrar_menu()
        +menu_crear_producto()
        +menu_modificar_stock()
        +menu_actualizar_precio()
        +menu_gestionar_categorias()
        +menu_eliminar_producto()
        +menu_exportar()
        +ejecutar()
    }

    SistemaInventario "1" --> "1" Catalogo : tiene
    SistemaInventario "1" --> "1" GestorCategorias : tiene
    SistemaInventario "1" --> "1" Historial : tiene
    SistemaInventario "1" --> "1" ExportadorExcel : tiene
    Catalogo "1" --> "*" Producto : gestiona
    ExportadorExcel --> Producto : exporta
```
y el empaquetado se ve de la siguiente forma: 
```
inventario/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── catalogo.py
│   ├── categorias.py
│   └── historial.py
├── exportador.py
└── sistema.py        
```
##  Implementación del codigo:

##  Requisitos previos
Para este codigo sera necesario tener instalado python y la libreria openpyxl.
- Versión mínima requerida: Python 3.7.
- Versión recomendada: Python 3.9.

Además, para el correcto funcionamiento del codigo se debera instalar openpyxl, para hacerlo se puede ir a nuestra consola y escribir :
```cmd
pip install openpyxl
```

##  Funcionamiento 
1. Debera descargar la carpeta llamada inventario, una vez hecho esto podra abrirla desde su visualizador de codigo de confianza.
2. El programa se ejecuta desde 
```cmd
Inventario/sistema.py
```
o bien puede hacer lo anterior o abrir el codigo en el editor y ejecutarlo desde ahi.

3. Se ejecutará una ventana en la consola en la cual se le solicitara que elija alguna de las opciones. 

<img width="700" height="532" alt="image" src="Screenshot 2025-07-23 141635.png" />


4. Como puede ver las diversas opciones le permitiran gestionar el inventario. Aqui una explicacion de que hace cada una:
 -*Crear nuevo producto*: con esto podra crear un producto base del cual se generaran los paquetes, de aqui podras partir para armar tus paquetes
   
   -*Crear paquetes*: Toma los productos base que has generado y te permite dar una cantidad de cuantos tienes de estos.

   -*Ver productos*: Te permite ver que productos tienes creados.

   -*Ver contenido del almacen*: Te permite ver que paquetes tienes creados.

   -*Exportar almacen a excel*: Te permite generar un excel con los paquetes que tienes generados, este te dirá cuantos tienes, que precio tiene el producto unitario, que precio tiene el rpoducto total la categoria y el stock que tienes.

   -*Historial de cambios*: Aqui podras ver todos los productos y paquetes que se han creado, tambien los archivos excel que se han generado.

   -*Registros*:

   -*Editar producto*:Aqui podras cambiarle el precio a el stock que tienes al producto

   -*Borrar producto*: Aqui podras eliminar los productos que ya no desees.

   -*Borrar paquete*: Aqui podras borrar los paquetes que ya no desees.

## Observaciones

Este codigo no está finalizado por ende tiene diversos inconvenientes:

- Aun no tiene la posibilidad de tener una persistencia de datos.
- Al generar un nuevo informe de los paquetes será necesario que se elimine el anterior y se remplace por el nuevo, esto puesto que aun no se genera de forma dinamica.
- Aun no se le ah añadido la funcion de edicion para los paquetes.

  

   





---

## Equipo Nuka-POOla


Nuestro grupo eligio la alternativa 1.

En esta se plantea un sistema de gestion de inventario para una bodega, nuestro grupo la tomo y espera centrarla en un sistema que pueda funcionar como sistema de envios, algo similar a los sistemas de los cuales disponen empresas tales como amazon, temu, entre otros.

Este sistema se plantea con diversas funciones y metodos mediante los cuales esperamos hacerlo trabajar. El funcionamiento esperado seria: 

Recibir la entrada de un objeto o paquete nuevo: El programa anotará la hora de entrada; asignará un numero de registro (con el cual se rastrearía el paquete); asignará un "espacio", en el cual dicho paquete se almacenaría hasta el momento de salida para que, cuando vaya a salir el paquete, sea llamado y  enviado fuera de la bodega; y, por último, se anotará su horario de salida. Se espera que con el numero de registro se pueda clasificar los paquetes en diferentes modulos mediante los cuales sea mas sencillo gestionarlos. Por ejemplo, se separarían de tal forma como: frágiles, pesados, vivos, urgencia, etc. Esto permite una gestion correcta y eficiente, ya que el usuario puede determinar cuales son los que llevan prioridad, dónde deben estar organizados, y si requieren algun trato especial, para posteriormente ser enviado a donde se haya encargado.  

Algunas de las ventajes del numero de registro son las siguientes:
1. clasificar los paquetes en diferentes modulos mediante los cuales sea mas sencillo gestionarlos. 
2. Asignarle caracteristicas especificas a los paquetes, por ejemplo: fragiles, pesados, vivos, , etc.
3. Permitir que el usuario determine la prioridad de cada paquete, ya sea: urgente, normal, baja prioridad.
4. generar una base de datos organizada con base en el numerode registro asociado al paquete, facilitando asi la busqueda de informacion y datos tales como: fecha de entrada, fecha de salida, caracteristicas del paquete, si esta el paquete en la bodega etc. (esto se piensa como tipo tabla de datos en exel que se pueda descargar)
