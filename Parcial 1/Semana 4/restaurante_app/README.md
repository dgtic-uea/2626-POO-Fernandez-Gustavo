# 🍽️ Sistema de Gestión de Restaurante - POO en Python

## Descripción General

Este proyecto implementa un **sistema básico de gestión de restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema demuestra principios de organización modular, separación de responsabilidades y comunicación entre archivos mediante importaciones.

El objetivo educativo es comprender cómo estructurar un proyecto Python en módulos, organizar clases con responsabilidades específicas, e implementar relaciones entre entidades del sistema.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase Producto
│   └── cliente.py       # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase Restaurante (servicio principal)
└── main.py              # Punto de entrada del programa
```

### Organización Modular

- **`modelos/`**: Contiene las clases que representan las entidades del negocio (Producto, Cliente)
- **`servicios/`**: Contiene la clase principal que gestiona las operaciones del sistema (Restaurante)
- **`main.py`**: Ejecutable principal que demuestra el uso del sistema

---

## Clases Implementadas

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un item disponible en el menú del restaurante.

**Atributos:**
- `id`: Identificador único (generado automáticamente)
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve
- `precio`: Precio en moneda local
- `categoria`: Categoría (Entrada, Plato Principal, Postre, Bebida)
- `disponible`: Estado de disponibilidad

**Métodos principales:**
- `__init__()`: Constructor para inicializar un nuevo producto
- `cambiar_disponibilidad()`: Modifica el estado de disponibilidad
- `obtener_info()`: Retorna información del producto en formato diccionario
- `__str__()`: Representación legible del producto

---

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa a una persona que realiza pedidos en el restaurante.

**Atributos:**
- `id`: Identificador único (generado automáticamente)
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `pedidos`: Lista de pedidos realizados

**Métodos principales:**
- `__init__()`: Constructor para registrar un nuevo cliente
- `agregar_pedido()`: Registra un pedido en el historial del cliente
- `obtener_cantidad_pedidos()`: Retorna el total de pedidos realizados
- `obtener_info()`: Retorna información del cliente
- `__str__()`: Representación legible del cliente

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Gestiona las operaciones principales del sistema (productos, clientes, pedidos).

**Atributos:**
- `nombre`: Nombre del restaurante
- `ubicacion`: Ubicación del restaurante
- `productos`: Lista de productos disponibles
- `clientes`: Lista de clientes registrados
- `pedidos`: Lista de pedidos realizados

**Métodos de Gestión de Productos:**
- `agregar_producto()`: Agrega nuevo producto al catálogo
- `obtener_productos_por_categoria()`: Filtra productos por categoría
- `obtener_productos_disponibles()`: Retorna productos con disponibilidad
- `listar_productos()`: Muestra el catálogo en consola

**Métodos de Gestión de Clientes:**
- `agregar_cliente()`: Registra nuevo cliente
- `buscar_cliente_por_id()`: Busca cliente por ID
- `listar_clientes()`: Muestra lista de clientes en consola

**Métodos de Gestión de Pedidos:**
- `crear_pedido()`: Crea pedido para un cliente
- `listar_pedidos()`: Muestra historial de pedidos

**Métodos de Información:**
- `mostrar_resumen()`: Resumen general del estado del restaurante

---

## Características Principales

✅ **Organización Modular**: Separación clara entre modelos y servicios  
✅ **Responsabilidades Definidas**: Cada clase tiene una responsabilidad específica  
✅ **Importaciones**: Correcta comunicación entre módulos  
✅ **Métodos Especiales**: Implementación de `__init__()` y `__str__()`  
✅ **Generación de IDs**: Variables de clase para generar identificadores únicos  
✅ **Gestión de Listas**: Almacenamiento y manipulación de colecciones  
✅ **Validaciones**: Verificación de instancias antes de operaciones  
✅ **Comentarios Documentados**: Código bien documentado con docstrings  

---

## Ejemplo de Uso

### Ejecutar el programa

```bash
cd restaurante_app
python3 main.py
```

### Output esperado

El programa demuestra:
1. Creación instancias de productos (entradas, platos, postres, bebidas)
2. Registro de clientes
3. Visualización del catálogo organizado por categoría
4. Creación de múltiples pedidos
5. Resumen general del sistema con ingresos totales
6. Análisis de datos (productos por categoría, pedidos por cliente)

---

## Conceptos POO Aplicados

### 1. **Abstracción**
Cada clase representa una entidad del negocio con sus atributos y comportamientos específicos.

### 2. **Encapsulación**
Los atributos de cada clase son gestionados por métodos específicos.

### 3. **Modularidad**
El código está dividido en módulos independientes con responsabilidades claras.

### 4. **Reutilización**
Las clases pueden ser instanciadas múltiples veces para diferentes objetos.

### 5. **Composición**
La clase Restaurante utiliza instancias de Producto y Cliente.

---

## Diferencias con el Ejemplo de Biblioteca

A diferencia del sistema de biblioteca del docente, este sistema:

| Aspecto | Biblioteca | Restaurante |
|---------|-----------|------------|
| Entidades | Libro, Autor, Biblioteca | Producto, Cliente, Restaurante |
| Operación Principal | Prestar/Devolver | Crear Pedidos |
| Atributos de Producto | Título, ISBN, Autor | Nombre, Precio, Categoría |
| Gestión | Disponibilidad de libros | Disponibilidad y precio de productos |
| Ingresos | N/A | Cálculo de ingresos por pedidos |

---

## Extensiones Posibles

Aunque el sistema es básico, puede extenderse con:

- ⭐ Clase `Pedido` independiente con detalles adicionales
- ⭐ Persistencia en base de datos (SQLite, PostgreSQL)
- ⭐ Cálculo de impuestos y promociones
- ⭐ Sistema de calificaciones de clientes
- ⭐ Interfaz gráfica (Tkinter, PyQt)
- ⭐ API REST (Flask, Django)

---

## Requisitos Técnicos

- **Python**: 3.7 o superior
- **Librerías**: Ninguna dependencia externa requerida (solo librerías estándar)

---

## Autor

Proyecto desarrollado como actividad de **Programación Orientada a Objetos** - Semana 3, Parcial 2

---

## Licencia

Este proyecto es de uso educativo.

