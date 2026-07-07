# GUÍA DE USO - Sistema de Restaurante

## ¿Cómo entender este sistema?

Este proyecto demuestra los **4 pasos fundamentales de la POO aplicada**:

### Paso 1: Captura de Datos (input)
El usuario ingresa datos por consola

### Paso 2: Creación de Objeto (constructor)
Los datos se transforman en objetos mediante el constructor (`__init__` o `@dataclass`)

### Paso 3: Almacenamiento (registro)
El objeto se almacena en la clase de servicio (`Restaurante`)

### Paso 4: Consulta (búsqueda/listado)
El objeto se recupera y visualiza

---

## Ejemplo Paso a Paso

### Ejecutar el programa:
```bash
cd /Users/gfernandez/PycharmProjects/2626-POO-Fernandez-Gustavo/Parcial\ 1/Semana\ 7/restaurante_app
python3 main.py
```

---

## Caso de Uso 1: Registrar un Nuevo Producto

### Flujo Interactivo:

```
Seleccione una opción (1-8): 1

--- REGISTRAR NUEVO PRODUCTO ---
Nombre del producto: Ensalada César
Categoría (ej: bebida, platillo, postre): platillo
Precio ($): 10.99
¿Disponible? (s/n, default: s): s

✓ Producto 'Ensalada César' registrado exitosamente.
```

### ¿Qué sucede internamente?

1. **El usuario ingresa datos**: "Ensalada César", "platillo", "10.99"

2. **Se crea un objeto Producto**:
   ```python
   # En main.py, función registrar_producto():
   producto = Producto(nombre, categoria, precio, disponible_bool)
   ```

3. **El constructor __init__ valida**:
   ```python
   # En modelos/producto.py:
   @nombre.setter
   def nombre(self, valor):
       if not valor or not valor.strip():
           raise ValueError("El nombre del producto no puede estar vacío.")
       self._nombre = valor.strip()
   ```

4. **El objeto se registra en Restaurante**:
   ```python
   restaurante.registrar_producto(producto)
   ```

5. **Se almacena en una lista privada**:
   ```python
   # En servicios/restaurante.py:
   self._productos.append(producto)
   ```

---

## Caso de Uso 2: Listar Productos

### Flujo Interactivo:

```
Seleccione una opción (1-8): 2

--- LISTADO DE PRODUCTOS ---

[1] Producto: Hamburguesa Clásica
  Categoría: platillo
  Precio: $12.50
  Estado: ✓ Disponible

[2] Producto: Ensalada César
  Categoría: platillo
  Precio: $10.99
  Estado: ✓ Disponible

... (más productos)
```

### ¿Qué sucede internamente?

```python
# En main.py:
productos = restaurante.listar_productos()

# En servicios/restaurante.py:
def listar_productos(self):
    return self._productos.copy()  # Retorna una copia de la lista

# Para cada producto, se llama:
producto.mostrar_informacion()  # Método de Producto que formatea los datos
```

---

## Caso de Uso 3: Buscar un Producto

### Flujo Interactivo:

```
Seleccione una opción (1-8): 3

--- BUSCAR PRODUCTO ---
1. Por nombre
2. Por categoría
3. Búsqueda general
Seleccione tipo de búsqueda (1-3): 1
Ingrese criterio de búsqueda: hambur

✓ Se encontraron 1 producto(s):

[1] Producto: Hamburguesa Clásica
  Categoría: platillo
  Precio: $12.50
  Estado: ✓ Disponible
```

### ¿Qué sucede internamente?

```python
# En main.py:
resultados = restaurante.buscar_producto("hambur", "nombre")

# En servicios/restaurante.py:
def buscar_producto(self, criterio, tipo_busqueda="nombre"):
    criterio_lower = criterio.lower()
    resultados = [p for p in self._productos 
                 if criterio_lower in p.nombre.lower()]
    return resultados  # Retorna lista de objetos Producto encontrados
```

---

## Caso de Uso 4: Registrar un Cliente

### Flujo Interactivo:

```
Seleccione una opción (1-8): 4

--- REGISTRAR NUEVO CLIENTE ---
ID del cliente (ej: C001): C006
Nombre completo: Fernando Ortiz
Correo electrónico: fernando.ortiz@email.com

✓ Cliente 'Fernando Ortiz' registrado exitosamente.
```

### ¿Qué sucede internamente?

1. **Se crea un objeto Cliente usando @dataclass**:
   ```python
   # En main.py:
   cliente = Cliente(id_cliente, nombre, correo)
   ```

2. **El constructor (generado por @dataclass) es simple**:
   ```python
   # En modelos/cliente.py:
   @dataclass
   class Cliente:
       id_cliente: str
       nombre: str
       correo: str
   ```

3. **El objeto se registra**:
   ```python
   restaurante.registrar_cliente(cliente)
   ```

**Nota**: A diferencia de `Producto`, `Cliente` usa `@dataclass` que **genera automáticamente** el constructor, sin necesidad de escribir `__init__()` manualmente.

---

## Diferencia: @dataclass vs Constructor Tradicional

### Producto (Constructor Tradicional):
```python
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre  # Usa setter para validar
        self.categoria = categoria
        self.precio = precio
        self._disponible = disponible
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("...")
        self._nombre = valor.strip()
```

**Ventaja**: Control total, validaciones complejas

---

### Cliente (@dataclass):
```python
@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
```

**Ventaja**: Código más limpio, menos boilerplate

---

## Validaciones Demostradas

### 1. Validación en Producto.nombre
```
Nombre del producto: 
✗ Error al registrar producto: El nombre del producto no puede estar vacío.
```

### 2. Validación en Producto.precio
```
Precio ($): -5
✗ Error al registrar producto: El precio debe ser mayor que cero.
```

### 3. Validación de duplicados
```
✗ Error al registrar producto: El producto 'Hamburguesa Clásica' ya existe en el registro.
```

### 4. Validación de ID único en Cliente
```
✗ Error al registrar cliente: El cliente con ID 'C001' ya existe.
```

---

## Estadísticas del Sistema

### Flujo Interactivo:

```
Seleccione una opción (1-8): 7

--- ESTADÍSTICAS DEL RESTAURANTE ---
Total de productos: 8
Productos disponibles: 8
Precio promedio: $7.50
Total de clientes: 5
```

### ¿Qué sucede internamente?

```python
# En main.py:
stats = restaurante.obtener_estadisticas()

# En servicios/restaurante.py:
def obtener_estadisticas(self):
    productos_disponibles = sum(1 for p in self._productos if p.disponible)
    precio_promedio = sum(p.precio for p in self._productos) / len(self._productos)
    
    return {
        "total_productos": len(self._productos),
        "productos_disponibles": productos_disponibles,
        "precio_promedio": precio_promedio,
        "total_clientes": len(self._clientes)
    }
```

---

## Flujo General del Programa

```
INICIO
  │
  ├─→ Cargar datos de ejemplo (cargar_datos_ejemplo)
  │
  ├─→ Mostrar menú interactivo
  │
  ├─→ Captar opción del usuario
  │
  ├─→ Ejecutar acción:
  │   │
  │   ├─ Opción 1: input() → constructor → almacenar → confirmación
  │   ├─ Opción 2: listar → recuperar → mostrar
  │   ├─ Opción 3: buscar → filtrar → mostrar
  │   ├─ Opción 4-6: igual que 1-3 pero con clientes
  │   ├─ Opción 7: estadísticas
  │   └─ Opción 8: salir
  │
  ├─→ ¿Salir?
  │   NO → volver a mostrar menú
  │   SÍ → FIN
  │
FIN
```

---

## Requisitos Cumplidos

✓ **Constructor tradicional** en Producto (`__init__`)
✓ **@property y @setter** en Producto
✓ **@dataclass** en Cliente
✓ **Arquitectura modular** (modelos, servicios, main)
✓ **Menú interactivo** en consola
✓ **Datos NO quemados** en código (cargados en función)
✓ **Validaciones** en constructores y setters
✓ **Encapsulación** con atributos privados
✓ **Métodos de búsqueda** flexibles
✓ **Documentación completa** en código

---

## Notas Importantes

- El programa carga **datos de ejemplo automáticamente** para demostración
- Puedes **agregar más** productos y clientes interactivamente
- Las búsquedas son **case-insensitive** (insensibles a mayúsculas)
- Los objetos se almacenan en **listas privadas** de Restaurante
- El programa se mantiene en **bucle infinito** hasta seleccionar "Salir"

---

## Para Mejorar tu Comprensión

1. **Modifica el precio de un producto**: ¿Qué validación se ejecuta?
2. **Intenta registrar producto con nombre vacío**: ¿Qué error ves?
3. **Busca un producto por categoría**: ¿Cómo filtra la lista?
4. **Abre modelos/producto.py**: ¿Ves cómo @property controla el acceso?
5. **Abre modelos/cliente.py**: ¿Por qué es más corto que Producto?

