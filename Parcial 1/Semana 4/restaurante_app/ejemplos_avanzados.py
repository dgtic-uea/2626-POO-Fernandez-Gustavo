"""
Archivo adicional con ejemplos avanzados y posibles extensiones del sistema.

Nota: Este archivo NO es requerido para la actividad, es solo para referencia
y demostración de cómo extender el sistema.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def ejemplo_consultas_avanzadas():
    """
    Demuestra consultas y análisis más complejos del sistema.
    """
    print("\n" + "="*80)
    print(f"{'EJEMPLOS DE CONSULTAS AVANZADAS':^80}")
    print("="*80 + "\n")

    # Crear instancia del restaurante
    restaurante = Restaurante("La Buena Comida", "Calle Principal 123")

    # Agregar algunos productos
    productos = [
        Producto("Entrada Especial", "Entrada fina", 15.00, "Entrada"),
        Producto("Filete Prime", "Carne premium", 35.00, "Plato Principal"),
        Producto("Agua", "Agua mineral", 2.00, "Bebida"),
    ]

    for p in productos:
        restaurante.agregar_producto(p)

    # Consulta: Productos más caros
    print("📊 LOS 3 PRODUCTOS MÁS CAROS:")
    productos_ordenados = sorted(restaurante.productos,
                                key=lambda p: p.precio, reverse=True)[:3]
    for i, prod in enumerate(productos_ordenados, 1):
        print(f"  {i}. {prod.nombre} - ${prod.precio:.2f}")

    # Consulta: Precio promedio
    if restaurante.productos:
        precio_promedio = sum(p.precio for p in restaurante.productos) / len(restaurante.productos)
        print(f"\n💰 PRECIO PROMEDIO DE PRODUCTOS: ${precio_promedio:.2f}")

    # Consulta: Productos en rango de precio
    print(f"\n🎯 PRODUCTOS ENTRE $10 Y $30:")
    productos_rango = [p for p in restaurante.productos
                      if 10 <= p.precio <= 30]
    if productos_rango:
        for prod in productos_rango:
            print(f"  - {prod.nombre}: ${prod.precio:.2f}")
    else:
        print("  No hay productos en este rango.")


def ejemplo_cambio_disponibilidad():
    """
    Demuestra cómo cambiar la disponibilidad de productos.
    """
    print("\n" + "="*80)
    print(f"{'EJEMPLO: CAMBIO DE DISPONIBILIDAD':^80}")
    print("="*80 + "\n")

    # Crear un producto
    pasta = Producto("Pasta a la Carbonara", "Pasta italiana clásica", 14.50, "Plato Principal")

    print(f"Estado inicial: {pasta}")

    # Cambiar disponibilidad
    pasta.cambiar_disponibilidad(False)
    print(f"Después de no disponible: {pasta}")

    # Cambiar nuevamente
    pasta.cambiar_disponibilidad(True)
    print(f"Disponible nuevamente: {pasta}")


def ejemplo_historial_cliente():
    """
    Demuestra cómo rastrear el historial de pedidos de un cliente.
    """
    print("\n" + "="*80)
    print(f"{'EJEMPLO: HISTORIAL DE CLIENTES':^80}")
    print("="*80 + "\n")

    # Crear cliente
    cliente = Cliente("Ana Martínez", "ana@email.com", "+34 666 444 555")

    # Simular varios pedidos
    for pedido_num in [1001, 1002, 1003]:
        cliente.agregar_pedido(pedido_num)

    print(f"Cliente: {cliente.nombre}")
    print(f"Email: {cliente.email}")
    print(f"Teléfono: {cliente.telefono}")
    print(f"Total de pedidos realizados: {cliente.obtener_cantidad_pedidos()}")
    print(f"Números de pedidos: {cliente.pedidos}")


def ejemplo_busqueda_cliente():
    """
    Demuestra búsqueda de clientes por ID y análisis.
    """
    print("\n" + "="*80)
    print(f"{'EJEMPLO: BÚSQUEDA Y ANÁLISIS DE CLIENTES':^80}")
    print("="*80 + "\n")

    # Crear restaurante y clientes
    restaurante = Restaurante("La Buena Comida", "Centro")

    clientes_data = [
        ("Roberto Silva", "roberto@email.com", "+34 611 222 333"),
        ("Laura Gómez", "laura@email.com", "+34 622 333 444"),
        ("Miguel Rodríguez", "miguel@email.com", "+34 633 444 555"),
    ]

    for nombre, email, telefono in clientes_data:
        restaurante.agregar_cliente(Cliente(nombre, email, telefono))

    # Buscar cliente específico
    cliente_buscado = restaurante.buscar_cliente_por_id(501)

    if cliente_buscado:
        info = cliente_buscado.obtener_info()
        print(f"✓ Cliente encontrado:")
        for clave, valor in info.items():
            print(f"  {clave}: {valor}")
    else:
        print("✗ Cliente no encontrado.")

    # Listar todos
    print(f"\nTotal de clientes en el sistema: {len(restaurante.clientes)}")


if __name__ == "__main__":
    """
    Ejecuta los ejemplos avanzados.
    Para correr este archivo:
    $ python3 ejemplos_avanzados.py
    """

    print("\n🍽️  EJEMPLOS AVANZADOS DEL SISTEMA DE RESTAURANTE 🍽️")

    ejemplo_consultas_avanzadas()
    ejemplo_cambio_disponibilidad()
    ejemplo_historial_cliente()
    ejemplo_busqueda_cliente()

    print("\n" + "="*80)
    print("\n✓ Ejemplos completados.\n")

