# EJEMPLO INTERACTIVO PASO A PASO

## Demostración Completa del Sistema

Este documento simula una sesión completa de uso del sistema, mostrando exactamente qué verás en consola.

---

## SESIÓN 1: Explorar Datos de Ejemplo

### Paso 1: Ejecutar el programa

```bash
$ python3 main.py
```

### Paso 2: Ver el mensaje de bienvenida

```
⚙ Cargando datos de ejemplo...

✓ Se han cargado exitosamente:
  - 8 productos de ejemplo
  - 5 clientes de ejemplo

Prueba las opciones del menú para ver cómo interactúa el sistema.

¡Bienvenido al Sistema de Restaurante!
El sistema ya tiene datos de ejemplo cargados. Pruébalo.
```

### Paso 3: Ver el menú principal

```
================================================
            SISTEMA DE RESTAURANTE
================================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Ver estadísticas
8. Salir
================================================
Seleccione una opción (1-8): 
```

---

## SESIÓN 2: Registrar un Nuevo Producto

### Seleccionar opción 1

```
Seleccione una opción (1-8): 1

--- REGISTRAR NUEVO PRODUCTO ---
Nombre del producto: Sopa de Verduras
Categoría (ej: bebida, platillo, postre): platillo
Precio ($): 8.75
¿Disponible? (s/n, default: s): s

✓ Producto 'Sopa de Verduras' registrado exitosamente.
```

### ¿Qué pasó internamente?

1. El usuario ingresó: "Sopa de Verduras", "platillo", "8.75"
2. Se ejecutó: `producto = Producto("Sopa de Verduras", "platillo", "8.75", True)`
3. El constructor validó:
   - ✓ Nombre no vacío
   - ✓ Categoría no vacía
   - ✓ Precio es número > 0
4. Se almacenó: `restaurante.registrar_producto(producto)`
5. Ahora está en `restaurante._productos`

---

## SESIÓN 3: Listar Productos (incluyendo el nuevo)

### Seleccionar opción 2

```
Seleccione una opción (1-8): 2

--- LISTADO DE PRODUCTOS ---

[1] Producto: Hamburguesa Clásica
  Categoría: platillo
  Precio: $12.50
  Estado: ✓ Disponible

[2] Producto: Pizza Margherita
  Categoría: platillo
  Precio: $14.99
  Estado: ✓ Disponible

[3] Producto: Pasta Alfredo
  Categoría: platillo
  Precio: $13.75
  Estado: ✓ Disponible

[4] Producto: Refresco Cola
  Categoría: bebida
  Precio: $2.50
  Estado: ✓ Disponible

[5] Producto: Jugo Natural
  Categoría: bebida
  Precio: $4.25
  Estado: ✓ Disponible

[6] Producto: Agua Mineral
  Categoría: bebida
  Precio: $1.50
  Estado: ✓ Disponible

[7] Producto: Tiramisú
  Categoría: postre
  Precio: $6.50
  Estado: ✓ Disponible

[8] Producto: Helado de Vainilla
  Categoría: postre
  Precio: $4.00
  Estado: ✓ Disponible

[9] Producto: Sopa de Verduras
  Categoría: platillo
  Precio: $8.75
  Estado: ✓ Disponible
```

### Observación
- ¡El nuevo producto aparece en la lista!
- Se creó como un objeto `Producto` con todos sus atributos

---

## SESIÓN 4: Buscar un Producto por Categoría

### Seleccionar opción 3

```
Seleccione una opción (1-8): 3

--- BUSCAR PRODUCTO ---
1. Por nombre
2. Por categoría
3. Búsqueda general
Seleccione tipo de búsqueda (1-3): 2
Ingrese criterio de búsqueda: bebida

✓ Se encontraron 3 producto(s):

[1] Producto: Refresco Cola
  Categoría: bebida
  Precio: $2.50
  Estado: ✓ Disponible

[2] Producto: Jugo Natural
  Categoría: bebida
  Precio: $4.25
  Estado: ✓ Disponible

[3] Producto: Agua Mineral
  Categoría: bebida
  Precio: $1.50
  Estado: ✓ Disponible
```

### ¿Qué pasó?
1. Se buscó en `restaurante.buscar_producto("bebida", "categoria")`
2. Se filtró la lista `_productos` por coincidencia en categoría
3. Se mostró cada `producto.mostrar_informacion()`

---

## SESIÓN 5: Intentar Registrar Producto Inválido

### Seleccionar opción 1

```
Seleccione una opción (1-8): 1

--- REGISTRAR NUEVO PRODUCTO ---
Nombre del producto: 
Categoría (ej: bebida, platillo, postre): bebida
Precio ($): 5.00
¿Disponible? (s/n, default: s): s

✗ Error al registrar producto: El nombre del producto no puede estar vacío.
```

### ¿Qué pasó?
1. El usuario dejó el nombre vacío
2. El setter de `@nombre.setter` validó
3. Lanzó `ValueError` porque el nombre está vacío
4. Se capturó el error y se mostró el mensaje

---

## SESIÓN 6: Intentar Precio Inválido

### Seleccionar opción 1

```
Seleccione una opción (1-8): 1

--- REGISTRAR NUEVO PRODUCTO ---
Nombre del producto: Café
Categoría (ej: bebida, platillo, postre): bebida
Precio ($): -3.50
¿Disponible? (s/n, default: s): s

✗ Error al registrar producto: El precio debe ser mayor que cero.
```

### ¿Qué pasó?
1. El usuario ingresó precio negativo
2. El setter de `@precio.setter` validó
3. Lanzó `ValueError` porque precio <= 0
4. El objeto NUNCA se creó

---

## SESIÓN 7: Registrar un Nuevo Cliente

### Seleccionar opción 4

```
Seleccione una opción (1-8): 4

--- REGISTRAR NUEVO CLIENTE ---
ID del cliente (ej: C001): C006
Nombre completo: Alejandra López
Correo electrónico: alejandra.lopez@email.com

✓ Cliente 'Alejandra López' registrado exitosamente.
```

### ¿Qué pasó internamente?
1. Se creó: `cliente = Cliente("C006", "Alejandra López", "alejandra.lopez@email.com")`
2. El constructor (generado por `@dataclass`) ejecutó automáticamente
3. Se almacenó: `restaurante.registrar_cliente(cliente)`
4. Ahora está en `restaurante._clientes`

---

## SESIÓN 8: Listar Clientes (incluyendo el nuevo)

### Seleccionar opción 5

```
Seleccione una opción (1-8): 5

--- LISTADO DE CLIENTES ---

[1] Cliente ID: C001
  Nombre: Juan Pérez
  Correo: juan.perez@email.com

[2] Cliente ID: C002
  Nombre: María García
  Correo: maria.garcia@email.com

[3] Cliente ID: C003
  Nombre: Carlos López
  Correo: carlos.lopez@email.com

[4] Cliente ID: C004
  Nombre: Ana Martínez
  Correo: ana.martinez@email.com

[5] Cliente ID: C005
  Nombre: Roberto Sánchez
  Correo: roberto.sanchez@email.com

[6] Cliente ID: C006
  Nombre: Alejandra López
  Correo: alejandra.lopez@email.com
```

### Observación
- El nuevo cliente aparece en la lista
- Se creó usando `@dataclass` (más simple que `Producto`)

---

## SESIÓN 9: Buscar Cliente por Correo

### Seleccionar opción 6

```
Seleccione una opción (1-8): 6

--- BUSCAR CLIENTE ---
1. Por nombre
2. Por ID
3. Por correo
4. Búsqueda general
Seleccione tipo de búsqueda (1-4): 3
Ingrese criterio de búsqueda: maria

✓ Se encontraron 1 cliente(s):

[1] Cliente ID: C002
  Nombre: María García
  Correo: maria.garcia@email.com
```

### ¿Qué pasó?
1. Se buscó en `restaurante.buscar_cliente("maria", "correo")`
2. Filtró por "maria" en el email (case-insensitive)
3. Encontró a María García

---

## SESIÓN 10: Ver Estadísticas

### Seleccionar opción 7

```
Seleccione una opción (1-8): 7

--- ESTADÍSTICAS DEL RESTAURANTE ---
Total de productos: 9
Productos disponibles: 9
Precio promedio: $7.80
Total de clientes: 6
```

### ¿Qué pasó?
1. Se ejecutó `restaurante.obtener_estadisticas()`
2. Contó: 9 productos (los 8 iniciales + 1 nuevo)
3. Contó: 6 clientes (los 5 iniciales + 1 nuevo)
4. Calculó promedio de precios

---

## SESIÓN 11: Intentar Registrar Cliente con ID Duplicado

### Seleccionar opción 4

```
Seleccione una opción (1-8): 4

--- REGISTRAR NUEVO CLIENTE ---
ID del cliente (ej: C001): C001
Nombre completo: Nuevo Cliente
Correo electrónico: nuevo@email.com

✗ Error al registrar cliente: El cliente con ID 'C001' ya existe.
```

### ¿Qué pasó?
1. El usuario intentó crear cliente con ID "C001" (ya existe)
2. `registrar_cliente()` verificó duplicados
3. Lanzó `ValueError`
4. El cliente NO fue registrado

---

## SESIÓN 12: Salir del Programa

### Seleccionar opción 8

```
Seleccione una opción (1-8): 8

¡Gracias por usar el Sistema de Restaurante!
Hasta luego.

$ 
```

---

## Resumen de Conceptos Demostrables

### 1. Constructor Tradicional con Validación ✓
```python
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre  # ← Usa setter que valida
```

### 2. Decorador @property ✓
```python
@property
def nombre(self):
    return self._nombre
```

### 3. Decorador @setter ✓
```python
@nombre.setter
def nombre(self, valor):
    if not valor or not valor.strip():
        raise ValueError("...")
    self._nombre = valor.strip()
```

### 4. Decorador @dataclass ✓
```python
@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
```

### 5. Clase de Servicio (Arquitectura) ✓
```python
class Restaurante:
    def __init__(self):
        self._productos = []
        self._clientes = []
```

### 6. Menú Interactivo ✓
```python
while True:
    # mostrar menú
    # captar opción
    # ejecutar acción
    # ¿salir?
```

### 7. Flujo Completo: input → objeto → almacenamiento → consulta ✓

---

## Pruebas Sugeridas

Intenta estas acciones:

1. **Registra un producto con nombre vacío** → ¿Qué error ves?
2. **Registra un producto con precio negativo** → ¿Se crea el objeto?
3. **Busca "platillo" en categoría** → ¿Cuántos encuentra?
4. **Registra 2 clientes con mismo ID** → ¿Qué pasa el segundo?
5. **Busca por nombre parcial** → ¿Es case-sensitive?

---

## Estructura de Archivos Verificada

```
restaurante_app/
├── modelos/
│   ├── __init__.py              ✓ Importa Producto, Cliente
│   ├── producto.py              ✓ Clase Producto con @property/@setter
│   └── cliente.py               ✓ Clase Cliente con @dataclass
├── servicios/
│   ├── __init__.py              ✓ Importa Restaurante
│   └── restaurante.py           ✓ Clase servicio con lógica
└── main.py                      ✓ Menú interactivo
```

---

## Conclusión

Este sistema demuestra completamente:
- ✓ POO con encapsulación
- ✓ Constructores y validación
- ✓ Propiedades y setters
- ✓ Dataclasses
- ✓ Arquitectura modular
- ✓ Gestión de excepciones
- ✓ Entrada/salida interactiva
- ✓ Almacenamiento en memoria

¡Estás listo para comprender sistemas más complejos!

