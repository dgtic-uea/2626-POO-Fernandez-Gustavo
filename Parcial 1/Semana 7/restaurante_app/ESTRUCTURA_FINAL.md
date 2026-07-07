# ESTRUCTURA FINAL DEL PROYECTO - Semana 7

## Resumen Ejecutivo

El proyecto **restaurante_app** de la Semana 7 es un sistema completo de gestión de restaurante que demuestra:

1. **Programación Orientada a Objetos (POO)**
2. **Constructores tradicionales** con validación
3. **Decoradores @property y @setter** para encapsulación
4. **Decorador @dataclass** para clases de datos
5. **Arquitectura modular por capas**
6. **Menú interactivo** en consola
7. **Flujo completo**: input → objeto → almacenamiento → consulta

---

## Estructura de Carpetas

```
/Users/gfernandez/PycharmProjects/2626-POO-Fernandez-Gustavo/
  └── Parcial 1/
      └── Semana 7/
          └── restaurante_app/
              ├── modelos/
              │   ├── __init__.py          (Exporta modelos)
              │   ├── producto.py          (Clase Producto)
              │   └── cliente.py           (Clase Cliente)
              ├── servicios/
              │   ├── __init__.py          (Exporta servicios)
              │   └── restaurante.py       (Clase Restaurante)
              ├── main.py                  (Punto de entrada)
              ├── README.md                (Documentación)
              ├── GUIA_DIDACTICA.md        (Guía detallada)
              └── EJEMPLO_INTERACTIVO.md   (Ejemplos paso a paso)
```

---

## Descripción de Cada Archivo

### 📁 modelos/__init__.py
```python
"""Módulo modelos: contiene las clases de datos principales."""
from .producto import Producto
from .cliente import Cliente

__all__ = ['Producto', 'Cliente']
```
- **Propósito**: Exportar las clases modelo
- **Facilita**: `from modelos import Producto, Cliente`

---

### 📄 modelos/producto.py
```python
class Producto:
    # Constructor tradicional
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        # ...
    
    # Decorador @property para lectura
    @property
    def nombre(self):
        return self._nombre
    
    # Decorador @setter para escritura con validación
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("...")
        self._nombre = valor.strip()
    
    # Método de información
    def mostrar_informacion(self):
        return f"Producto: {self.nombre}..."
```

**Características**:
- Constructor `__init__()` tradicional
- Validación de datos mediante setters
- Encapsulación con propiedades privadas
- 4 atributos: nombre, categoría, precio, disponible
- Validaciones:
  - Nombre no vacío
  - Categoría no vacía
  - Precio > 0

---

### 📄 modelos/cliente.py
```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
    
    def mostrar_informacion(self):
        return f"Cliente ID: {self.id_cliente}..."
```

**Características**:
- Decorador `@dataclass` para simplificar
- Constructor automático generado
- 3 atributos: id_cliente, nombre, correo
- Método `mostrar_informacion()`

**Comparación con Producto**:
- Producto: Control completo, validaciones complejas
- Cliente: Código limpio, menos boilerplate

---

### 📁 servicios/__init__.py
```python
"""Módulo servicios: contiene clases de servicio."""
from .restaurante import Restaurante

__all__ = ['Restaurante']
```
- **Propósito**: Exportar la clase servicio
- **Facilita**: `from servicios import Restaurante`

---

### 📄 servicios/restaurante.py
```python
class Restaurante:
    def __init__(self, nombre="Mi Restaurante"):
        self._productos = []  # Lista privada
        self._clientes = []   # Lista privada
    
    # Métodos para Productos
    def registrar_producto(self, producto):
        # Valida duplicados y registra
        
    def listar_productos(self):
        # Retorna copia de lista
        
    def buscar_producto(self, criterio, tipo_busqueda="nombre"):
        # Busca y retorna resultados
    
    # Métodos para Clientes
    def registrar_cliente(self, cliente):
        # Valida IDs únicos y registra
        
    def listar_clientes(self):
        # Retorna copia de lista
        
    def buscar_cliente(self, criterio, tipo_busqueda="nombre"):
        # Busca y retorna resultados
    
    # Métodos de información
    def obtener_estadisticas(self):
        # Retorna diccionario con estadísticas
```

**Responsabilidades**:
- Administrar lista de productos
- Administrar lista de clientes
- Validar duplicados
- Permitir búsquedas flexibles
- Generar estadísticas

---

### 📄 main.py
```python
"""Punto de entrada del sistema."""
from servicios import Restaurante
from modelos import Producto, Cliente

def main():
    # Crear instancia de Restaurante
    restaurante = Restaurante("Restaurante El Buen Sabor")
    
    # Cargar datos de ejemplo
    cargar_datos_ejemplo(restaurante)
    
    # Menú interactivo en bucle
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        # ... más opciones
        elif opcion == "8":
            break
```

**Flujo**:
1. Crea instancia de servicio
2. Carga datos de ejemplo
3. Muestra menú interactivo
4. Captura opciones del usuario
5. Llama funciones correspondientes
6. Se mantiene en bucle

---

## Flujo Interactivo Completo

```
USUARIO              →  input()
                    ↓
CONSOLA             ←  Muestra menú
                    ↓
USUARIO             →  Selecciona opción 1 (Registrar)
                    ↓
CONSOLA             ←  Solicita datos
                    ↓
USUARIO             →  Ingresa: nombre, categoría, precio
                    ↓
CONSTRUCTOR         →  Producto.__init__(...)
                    ↓
VALIDACIÓN          →  @setter valida cada atributo
                    ↓
OBJETO              →  Producto creado exitosamente
                    ↓
SERVICIO            →  restaurante.registrar_producto(producto)
                    ↓
ALMACENAMIENTO      →  Agregado a _productos[]
                    ↓
CONSOLA             ←  "✓ Producto registrado"
                    ↓
USUARIO             →  Selecciona opción 2 (Listar)
                    ↓
SERVICIO            →  restaurante.listar_productos()
                    ↓
CONSULTA            →  Recupera de _productos[]
                    ↓
VISUALIZACIÓN       →  Para cada producto: mostrar_informacion()
                    ↓
CONSOLA             ←  Muestra lista de productos
                    ↓
USUARIO             →  Ve sus datos + datos de ejemplo
```

---

## Requisitos Cumplidos

### ✓ Estructura Modular
- [x] Carpeta modelos/ con __init__.py
- [x] Carpeta servicios/ con __init__.py
- [x] Archivo main.py como punto de entrada
- [x] Importaciones correctas entre módulos

### ✓ Clase Producto
- [x] Implementada en modelos/producto.py
- [x] Constructor tradicional __init__()
- [x] Atributos: nombre, categoría, precio, disponible
- [x] Decorador @property para lectura
- [x] Decorador @setter para escritura
- [x] Validación: nombre no vacío
- [x] Validación: categoría no vacía
- [x] Validación: precio > 0
- [x] Método mostrar_informacion()

### ✓ Clase Cliente
- [x] Implementada en modelos/cliente.py
- [x] Decorador @dataclass
- [x] Atributos: id_cliente, nombre, correo
- [x] Método mostrar_informacion()

### ✓ Clase Restaurante
- [x] Implementada en servicios/restaurante.py
- [x] Lista privada de productos
- [x] Lista privada de clientes
- [x] Método registrar_producto()
- [x] Método listar_productos()
- [x] Método buscar_producto()
- [x] Método registrar_cliente()
- [x] Método listar_clientes()
- [x] Método buscar_cliente()
- [x] Validación de duplicados
- [x] Método obtener_estadisticas()

### ✓ Menú Interactivo
- [x] Implementado en main.py
- [x] Muestra opciones 1-8
- [x] Registrar producto
- [x] Listar productos
- [x] Buscar producto
- [x] Registrar cliente
- [x] Listar clientes
- [x] Buscar cliente
- [x] Ver estadísticas
- [x] Opción salir
- [x] Bucle mientras no salga

### ✓ Características Adicionales
- [x] Datos de ejemplo precargados
- [x] Flujo input → constructor → objeto → almacenamiento → consulta
- [x] Validaciones y manejo de errores
- [x] Encapsulación con atributos privados
- [x] Búsquedas case-insensitive
- [x] Comentarios descriptivos
- [x] Documentación completa
- [x] Ejemplos didácticos

---

## Datos de Ejemplo Precargados

### Productos (8):
1. Hamburguesa Clásica - platillo - $12.50
2. Pizza Margherita - platillo - $14.99
3. Pasta Alfredo - platillo - $13.75
4. Refresco Cola - bebida - $2.50
5. Jugo Natural - bebida - $4.25
6. Agua Mineral - bebida - $1.50
7. Tiramisú - postre - $6.50
8. Helado de Vainilla - postre - $4.00

### Clientes (5):
1. C001 - Juan Pérez - juan.perez@email.com
2. C002 - María García - maria.garcia@email.com
3. C003 - Carlos López - carlos.lopez@email.com
4. C004 - Ana Martínez - ana.martinez@email.com
5. C005 - Roberto Sánchez - roberto.sanchez@email.com

---

## Conceptos Demostrados

### 1. Encapsulación
```python
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, valor):
    # Validación aquí
```

### 2. Herencia de Excepciones
```python
try:
    producto = Producto(nombre, categoría, precio)
except ValueError as e:
    print(f"Error: {e}")
```

### 3. Uso de Decoradores
```python
@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
```

### 4. Manejo de Listas Privadas
```python
self._productos = []  # Privada
self._clientes = []   # Privada

def listar_productos(self):
    return self._productos.copy()  # Copia segura
```

### 5. Búsquedas Flexibles
```python
def buscar_producto(self, criterio, tipo_busqueda="nombre"):
    criterio_lower = criterio.lower()
    if tipo_busqueda == "nombre":
        return [p for p in self._productos 
                if criterio_lower in p.nombre.lower()]
```

---

## Cómo Ejecutar

### Opción 1: Terminal
```bash
cd "/Users/gfernandez/PycharmProjects/2626-POO-Fernandez-Gustavo/Parcial 1/Semana 7/restaurante_app"
python3 main.py
```

### Opción 2: PyCharm
1. Abre PyCharm
2. Navega a Semana 7/restaurante_app
3. Click derecho en main.py
4. Selecciona "Run 'main'"

---

## Documentación Incluida

1. **README.md** - Descripción general del proyecto
2. **GUIA_DIDACTICA.md** - Explicación detallada de conceptos
3. **EJEMPLO_INTERACTIVO.md** - Sesión completa de uso
4. **Comentarios en código** - Explicación de cada sección

---

## Validaciones Implementadas

| Elemento | Validación | Error |
|----------|-----------|--------|
| Producto.nombre | No vacío | "El nombre del producto no puede estar vacío." |
| Producto.categoria | No vacía | "La categoría del producto no puede estar vacía." |
| Producto.precio | > 0 | "El precio debe ser mayor que cero." |
| Productos | Sin duplicados | "El producto '[nombre]' ya existe." |
| Cliente.id | Único | "El cliente con ID '[id]' ya existe." |

---

## Estadísticas Generadas

```python
{
    "total_productos": 8,
    "productos_disponibles": 8,
    "precio_promedio": 7.50,
    "total_clientes": 5
}
```

---

## Estructura de Importaciones

```
main.py
  ├─ from servicios import Restaurante
  │   └─ servicios/__init__.py
  │       └─ from .restaurante import Restaurante
  │           └─ from modelos import Producto, Cliente
  │               └─ modelos/__init__.py
  │                   ├─ from .producto import Producto
  │                   └─ from .cliente import Cliente
  │
  └─ from modelos import Producto, Cliente
      └─ modelos/__init__.py (ya importado arriba)
```

---

## Conclusión

Este proyecto es una demostración completa de **Programación Orientada a Objetos en Python** con:

✓ Diseño modular y escalable
✓ Encapsulación mediante @property y @setter
✓ Simplificación mediante @dataclass
✓ Interfaz interactiva intuitiva
✓ Datos de ejemplo para demostración
✓ Documentación completa y didáctica
✓ Manejo robusto de errores y validaciones

**Está listo para ser presentado como solución de la Semana 7.**

