"""
Clase padre Producto que representa un producto general del restaurante.
"""


class Producto:
    """
    Clase padre que define los atributos y métodos comunes a todos los productos del restaurante.
    """

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        """
        Inicializa un producto con los atributos básicos.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto. Debe ser mayor a cero.
            disponible (bool): Indica si el producto está disponible. Por defecto es True.
        """
        self.nombre = nombre
        # Encapsulación: precio es privado, solo se modifica a través de métodos
        self.__precio = None
        self.disponible = disponible
        # Validamos el precio mediante el método setter
        self.cambiar_precio(precio)

    def cambiar_precio(self, nuevo_precio: float) -> bool:
        """
        Modifica el precio del producto con validación.

        Args:
            nuevo_precio (float): El nuevo precio del producto.

        Returns:
            bool: True si el precio fue modificado exitosamente, False en caso contrario.
        """
        if nuevo_precio <= 0:
            print(f"⚠️ Error: El precio debe ser mayor a cero. Precio actual: ${self.__precio:.2f}")
            return False
        self.__precio = nuevo_precio
        return True

    def obtener_precio(self) -> float:
        """
        Retorna el precio del producto.

        Returns:
            float: El precio encapsulado del producto.
        """
        return self.__precio

    def mostrar_informacion(self) -> None:
        """
        Muestra la información básica del producto.
        Este método será sobrescrito en las clases hijas para demostrar polimorfismo.
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        print(f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | {estado}")

    def __str__(self) -> str:
        """Representación en string del producto."""
        return f"Producto({self.nombre}, ${self.__precio:.2f})"
