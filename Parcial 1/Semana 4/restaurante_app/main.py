"""
Archivo principal del sistema de gestión de restaurante.
Define el punto de entrada de la aplicación.

Este script demuestra el funcionamiento del sistema mediante:
- Creación de instancias de Producto
- Creación de instancias de Cliente
- Operaciones del Restaurante (agregar productos, clientes, crear pedidos)
- Visualización de información del sistema
"""

# Importar las clases necesarias desde sus módulos
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que inicializa y demuestra el funcionamiento del sistema.
    """

    # ==================== 1. CREAR INSTANCIA DEL RESTAURANTE ====================
    print("\n🍽️  INICIALIZANDO SISTEMA DE GESTIÓN DE RESTAURANTE 🍽️\n")

    restaurante = Restaurante("La Buena Comida", "Calle Principal 123, Centro")
    print(f"✓ {restaurante} creado exitosamente.\n")


    # ==================== 2. CREAR PRODUCTOS ====================
    print("📦 Creando productos del catálogo...\n")

    # Entradas
    entrada1 = Producto(
        "Tabla de Quesos y Embutidos",
        "Selección variada de quesos artesanales y embutidos españoles",
        12.50,
        "Entrada"
    )

    entrada2 = Producto(
        "Ceviche Clásico",
        "Pescado fresco marinado en jugo de limón",
        10.00,
        "Entrada"
    )

    # Platos Principales
    principal1 = Producto(
        "Filete a la Parrilla",
        "Carne premium asada con verduras al grill",
        24.99,
        "Plato Principal"
    )

    principal2 = Producto(
        "Pasta Alfredo con Pollo",
        "Pasta fresca en salsa cremosa con pechuga de pollo",
        16.50,
        "Plato Principal"
    )

    principal3 = Producto(
        "Salmón a la Mantequilla",
        "Salmón fresco con salsa de mantequilla y limón",
        22.00,
        "Plato Principal"
    )

    # Postres
    postre1 = Producto(
        "Tiramisú Casero",
        "Postre italiano tradicional con mascarpone y café",
        7.50,
        "Postre"
    )

    postre2 = Producto(
        "Brownie de Chocolate",
        "Brownie caliente con helado de vainilla",
        6.00,
        "Postre"
    )

    # Bebidas
    bebida1 = Producto(
        "Agua Embotellada",
        "Agua mineral sin gas",
        1.50,
        "Bebida"
    )

    bebida2 = Producto(
        "Vino Tinto Reserva",
        "Vino tinto de cosecha 2018",
        15.00,
        "Bebida"
    )

    bebida3 = Producto(
        "Jugo de Naranja Natural",
        "Jugo natural recién exprimido",
        3.50,
        "Bebida"
    )

    # Agregar todos los productos al restaurante
    productos = [entrada1, entrada2, principal1, principal2, principal3,
                 postre1, postre2, bebida1, bebida2, bebida3]

    for producto in productos:
        restaurante.agregar_producto(producto)


    # ==================== 3. CREAR CLIENTES ====================
    print("\n👥 Registrando clientes del restaurante...\n")

    cliente1 = Cliente("Juan Pérez", "juan.perez@email.com", "+34 612 345 678")
    cliente2 = Cliente("María García", "maria.garcia@email.com", "+34 698 765 432")
    cliente3 = Cliente("Carlos López", "carlos.lopez@email.com", "+34 654 321 987")

    clientes = [cliente1, cliente2, cliente3]

    for cliente in clientes:
        restaurante.agregar_cliente(cliente)


    # ==================== 4. MOSTRAR CATÁLOGO DE PRODUCTOS ====================
    restaurante.listar_productos()


    # ==================== 5. MOSTRAR CLIENTES REGISTRADOS ====================
    restaurante.listar_clientes()


    # ==================== 6. CREAR PEDIDOS ====================
    print("📋 Creando pedidos de clientes...\n")

    # Pedido del cliente 1 (Juan)
    # Toma: tabla de quesos (1000), filete parrilla (1002), tiramisú (1005), vino (1008)
    pedido1 = restaurante.crear_pedido(500, [1000, 1002, 1005, 1008])
    if pedido1:
        print(f"✓ Pedido #{pedido1['numero']} creado para {pedido1['cliente']}")
        print(f"  Total: ${pedido1['total']:.2f}\n")

    # Pedido del cliente 2 (María)
    # Toma: ceviche (1001), pasta alfredo (1003), brownie (1006), jugo (1009)
    pedido2 = restaurante.crear_pedido(501, [1001, 1003, 1006, 1009])
    if pedido2:
        print(f"✓ Pedido #{pedido2['numero']} creado para {pedido2['cliente']}")
        print(f"  Total: ${pedido2['total']:.2f}\n")

    # Pedido del cliente 3 (Carlos)
    # Toma: salmón mantequilla (1004), agua (1007)
    pedido3 = restaurante.crear_pedido(502, [1004, 1007])
    if pedido3:
        print(f"✓ Pedido #{pedido3['numero']} creado para {pedido3['cliente']}")
        print(f"  Total: ${pedido3['total']:.2f}\n")


    # ==================== 7. MOSTRAR TODOS LOS PEDIDOS ====================
    restaurante.listar_pedidos()


    # ==================== 8. MOSTRAR RESUMEN GENERAL ====================
    restaurante.mostrar_resumen()


    # ==================== 9. DEMOSTRACIÓN DE MÉTODOS ADICIONALES ====================
    print("📊 CONSULTAS Y ANÁLISIS DEL SISTEMA:\n")
    print("="*80)

    # Mostrar productos disponibles
    productos_disponibles = restaurante.obtener_productos_disponibles()
    print(f"\n✓ Total de productos disponibles: {len(productos_disponibles)}")

    # Mostrar productos por categoría
    print("\n✓ Cantidad de productos por categoría:")
    categorias = set(p.categoria for p in restaurante.productos)
    for categoria in sorted(categorias):
        cantidad = len(restaurante.obtener_productos_por_categoria(categoria))
        print(f"  - {categoria}: {cantidad} productos")

    # Mostrar información de clientes específicos
    print("\n✓ Información detallada de clientes:")
    for cliente in restaurante.clientes:
        info = cliente.obtener_info()
        print(f"  - {info['nombre']}: {info['total_pedidos']} pedido(s) realizados")

    print("\n" + "="*80)
    print("\n✓ Sistema de gestión de restaurante finalizado correctamente.\n")


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Se ejecuta cuando el archivo se corre directamente.
    """
    main()

