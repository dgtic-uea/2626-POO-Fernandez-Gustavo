# Clase Mascota - Programación Orientada a Objetos
# Implementa atributos, métodos y abstracción

class Mascota:
    """Clase que representa una mascota con sus características y comportamientos"""
    
    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota
        
        Atributos:
            nombre (str): El nombre de la mascota
            especie (str): La especie de la mascota
            edad (int): La edad de la mascota en años
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    
    def mostrar_informacion(self):
        """
        Método que muestra la información completa de la mascota
        de forma organizada y clara
        """
        print("\n" + "="*50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad} años")
        print("="*50)
    
    
    def hacer_sonido(self):
        """
        Método que emite el sonido típico de la mascota
        según su especie
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pajaro": "¡Pío pío!",
            "hamster": "¡Pip pip!",
            "conejo": "¡Ñam ñam!",
            "pez": "Burbuja...",
        }
        
        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "Sonido desconocido")
        
        print(f"\n{self.nombre} ({self.especie}): {sonido}")

