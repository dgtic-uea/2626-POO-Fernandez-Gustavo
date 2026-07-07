"""
Módulo main: punto de entrada del sistema de restaurante.

Este módulo contiene el menú interactivo y la lógica principal para:
- Registrar productos desde entrada del usuario
- Registrar clientes desde entrada del usuario
- Listar productos y clientes
- Buscar productos y clientes
- Mostrar estadísticas del restaurante

El flujo demuestra cómo los datos ingresados por el usuario se transforman
en objetos mediante constructores y se administran mediante la clase Restaurante.
"""

from servicios import Restaurante
from modelos import Producto, Cliente


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 48)
    print(" " * 12 + "SISTEMA DE RESTAURANTE")
    print("=" * 48)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 48)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 48)
    print("7. Ver estadísticas")
    print("8. Salir")
    print("=" * 48)


def registrar_producto(restaurante):
    """
    Solicita datos del usuario y registra un nuevo producto.

    Demuestra:
    - Captura de datos mediante input()
    - Validación mediante excepciones
    - Creación de objeto Producto mediante constructor
    - Almacenamiento en clase Restaurante

    Args:
        restaurante: objeto Restaurante donde registrar el producto
    """
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (ej: bebida, platillo, postre): ").strip()
        precio = input("Precio ($): ").strip()
        disponible = input("¿Disponible? (s/n, default: s): ").strip().lower()

        # El constructor del Producto valida automáticamente los datos
        disponible_bool = disponible != 'n'
        producto = Producto(nombre, categoria, precio, disponible_bool)

        # Se registra en el servicio
        restaurante.registrar_producto(producto)
        print(f"✓ Producto '{nombre}' registrado exitosamente.")

    except ValueError as e:
        print(f"✗ Error al registrar producto: {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")


def listar_productos(restaurante):
    """
    Lista todos los productos registrados.

    Demuestra:
    - Recuperación de objetos desde la clase servicio
    - Utilización del método mostrar_informacion()

    Args:
        restaurante: objeto Restaurante
    """
    print("\n--- LISTADO DE PRODUCTOS ---")
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for i, producto in enumerate(productos, 1):
        print(f"\n[{i}] {producto.mostrar_informacion()}")


def buscar_producto(restaurante):
    """
    Busca productos por criterio del usuario.

    Demuestra:
    - Uso del método buscar_producto() del servicio
    - Flexibilidad en búsquedas

    Args:
        restaurante: objeto Restaurante
    """
    print("\n--- BUSCAR PRODUCTO ---")
    print("1. Por nombre")
    print("2. Por categoría")
    print("3. Búsqueda general")

    opcion = input("Seleccione tipo de búsqueda (1-3): ").strip()

    tipos = {"1": "nombre", "2": "categoria", "3": "todos"}
    tipo = tipos.get(opcion, "nombre")

    criterio = input("Ingrese criterio de búsqueda: ").strip()

    if not criterio:
        print("✗ Criterio de búsqueda vacío.")
        return

    resultados = restaurante.buscar_producto(criterio, tipo)

    if not resultados:
        print(f"✗ No se encontraron productos con '{criterio}'.")
        return

    print(f"\n✓ Se encontraron {len(resultados)} producto(s):\n")
    for i, producto in enumerate(resultados, 1):
        print(f"[{i}] {producto.mostrar_informacion()}\n")


def registrar_cliente(restaurante):
    """
    Solicita datos del usuario y registra un nuevo cliente.

    Demuestra:
    - Captura de datos mediante input()
    - Creación de objeto Cliente mediante @dataclass (más simple que Producto)
    - Almacenamiento en clase Restaurante

    Args:
        restaurante: objeto Restaurante donde registrar el cliente
    """
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    try:
        id_cliente = input("ID del cliente (ej: C001): ").strip()
        nombre = input("Nombre completo: ").strip()
        correo = input("Correo electrónico: ").strip()

        # El constructor de Cliente (generado por @dataclass) valida tipos
        cliente = Cliente(id_cliente, nombre, correo)

        # Se registra en el servicio
        restaurante.registrar_cliente(cliente)
        print(f"✓ Cliente '{nombre}' registrado exitosamente.")

    except ValueError as e:
        print(f"✗ Error al registrar cliente: {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")


def listar_clientes(restaurante):
    """
    Lista todos los clientes registrados.

    Demuestra:
    - Recuperación de objetos desde la clase servicio
    - Uso del método mostrar_informacion()

    Args:
        restaurante: objeto Restaurante
    """
    print("\n--- LISTADO DE CLIENTES ---")
    clientes = restaurante.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for i, cliente in enumerate(clientes, 1):
        print(f"\n[{i}] {cliente.mostrar_informacion()}")


def buscar_cliente(restaurante):
    """
    Busca clientes por criterio del usuario.

    Demuestra:
    - Uso del método buscar_cliente() del servicio
    - Múltiples opciones de búsqueda

    Args:
        restaurante: objeto Restaurante
    """
    print("\n--- BUSCAR CLIENTE ---")
    print("1. Por nombre")
    print("2. Por ID")
    print("3. Por correo")
    print("4. Búsqueda general")

    opcion = input("Seleccione tipo de búsqueda (1-4): ").strip()

    tipos = {"1": "nombre", "2": "id", "3": "correo", "4": "todos"}
    tipo = tipos.get(opcion, "nombre")

    criterio = input("Ingrese criterio de búsqueda: ").strip()

    if not criterio:
        print("✗ Criterio de búsqueda vacío.")
        return

    resultados = restaurante.buscar_cliente(criterio, tipo)

    if not resultados:
        print(f"✗ No se encontraron clientes con '{criterio}'.")
        return

    print(f"\n✓ Se encontraron {len(resultados)} cliente(s):\n")
    for i, cliente in enumerate(resultados, 1):
        print(f"[{i}] {cliente.mostrar_informacion()}\n")


def mostrar_estadisticas(restaurante):
    """
    Muestra estadísticas del restaurante.

    Demuestra:
    - Acceso a métodos de información del servicio
    - Procesamiento de datos agregados

    Args:
        restaurante: objeto Restaurante
    """
    print("\n--- ESTADÍSTICAS DEL RESTAURANTE ---")
    stats = restaurante.obtener_estadisticas()

    print(f"Total de productos: {stats['total_productos']}")
    print(f"Productos disponibles: {stats['productos_disponibles']}")
    print(f"Precio promedio: ${stats['precio_promedio']:.2f}")
    print(f"Total de clientes: {stats['total_clientes']}")


def cargar_datos_ejemplo(restaurante):
    """
    Carga datos de ejemplo para demostración.

    Esto permite que el usuario vea inmediatamente cómo funciona el sistema
    con algunos productos y clientes predefinidos.

    Args:
        restaurante: objeto Restaurante
    """
    print("\n⚙ Cargando datos de ejemplo...\n")

    # Crear productos de ejemplo
    productos_ejemplo = [
        Producto("Hamburguesa Clásica", "platillo", 12.50, True),
        Producto("Pizza Margherita", "platillo", 14.99, True),
        Producto("Pasta Alfredo", "platillo", 13.75, True),
        Producto("Refresco Cola", "bebida", 2.50, True),
        Producto("Jugo Natural", "bebida", 4.25, True),
        Producto("Agua Mineral", "bebida", 1.50, True),
        Producto("Tiramisú", "postre", 6.50, True),
        Producto("Helado de Vainilla", "postre", 4.00, True),
    ]

    # Crear clientes de ejemplo
    clientes_ejemplo = [
        Cliente("C001", "Juan Pérez", "juan.perez@email.com"),
        Cliente("C002", "María García", "maria.garcia@email.com"),
        Cliente("C003", "Carlos López", "carlos.lopez@email.com"),
        Cliente("C004", "Ana Martínez", "ana.martinez@email.com"),
        Cliente("C005", "Roberto Sánchez", "roberto.sanchez@email.com"),
    ]

    # Registrar todos los productos
    for producto in productos_ejemplo:
        restaurante.registrar_producto(producto)

    # Registrar todos los clientes
    for cliente in clientes_ejemplo:
        restaurante.registrar_cliente(cliente)

    print("✓ Se han cargado exitosamente:")
    print(f"  - {len(productos_ejemplo)} productos de ejemplo")
    print(f"  - {len(clientes_ejemplo)} clientes de ejemplo")
    print("\nPrueba las opciones del menú para ver cómo interactúa el sistema.")


def main():
    """
    Función principal que ejecuta el menú interactivo del restaurante.

    Demuestra el flujo completo:
    input() → constructor → objeto → almacenamiento → consulta
    """
    # Crear instancia del restaurante (servicio principal)
    restaurante = Restaurante("Restaurante El Buen Sabor")

    # Cargar datos de ejemplo para demostración didáctica
    cargar_datos_ejemplo(restaurante)

    print("\n¡Bienvenido al Sistema de Restaurante!")
    print("El sistema ya tiene datos de ejemplo cargados. Pruébalo.\n")

    # Menú principal en bucle hasta que el usuario salga
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            mostrar_estadisticas(restaurante)
        elif opcion == "8":
            print("\n¡Gracias por usar el Sistema de Restaurante!")
            print("Hasta luego.\n")
            break
        else:
            print("✗ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

