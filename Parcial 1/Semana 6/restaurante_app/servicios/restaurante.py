"""
Clase Restaurante que administra los productos (platillos y bebidas) disponibles.
"""

from typing import List
from modelos import Producto, Platillo, Bebida


class Restaurante:
    """
    Clase de servicio que administra una lista de productos registrados en el restaurante.
    Permite agregar productos y mostrar su información de manera organizada.
    """

    def __init__(self, nombre_restaurante: str):
        """
        Inicializa el restaurante.

        Args:
            nombre_restaurante (str): El nombre del restaurante.
        """
        self.nombre = nombre_restaurante
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un producto a la lista del restaurante.

        Args:
            producto (Producto): El producto a agregar (Platillo o Bebida).

        Returns:
            bool: True si el producto fue agregado, False en caso contrario.
        """
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"✅ Producto agregado: {producto.nombre}")
            return True
        print("❌ Error: El objeto no es un producto válido.")
        return False

    def listar_productos(self) -> None:
        """
        Muestra todos los productos registrados en el restaurante.
        Demuestra polimorfismo al ejecutar mostrar_informacion() en cada producto,
        que se ejecuta diferente según sea Platillo o Bebida.
        """
        if not self.productos:
            print("⚠️  No hay productos registrados en el restaurante.")
            return

        print(f"\n{'='*90}")
        print(f"🏪 MENÚ DEL RESTAURANTE: {self.nombre.upper()}")
        print(f"{'='*90}\n")

        # Separamos platillos y bebidas para mostrar de manera organizada
        platillos = [p for p in self.productos if isinstance(p, Platillo)]
        bebidas = [b for b in self.productos if isinstance(b, Bebida)]

        if platillos:
            print("📋 PLATILLOS:")
            print("-" * 90)
            for platillo in platillos:
                # Polimorfismo: cada tipo de producto ejecuta su propia versión de mostrar_informacion()
                platillo.mostrar_informacion()
            print()

        if bebidas:
            print("🥤 BEBIDAS:")
            print("-" * 90)
            for bebida in bebidas:
                # Polimorfismo: cada tipo de producto ejecuta su propia versión de mostrar_informacion()
                bebida.mostrar_informacion()
            print()

        print(f"{'='*90}\n")

    def obtener_total_productos(self) -> int:
        """
        Retorna el total de productos registrados.

        Returns:
            int: Cantidad de productos en el restaurante.
        """
        return len(self.productos)

    def obtener_productos_disponibles(self) -> List[Producto]:
        """
        Retorna una lista solo de productos disponibles.

        Returns:
            List[Producto]: Lista de productos disponibles.
        """
        return [p for p in self.productos if p.disponible]

    def cambiar_disponibilidad(self, nombre_producto: str, disponible: bool) -> bool:
        """
        Cambia la disponibilidad de un producto.

        Args:
            nombre_producto (str): El nombre del producto a modificar.
            disponible (bool): El nuevo estado de disponibilidad.

        Returns:
            bool: True si se cambió la disponibilidad, False si no se encontró el producto.
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                producto.disponible = disponible
                estado = "disponible" if disponible else "no disponible"
                print(f"✅ {producto.nombre} ahora está {estado}.")
                return True
        print(f"❌ No se encontró el producto '{nombre_producto}'.")
        return False

    def mostrar_estadisticas(self) -> None:
        """
        Muestra estadísticas generales del restaurante.
        """
        total = self.obtener_total_productos()
        disponibles = len(self.obtener_productos_disponibles())
        platillos = len([p for p in self.productos if isinstance(p, Platillo)])
        bebidas = len([b for b in self.productos if isinstance(b, Bebida)])

        print("\n📊 ESTADÍSTICAS DEL RESTAURANTE:")
        print("-" * 50)
        print(f"Total de productos: {total}")
        print(f"Productos disponibles: {disponibles}")
        print(f"Platillos: {platillos}")
        print(f"Bebidas: {bebidas}")
        print("-" * 50 + "\n")
