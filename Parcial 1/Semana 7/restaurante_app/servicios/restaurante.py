"""
Módulo Restaurante: contiene la clase Restaurante que administra productos
y clientes del restaurante mediante listas.
"""
from modelos import Producto, Cliente


class Restaurante:
    """
    Clase de servicio que administra la lógica de negocio del restaurante.

    Responsabilidades:
        - Administrar una lista de productos disponibles
        - Administrar una lista de clientes registrados
        - Permitir registrar, listar y buscar productos
        - Permitir registrar, listar y buscar clientes
    """

    def __init__(self, nombre="Mi Restaurante"):
        """
        Constructor del restaurante.

        Args:
            nombre: nombre del restaurante (default: "Mi Restaurante")
        """
        self.nombre = nombre
        self._productos = []  # Lista privada de productos
        self._clientes = []   # Lista privada de clientes

    # ========== MÉTODOS PARA PRODUCTOS ==========

    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.

        Args:
            producto: objeto Producto a registrar

        Raises:
            ValueError: si el producto ya existe (mismo nombre)
        """
        if self._buscar_producto_por_nombre(producto.nombre):
            raise ValueError(f"El producto '{producto.nombre}' ya existe en el registro.")
        self._productos.append(producto)

    def listar_productos(self):
        """
        Retorna la lista de todos los productos registrados.

        Returns:
            list: lista de objetos Producto
        """
        return self._productos.copy()

    def buscar_producto(self, criterio, tipo_busqueda="nombre"):
        """
        Busca productos según un criterio específico.

        Args:
            criterio: valor a buscar
            tipo_busqueda: "nombre", "categoria" o "todos" (default: "nombre")

        Returns:
            list: lista de productos encontrados
        """
        resultados = []
        criterio_lower = criterio.lower()

        if tipo_busqueda == "nombre":
            resultados = [p for p in self._productos
                         if criterio_lower in p.nombre.lower()]
        elif tipo_busqueda == "categoria":
            resultados = [p for p in self._productos
                         if criterio_lower in p.categoria.lower()]
        elif tipo_busqueda == "todos":
            resultados = [p for p in self._productos
                         if (criterio_lower in p.nombre.lower() or
                             criterio_lower in p.categoria.lower())]

        return resultados

    def _buscar_producto_por_nombre(self, nombre):
        """
        Método privado para buscar un producto exacto por nombre.

        Args:
            nombre: nombre del producto a buscar

        Returns:
            Producto o None
        """
        for producto in self._productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def obtener_producto(self, nombre):
        """
        Obtiene un producto específico por nombre exacto.

        Args:
            nombre: nombre del producto

        Returns:
            Producto o None si no existe
        """
        return self._buscar_producto_por_nombre(nombre)

    # ========== MÉTODOS PARA CLIENTES ==========

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Args:
            cliente: objeto Cliente a registrar

        Raises:
            ValueError: si el cliente ya existe (mismo ID)
        """
        if self._buscar_cliente_por_id(cliente.id_cliente):
            raise ValueError(f"El cliente con ID '{cliente.id_cliente}' ya existe.")
        self._clientes.append(cliente)

    def listar_clientes(self):
        """
        Retorna la lista de todos los clientes registrados.

        Returns:
            list: lista de objetos Cliente
        """
        return self._clientes.copy()

    def buscar_cliente(self, criterio, tipo_busqueda="nombre"):
        """
        Busca clientes según un criterio específico.

        Args:
            criterio: valor a buscar
            tipo_busqueda: "nombre", "id", "correo" o "todos" (default: "nombre")

        Returns:
            list: lista de clientes encontrados
        """
        resultados = []
        criterio_lower = criterio.lower()

        if tipo_busqueda == "nombre":
            resultados = [c for c in self._clientes
                         if criterio_lower in c.nombre.lower()]
        elif tipo_busqueda == "id":
            resultados = [c for c in self._clientes
                         if criterio_lower in c.id_cliente.lower()]
        elif tipo_busqueda == "correo":
            resultados = [c for c in self._clientes
                         if criterio_lower in c.correo.lower()]
        elif tipo_busqueda == "todos":
            resultados = [c for c in self._clientes
                         if (criterio_lower in c.nombre.lower() or
                             criterio_lower in c.id_cliente.lower() or
                             criterio_lower in c.correo.lower())]

        return resultados

    def _buscar_cliente_por_id(self, id_cliente):
        """
        Método privado para buscar un cliente exacto por ID.

        Args:
            id_cliente: ID del cliente a buscar

        Returns:
            Cliente o None
        """
        for cliente in self._clientes:
            if cliente.id_cliente.lower() == id_cliente.lower():
                return cliente
        return None

    def obtener_cliente(self, id_cliente):
        """
        Obtiene un cliente específico por ID exacto.

        Args:
            id_cliente: ID del cliente

        Returns:
            Cliente o None si no existe
        """
        return self._buscar_cliente_por_id(id_cliente)

    # ========== MÉTODOS DE INFORMACIÓN ==========

    def obtener_estadisticas(self):
        """
        Retorna estadísticas del restaurante.

        Returns:
            dict: diccionario con estadísticas
        """
        productos_disponibles = sum(1 for p in self._productos if p.disponible)
        precio_promedio = sum(p.precio for p in self._productos) / len(self._productos) if self._productos else 0

        return {
            "total_productos": len(self._productos),
            "productos_disponibles": productos_disponibles,
            "precio_promedio": precio_promedio,
            "total_clientes": len(self._clientes)
        }

