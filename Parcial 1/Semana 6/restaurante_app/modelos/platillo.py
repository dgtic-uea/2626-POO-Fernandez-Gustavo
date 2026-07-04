"""
Clase Platillo que hereda de Producto y representa una comida del restaurante.
"""

from .producto import Producto


class Platillo(Producto):
    """
    Clase que representa un platillo del restaurante.
    Hereda de Producto y agrega atributos específicos: calorías y tipo de platillo.
    """

    def __init__(
        self,
        nombre: str,
        precio: float,
        calorias: int,
        tipo_platillo: str,
        disponible: bool = True
    ):
        """
        Inicializa un platillo con sus atributos específicos.

        Args:
            nombre (str): El nombre del platillo.
            precio (float): El precio del platillo. Debe ser mayor a cero.
            calorias (int): Número de calorías del platillo.
            tipo_platillo (str): Tipo del platillo (ej: "Entrada", "Principal", "Postre").
            disponible (bool): Indica si está disponible. Por defecto es True.
        """
        # Llamamos a super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias
        self.tipo_platillo = tipo_platillo

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método de la clase padre para mostrar información específica del platillo.
        Demuestra polimorfismo: mismo método, diferentes implementaciones.
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        print(
            f"🍽️  PLATILLO | {self.tipo_platillo}: {self.nombre} | "
            f"Precio: ${self.obtener_precio():.2f} | Calorías: {self.calorias} cal | {estado}"
        )

    def __str__(self) -> str:
        """Representación en string del platillo."""
        return f"Platillo({self.nombre}, ${self.obtener_precio():.2f}, {self.calorias} cal)"
