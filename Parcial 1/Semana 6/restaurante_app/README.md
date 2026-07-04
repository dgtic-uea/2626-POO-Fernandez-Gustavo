# Sistema de Restaurante - Programación Orientada a Objetos

## 📋 Información del Estudiante
- **Nombre:** Gustavo Fernández
- **Asignatura:** Programación Orientada a Objetos (POO)
- **Semana:** 6
- **Parcial:** 1

---

## 📝 Descripción del Sistema

Este proyecto implementa un sistema de gestión de productos para un restaurante utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite administrar platillos y bebidas disponibles en el restaurante, aplicando principios fundamentales como:

- **Herencia**: Creación de una jerarquía de clases donde `Platillo` y `Bebida` heredan de `Producto`.
- **Encapsulación**: Protección del atributo `__precio` mediante métodos de acceso y validación.
- **Polimorfismo**: Implementación de `mostrar_informacion()` en las clases hijas con comportamientos específicos.
- **Modularidad**: Organización del código en paquetes y módulos independientes.

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del paquete modelos
│   ├── producto.py           # Clase padre Producto
│   ├── platillo.py           # Clase hija Platillo
│   └── bebida.py             # Clase hija Bebida
├── servicios/
│   ├── __init__.py           # Inicializador del paquete servicios
│   └── restaurante.py        # Clase de servicio Restaurante
└── main.py                   # Punto de entrada del programa
```

---

## 🔗 Jerarquía de Herencia

```
Producto (Clase Padre)
├── Platillo (Clase Hija)
│   └── Atributos adicionales: calorias, tipo_platillo
└── Bebida (Clase Hija)
    └── Atributos adicionales: volumen_ml, tipo_bebida
```

La relación de herencia es **lógica y coherente**: todos los productos del restaurante comparten atributos básicos (nombre, precio, disponibilidad), pero cada tipo tiene características específicas.

---

## 🔐 Encapsulación

### Atributo Encapsulado: `__precio`

El atributo `__precio` en la clase `Producto` es **privado** (con doble guion bajo) para protegerlo:

**Métodos de Acceso:**

1. **`obtener_precio()`**: Retorna el precio actual del producto.
   ```python
   precio_actual = producto.obtener_precio()
   ```

2. **`cambiar_precio(nuevo_precio)`**: Modifica el precio con validación.
   - Valida que el precio sea mayor a cero.
   - Retorna `True` si la modificación fue exitosa.
   - Retorna `False` si el precio es inválido (≤ 0).

**Ventajas de esta encapsulación:**
- Evita que se asignen valores inválidos directamente.
- Protege la integridad de los datos.
- Permite implementar lógica de validación centralizada.

---

## 🔄 Polimorfismo

El polimorfismo se demuestra mediante la **sobrescritura del método `mostrar_informacion()`** en las clases hijas.

### Método en la clase padre (`Producto`):
```python
def mostrar_informacion(self) -> None:
    estado = "✓ Disponible" if self.disponible else "✗ No disponible"
    print(f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | {estado}")
```

### Método sobrescrito en `Platillo`:
```python
def mostrar_informacion(self) -> None:
    estado = "✓ Disponible" if self.disponible else "✗ No disponible"
    print(f"🍽️  PLATILLO | {self.tipo_platillo}: {self.nombre} | "
          f"Precio: ${self.obtener_precio():.2f} | Calorías: {self.calorias} cal | {estado}")
```

### Método sobrescrito en `Bebida`:
```python
def mostrar_informacion(self) -> None:
    estado = "✓ Disponible" if self.disponible else "✗ No disponible"
    print(f"🥤 BEBIDA | {self.tipo_bebida}: {self.nombre} | "
          f"Precio: ${self.obtener_precio():.2f} | Volumen: {self.volumen_ml} ml | {estado}")
```

**Demostración en la clase `Restaurante`:**
En el método `listar_productos()`, se itera sobre una lista de productos ejecutando `mostrar_informacion()`. Cada objeto ejecuta su propia versión del método, demostrando así el polimorfismo.

---

## 📦 Descripción de las Clases

### 1. **Producto** (modelos/producto.py)
Clase padre que define los atributos comunes a todos los productos:
- `nombre`: Nombre del producto
- `__precio`: Precio encapsulado (privado)
- `disponible`: Booleano que indica disponibilidad

**Métodos principales:**
- `__init__()`: Inicializador con validación de precio
- `cambiar_precio()`: Modifica el precio con validación
- `obtener_precio()`: Retorna el precio
- `mostrar_informacion()`: Muestra información básica del producto

### 2. **Platillo** (modelos/platillo.py)
Clase hija que representa un plato del restaurante:
- Hereda: nombre, precio, disponible
- Atributos propios: `calorias`, `tipo_platillo`

**Método sobrescrito:**
- `mostrar_informacion()`: Muestra información específica del platillo

### 3. **Bebida** (modelos/bebida.py)
Clase hija que representa una bebida del restaurante:
- Hereda: nombre, precio, disponible
- Atributos propios: `volumen_ml`, `tipo_bebida`

**Método sobrescrito:**
- `mostrar_informacion()`: Muestra información específica de la bebida

### 4. **Restaurante** (servicios/restaurante.py)
Clase de servicio que administra los productos:
- `nombre`: Nombre del restaurante
- `productos`: Lista que almacena los productos registrados

**Métodos principales:**
- `agregar_producto()`: Agrega un producto a la lista
- `listar_productos()`: Muestra todos los productos (demuestra polimorfismo)
- `obtener_total_productos()`: Retorna la cantidad de productos
- `obtener_productos_disponibles()`: Retorna productos disponibles
- `cambiar_disponibilidad()`: Modifica la disponibilidad de un producto
- `mostrar_estadisticas()`: Muestra estadísticas del restaurante

---

## 🚀 Cómo Ejecutar el Programa

1. **Navegar a la carpeta del proyecto:**
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

3. **Resultado esperado:**
   El programa mostrará:
   - La creación de platillos y bebidas
   - El menú organizado del restaurante
   - Demostración de encapsulación (validación de precios)
   - Cambios de disponibilidad
   - Estadísticas del restaurante
   - Verificación de la relación de herencia

---

## ✨ Características Implementadas

✅ **Herencia**: `Platillo` y `Bebida` heredan de `Producto` usando `super()`  
✅ **Encapsulación**: Atributo `__precio` privado con métodos de acceso y validación  
✅ **Polimorfismo**: Método `mostrar_informacion()` sobrescrito en clases hijas  
✅ **Modularidad**: Código organizado en paquetes y módulos  
✅ **Validación**: El precio no puede ser negativo ni igual a cero  
✅ **Tipo hints**: Uso de anotaciones de tipo en métodos y parámetros  
✅ **Documentación**: Docstrings en todas las clases y métodos  
✅ **Convenciones**: Nombres descriptivos siguiendo PEP 8  
✅ **Demostración completa**: main.py ejecuta todas las características  

---

## 💡 Reflexión sobre la Importancia de POO

La Programación Orientada a Objetos es fundamental en proyectos Python modulares porque:

1. **Organización**: Los principios de encapsulación y herencia permiten estructurar el código de manera lógica y coherente.

2. **Reutilización**: La herencia evita la duplicación de código. Los atributos y métodos comunes se definen una vez en la clase padre.

3. **Mantenibilidad**: Los cambios en la lógica común (como la validación del precio) se realizan en un solo lugar.

4. **Extensibilidad**: Nuevas clases (como `PlatilloEspecial` o `BebidaSinAlcohol`) pueden heredar de las clases existentes sin modificarlas.

5. **Polimorfismo**: Permite escribir código más flexible que funciona con diferentes tipos de objetos sin conocer específicamente qué tipo son.

6. **Seguridad**: La encapsulación protege los datos internos y evita modificaciones accidentales o maliciosas.

En conclusión, POO facilita la creación de sistemas escalables, mantenibles y profesionales en Python.

---

## 📚 Recursos Utilizados

- **Lenguaje**: Python 3.x
- **Paradigma**: Programación Orientada a Objetos (POO)
- **Principios aplicados**: Herencia, Encapsulación, Polimorfismo
- **Convenciones**: PEP 8 (Style Guide for Python Code)

---

**Fecha de elaboración**: Julio 2024  
**Versión**: 1.0
