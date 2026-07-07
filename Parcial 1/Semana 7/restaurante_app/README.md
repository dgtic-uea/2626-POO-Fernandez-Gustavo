# Sistema de Restaurante - Semana 7

## Descripción del Proyecto

Este es un sistema de gestión de restaurante desarrollado en Python utilizando **Programación Orientada a Objetos (POO)** con los siguientes principios:

- **Constructores tradicionales** (`__init__`)
- **Decoradores `@property` y `@setter`** para encapsulación
- **Decorador `@dataclass`** para simplificar clases de datos
- **Arquitectura modular por capas** (modelos, servicios)
- **Menú interactivo** en consola

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py          # Exporta Producto y Cliente
│   ├── producto.py          # Clase Producto (constructor + @property/@setter)
│   └── cliente.py           # Clase Cliente (@dataclass)
├── servicios/
│   ├── __init__.py          # Exporta Restaurante
│   └── restaurante.py       # Clase Restaurante (servicio principal)
└── main.py                  # Punto de entrada (menú interactivo)
```

## Conceptos Implementados

### 1. **Clase Producto** (`modelos/producto.py`)
- Constructor tradicional `__init__()` con validación
- Atributos privados (`_nombre`, `_categoria`, `_precio`, `_disponible`)
- Decoradores `@property` para lectura controlada
- Decoradores `@setter` para escritura con validaciones:
  - Nombre no vacío
  - Categoría no vacía
  - Precio mayor que cero
- Método `mostrar_informacion()` para visualización legible

### 2. **Clase Cliente** (`modelos/cliente.py`)
- Implementada con `@dataclass` para reducir código boilerplate
- Atributos: `id_cliente`, `nombre`, `correo`
- Genera automáticamente `__init__`, `__repr__`, `__eq__`
- Método `mostrar_informacion()` para visualización

### 3. **Clase Restaurante** (`servicios/restaurante.py`)
- Administra listas privadas de productos y clientes
- Métodos para productos:
  - `registrar_producto()`: agrega productos validando duplicados
  - `listar_productos()`: retorna copia de lista
  - `buscar_producto()`: busca por nombre, categoría o ambos
- Métodos para clientes:
  - `registrar_cliente()`: agrega clientes validando IDs únicos
  - `listar_clientes()`: retorna copia de lista
  - `buscar_cliente()`: busca por nombre, ID, correo o todos
- Método `obtener_estadisticas()`: información agregada

### 4. **Menú Interactivo** (`main.py`)
Flujo demostrativo:
```
input() del usuario
    ↓
constructor del modelo (valida datos)
    ↓
creación del objeto
    ↓
registro en Restaurante (servicio)
    ↓
listado o búsqueda del registro
```

## Cómo Ejecutar

### Desde la terminal (macOS/Linux):

```bash
# Navegar a la carpeta del proyecto
cd /Users/gfernandez/PycharmProjects/2626-POO-Fernandez-Gustavo/Parcial\ 1/Semana\ 7

# Ejecutar el programa
python main.py
```

### Desde PyCharm:
1. Abre el proyecto en PyCharm
2. Navega a la carpeta `Semana 7`
3. Click derecho en `main.py` → "Run 'main'"

## Datos de Ejemplo

El sistema carga automáticamente **datos de ejemplo** al iniciarse:

**Productos:**
- Hamburguesa Clásica ($12.50)
- Pizza Margherita ($14.99)
- Pasta Alfredo ($13.75)
- Refresco Cola ($2.50)
- Jugo Natural ($4.25)
- Agua Mineral ($1.50)
- Tiramisú ($6.50)
- Helado de Vainilla ($4.00)

**Clientes:**
- C001 - Juan Pérez
- C002 - María García
- C003 - Carlos López
- C004 - Ana Martínez
- C005 - Roberto Sánchez

## Opciones del Menú

```
1. Registrar producto      → Captura datos y crea objeto Producto
2. Listar productos        → Muestra todos los productos
3. Buscar producto         → Busca por nombre, categoría o general
4. Registrar cliente       → Captura datos y crea objeto Cliente
5. Listar clientes         → Muestra todos los clientes
6. Buscar cliente          → Busca por nombre, ID, correo o general
7. Ver estadísticas        → Muestra información agregada
8. Salir                   → Termina el programa
```

## Validaciones Implementadas

### Producto
- **Nombre**: No vacío
- **Categoría**: No vacía
- **Precio**: Número válido > 0
- **Duplicados**: No permite productos con mismo nombre

### Cliente
- **ID Cliente**: Único (no permite duplicados)
- **Nombre y Correo**: Requeridos

## Características Didácticas

✓ **Datos precargados**: Demuestra inmediatamente el funcionamiento
✓ **Menú interactivo**: Facilita la comprensión del flujo
✓ **Validaciones claras**: Muestra cómo proteger objetos
✓ **Encapsulación**: Uso de `@property` y `@setter`
✓ **Comparación de enfoques**: `@dataclass` vs constructor tradicional
✓ **Arquitectura modular**: Separación clara de responsabilidades
✓ **Comentarios descriptivos**: Explica conceptos clave

## Ejemplo de Flujo Interactivo

```
¡Bienvenido al Sistema de Restaurante!

--- REGISTRAR NUEVO PRODUCTO ---
Nombre del producto: Empanadas
Categoría (ej: bebida, platillo, postre): platillo
Precio ($): 5.50
¿Disponible? (s/n, default: s): s

✓ Producto 'Empanadas' registrado exitosamente.
```

## Requisitos de Python

- Python 3.7+ (para @dataclass)
- No requiere librerías externas

## Notas Importantes

- Los objetos **NO** están quemados en el código
- Se cargan datos de ejemplo en `cargar_datos_ejemplo()`
- El usuario puede agregar más productos y clientes
- Las búsquedas son **case-insensitive**
- Los setters de Producto validan automáticamente los datos

## Autor

Desarrollado como actividad de **Programación Orientada a Objetos - Semana 7**

