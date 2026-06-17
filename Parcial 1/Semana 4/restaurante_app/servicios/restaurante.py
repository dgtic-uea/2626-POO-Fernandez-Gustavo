"""
Módulo que define la clase Restaurante para gestionar el sistema del restaurante.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.
    Administra productos, clientes y pedidos del sistema.

    Atributos:
        - nombre: nombre del restaurante
        - ubicacion: ubicación del restaurante
        - productos: lista de productos disponibles
        - clientes: lista de clientes registrados
        - pedidos: lista de pedidos realizados
    """

    def __init__(self, nombre, ubicacion):
        """
        Constructor que inicializa un nuevo restaurante.

        Args:
            nombre: nombre del restaurante
            ubicacion: ubicación del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []  # Lista de productos disponibles
        self.clientes = []   # Lista de clientes registrados
        self.pedidos = []    # Lista de pedidos realizados
        self.contador_pedidos = 1  # Contador para generar números de pedido

    # ==================== GESTIÓN DE PRODUCTOS ====================

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al catálogo del restaurante.

        Args:
            producto: instancia de la clase Producto
        """
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"✓ Producto '{producto.nombre}' agregado exitosamente.")
        else:
            print("✗ Error: el objeto no es una instancia de Producto.")

    def obtener_productos_por_categoria(self, categoria):
        """
        Obtiene todos los productos de una categoría específica.

        Args:
            categoria: categoría a filtrar

        Returns:
            lista de productos de esa categoría
        """
        return [p for p in self.productos if p.categoria == categoria]

    def obtener_productos_disponibles(self):
        """
        Obtiene todos los productos que están disponibles.

        Returns:
            lista de productos disponibles
        """
        return [p for p in self.productos if p.disponible]

    def listar_productos(self):
        """
        Muestra en consola todos los productos del restaurante de forma organizada.
        """
        if not self.productos:
            print("\n📭 No hay productos registrados en el restaurante.")
            return

        print("\n" + "="*80)
        print(f"{'CATÁLOGO DE PRODUCTOS':^80}")
        print("="*80)

        # Agrupar productos por categoría
        categorias = set(p.categoria for p in self.productos)

        for categoria in sorted(categorias):
            productos_categoria = self.obtener_productos_por_categoria(categoria)
            print(f"\n🍽️  {categoria.upper()}")
            print("-" * 80)
            for producto in productos_categoria:
                print(f"  {producto}")

        print("\n" + "="*80 + "\n")

    # ==================== GESTIÓN DE CLIENTES ====================

    def agregar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema del restaurante.

        Args:
            cliente: instancia de la clase Cliente
        """
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente)
            print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
        else:
            print("✗ Error: el objeto no es una instancia de Cliente.")

    def buscar_cliente_por_id(self, cliente_id):
        """
        Busca un cliente por su ID.

        Args:
            cliente_id: ID del cliente a buscar

        Returns:
            instancia del Cliente o None si no lo encuentra
        """
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def listar_clientes(self):
        """
        Muestra en consola todos los clientes registrados de forma organizada.
        """
        if not self.clientes:
            print("\n👥 No hay clientes registrados en el sistema.")
            return

        print("\n" + "="*80)
        print(f"{'CLIENTES REGISTRADOS':^80}")
        print("="*80)

        for cliente in self.clientes:
            print(f"  {cliente}")

        print("="*80 + "\n")

    # ==================== GESTIÓN DE PEDIDOS ====================

    def crear_pedido(self, cliente_id, productos_pedido):
        """
        Crea un nuevo pedido para un cliente.

        Args:
            cliente_id: ID del cliente que realiza el pedido
            productos_pedido: lista de IDs de productos en el pedido

        Returns:
            diccionario con información del pedido (número, total, etc.)
        """
        cliente = self.buscar_cliente_por_id(cliente_id)

        if not cliente:
            print(f"✗ Error: cliente con ID {cliente_id} no encontrado.")
            return None

        # Buscar los productos
        productos_encontrados = []
        total = 0

        for prod_id in productos_pedido:
            producto = next((p for p in self.productos if p.id == prod_id), None)
            if producto and producto.disponible:
                productos_encontrados.append(producto)
                total += producto.precio
            else:
                print(f"⚠️  Producto {prod_id} no disponible.")

        if not productos_encontrados:
            print("✗ Error: no hay productos disponibles para este pedido.")
            return None

        # Crear el pedido
        numero_pedido = self.contador_pedidos
        self.contador_pedidos += 1

        pedido = {
            'numero': numero_pedido,
            'cliente': cliente.nombre,
            'cliente_id': cliente_id,
            'productos': productos_encontrados,
            'total': total
        }

        self.pedidos.append(pedido)
        cliente.agregar_pedido(numero_pedido)

        return pedido

    def listar_pedidos(self):
        """
        Muestra en consola todos los pedidos realizados de forma organizada.
        """
        if not self.pedidos:
            print("\n📋 No hay pedidos registrados.")
            return

        print("\n" + "="*80)
        print(f"{'PEDIDOS REALIZADOS':^80}")
        print("="*80)

        for pedido in self.pedidos:
            print(f"\n📍 Pedido #{pedido['numero']} | Cliente: {pedido['cliente']} | Total: ${pedido['total']:.2f}")
            print("   Productos:")
            for producto in pedido['productos']:
                print(f"   - {producto.nombre} (${producto.precio:.2f})")

        print("\n" + "="*80 + "\n")

    # ==================== INFORMACIÓN GENERAL ====================

    def mostrar_resumen(self):
        """
        Muestra un resumen general del estado del restaurante.
        """
        print("\n" + "="*80)
        print(f"{'RESUMEN DEL RESTAURANTE':^80}")
        print("="*80)
        print(f"\n🏪 Restaurante: {self.nombre}")
        print(f"📍 Ubicación: {self.ubicacion}")
        print(f"\n📦 Total de productos: {len(self.productos)}")
        print(f"   - Disponibles: {len(self.obtener_productos_disponibles())}")
        print(f"\n👥 Total de clientes: {len(self.clientes)}")
        print(f"\n📋 Total de pedidos: {len(self.pedidos)}")
        if self.pedidos:
            ingresos_totales = sum(p['total'] for p in self.pedidos)
            print(f"💰 Ingresos totales: ${ingresos_totales:.2f}")

        print("\n" + "="*80 + "\n")

    def __str__(self):
        """Representación en texto del restaurante."""
        return f"Restaurante '{self.nombre}' en {self.ubicacion}"

    def __repr__(self):
        """Representación para desarrolladores."""
        return f"Restaurante(nombre='{self.nombre}', ubicacion='{self.ubicacion}')"

