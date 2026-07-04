"""
Clase Bebida que hereda de Producto y representa una bebida del restaurante.
"""

from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto y agrega atributos específicos: volumen en mililitros y tipo de bebida.
    """

    def __init__(
        self,
        nombre: str,
        precio: float,
        volumen_ml: int,
        tipo_bebida: str,
        disponible: bool = True
    ):
        """
        Inicializa una bebida con sus atributos específicos.

        Args:
            nombre (str): El nombre de la bebida.
            precio (float): El precio de la bebida. Debe ser mayor a cero.
            volumen_ml (int): Volumen de la bebida en mililitros.
            tipo_bebida (str): Tipo de bebida (ej: "Refresco", "Agua", "Jugo", "Cerveza").
            disponible (bool): Indica si está disponible. Por defecto es True.
        """
        # Llamamos a super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método de la clase padre para mostrar información específica de la bebida.
        Demuestra polimorfismo: mismo método, diferentes implementaciones.
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        print(
            f"🥤 BEBIDA | {self.tipo_bebida}: {self.nombre} | "
            f"Precio: ${self.obtener_precio():.2f} | Volumen: {self.volumen_ml} ml | {estado}"
        )

    def __str__(self) -> str:
        """Representación en string de la bebida."""
        return f"Bebida({self.nombre}, ${self.obtener_precio():.2f}, {self.volumen_ml} ml)"
