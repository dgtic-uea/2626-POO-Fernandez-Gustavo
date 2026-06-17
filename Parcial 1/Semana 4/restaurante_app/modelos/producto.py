"""
Módulo que define la clase Producto para representar los items disponibles en el restaurante.
"""


class Producto:
    """
    Representa un producto (plato, bebida o artículo) disponible en el restaurante.

    Atributos:
        - id: identificador único del producto
        - nombre: nombre del producto
        - descripcion: descripción breve del producto
        - precio: precio del producto en moneda local
        - categoria: categoría del producto (ej: Entrada, Plato Principal, Postre, Bebida)
        - disponible: estado de disponibilidad del producto
    """

    # Variable de clase para generar IDs únicos automáticamente
    contador_id = 1000

    def __init__(self, nombre, descripcion, precio, categoria, disponible=True):
        """
        Constructor que inicializa un nuevo producto.

        Args:
            nombre: nombre del producto
            descripcion: descripción breve
            precio: precio en moneda local
            categoria: categoría del producto
            disponible: estado de disponibilidad (True por defecto)
        """
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad del producto.

        Args:
            disponible: nuevo estado de disponibilidad
        """
        self.disponible = disponible

    def obtener_info(self):
        """
        Retorna un diccionario con la información del producto.

        Returns:
            diccionario con los atributos del producto
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': f"${self.precio:.2f}",
            'categoria': self.categoria,
            'disponible': 'Sí' if self.disponible else 'No'
        }

    def __str__(self):
        """
        Representación en texto del producto.
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        return f"[{self.id}] {self.nombre} ({self.categoria}) - ${self.precio:.2f} - {estado}"

    def __repr__(self):
        """Representación para desarrolladores."""
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})"

