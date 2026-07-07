"""
Módulo Producto: contiene la clase Producto con constructor tradicional,
decoradores @property y @setter para encapsulación de atributos.
"""


class Producto:
    """
    Clase que representa un producto disponible en el restaurante.

    Utiliza constructor tradicional __init__ y decoradores @property y @setter
    para el control de acceso y validación de atributos.

    Atributos:
        nombre: nombre del producto
        categoria: categoría del producto (ej: bebida, platillo, postre)
        precio: precio unitario del producto
        disponible: booleano indicando disponibilidad
    """

    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor del producto.

        Args:
            nombre: nombre del producto (no vacío)
            categoria: categoría del producto (no vacía)
            precio: precio del producto (> 0)
            disponible: disponibilidad inicial (default: True)
        """
        # Usamos los setters para validar los datos al crear el objeto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self._disponible = disponible

    # ========== PROPIEDADES Y SETTERS PARA NOMBRE ==========
    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Establece el nombre del producto con validación.

        Args:
            valor: nombre a establecer

        Raises:
            ValueError: si el nombre está vacío
        """
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # ========== PROPIEDADES Y SETTERS PARA CATEGORÍA ==========
    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """
        Establece la categoría del producto con validación.

        Args:
            valor: categoría a establecer

        Raises:
            ValueError: si la categoría está vacía
        """
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    # ========== PROPIEDADES Y SETTERS PARA PRECIO ==========
    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """
        Establece el precio del producto con validación.

        Args:
            valor: precio a establecer

        Raises:
            ValueError: si el precio no es mayor que cero
        """
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            self._precio = precio_float
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido mayor que cero.")

    # ========== PROPIEDADES Y SETTERS PARA DISPONIBILIDAD ==========
    @property
    def disponible(self):
        """Obtiene el estado de disponibilidad del producto."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        """
        Establece la disponibilidad del producto.

        Args:
            valor: booleano indicando disponibilidad
        """
        self._disponible = bool(valor)

    # ========== MÉTODO DE INFORMACIÓN ==========
    def mostrar_informacion(self):
        """
        Retorna una representación legible de la información del producto.

        Returns:
            str: información formateada del producto
        """
        estado = "✓ Disponible" if self.disponible else "✗ No disponible"
        return (
            f"Producto: {self.nombre}\n"
            f"  Categoría: {self.categoria}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Estado: {estado}"
        )

    def __str__(self):
        """Representación en string del producto."""
        return f"{self.nombre} (${self.precio:.2f}) - {self.categoria}"

    def __repr__(self):
        """Representación técnica del producto."""
        return f"Producto(nombre='{self.nombre}', categoria='{self.categoria}', precio={self.precio}, disponible={self.disponible})"

