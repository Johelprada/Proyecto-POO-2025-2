from datetime import datetime


#  Clase que gestiona el historial de cambios del sistema
class Historial:
    """
    Aqui se registran los cambios realizados con fecha y hora de estos
    """
    def __init__(self):
        # Lista privada que almacena los cambios
        self._cambios = []  
    
    #  Metodo para registrar un nuevo cambio
    def registrar_cambio(self, descripcion: str):

        """se agrega un cambio al historial con fecha y hora"""

        cambio_completo = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {descripcion}"
        self._cambios.append(cambio_completo)
    
    def ver_historial(self):
        # Verificamos si la lista de cambios esta vacia
        if not self._cambios:
            print("No hay cambios registrados aun")
            return
        
        print("\n" + "="*70)
        print("HISTORIAL DE CAMBIOS")
        print("="*70)
        
        # Recorremos la lista de cambios con enumerate para obtener el indice
        for i, cambio in enumerate(self._cambios, 1):
            print(f"{i}. {cambio}")
        
        print("="*70)
    
    #  Metodo para obtener todos los cambios (no lo estoy usando del todo aun)
    def obtener_cambios(self):
        """ Retorna una copia de la lista de cambios"""
        return self._cambios.copy()