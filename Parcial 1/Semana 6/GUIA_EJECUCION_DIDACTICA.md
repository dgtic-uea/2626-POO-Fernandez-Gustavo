# 📚 Guía de Ejecución Didáctica - Sistema de Restaurante

## 🎯 Objetivo
Este programa demuestra de forma **interactiva y educativa** los cuatro pilares de la **Programación Orientada a Objetos**:
- ✅ **Herencia**
- ✅ **Encapsulación**
- ✅ **Polimorfismo**
- ✅ **Modularidad**

---

## 🚀 Cómo Ejecutar

### Opción 1: Ejecución Interactiva (RECOMENDADO)

```bash
cd restaurante_app/
python3 main.py
```

El programa se ejecutará con **4 secciones principales**, cada una con pausas interactivas:

```
═══════════════════════════════════════════════════════════════════════════════════════════
 1️⃣  PARTE 1: DEMOSTRACIÓN DE HERENCIA
═══════════════════════════════════════════════════════════════════════════════════════════
   ⏸️  Presiona Enter para continuar...
```

**Simplemente presiona Enter** en cada pausa para avanzar a la siguiente sección.

---

## 📋 Estructura del Programa Interactivo

### 1️⃣ **PARTE 1: DEMOSTRACIÓN DE HERENCIA**

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES LA HERENCIA?                    ┃
┃  La herencia permite que una clase hija  ┃
┃  herede atributos y métodos de una      ┃
┃  clase padre.                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Demuestra:**
- Creación de objeto `Platillo` (clase hija)
- Identificación de atributos **HEREDADOS** de `Producto`:
  - `nombre`
  - `__precio`
  - `disponible`
- Identificación de atributos **PROPIOS** de `Platillo`:
  - `calorias`
  - `tipo_platillo`
- Verificación con `isinstance()` de la relación de herencia

**Salida esperada:**
```
📝 PASO 1: Creando un objeto de tipo Platillo

>>> platillo_1 = Platillo(
        nombre='Lomo a la Pimienta',
        precio=45.99,
        calorias=650,
        tipo_platillo='Principal'
    )

✅ Objeto Platillo creado exitosamente

🔍 Analizando los atributos del objeto:
   ┌─ Atributo: nombre = 'Lomo a la Pimienta'
   │  └─ Origen: HEREDADO de Producto ✓
   │
   ├─ Atributo: __precio = $45.99
   │  └─ Origen: HEREDADO de Producto ✓
   ...
```

---

### 2️⃣ **PARTE 2: DEMOSTRACIÓN DE ENCAPSULACIÓN**

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES LA ENCAPSULACIÓN?               ┃
┃  Protege los atributos privados          ┃
┃  permitiendo acceso solo a través        ┃
┃  de métodos de validación.               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Demuestra 5 pruebas:**

#### Prueba 1: Acceso de Lectura (PERMITIDO)
```python
>>> platillo_1.obtener_precio()
$45.99
✅ Lectura exitosa
```

#### Prueba 2: Acceso Directo (NO PERMITIDO)
```python
>>> platillo_1.precio
❌ Error: 'Platillo' object has no attribute 'precio'
✅ Correcto: El atributo está PROTEGIDO
```

#### Prueba 3: Cambio a Valor Válido
```python
>>> platillo_1.cambiar_precio(55.99)
✅ Cambio exitoso - Precio válido aceptado
Precio: $55.99
```

#### Prueba 4: Cambio a Valor Inválido (Negativo)
```python
>>> platillo_1.cambiar_precio(-10.00)
⚠️ Error: El precio debe ser mayor a cero
✅ Cambio rechazado - VALIDACIÓN lo impidió
```

#### Prueba 5: Cambio a Valor Inválido (Cero)
```python
>>> platillo_1.cambiar_precio(0)
⚠️ Error: El precio debe ser mayor a cero
✅ Cambio rechazado - VALIDACIÓN lo impidió
```

---

### 3️⃣ **PARTE 3: DEMOSTRACIÓN DE POLIMORFISMO**

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES EL POLIMORFISMO?                ┃
┃  Capacidad de objetos diferentes de      ┃
┃  responder al MISMO MENSAJE de formas    ┃
┃  DIFERENTES.                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Demuestra:**
- Creación de múltiples objetos (Platillo y Bebida)
- Almacenamiento en una lista heterogénea
- Iteración sobre la lista
- Llamada al método `mostrar_informacion()` en cada objeto

**Salida esperada:**
```
🔄 ITERACIÓN EN PROGRESO:

═══════════════════════════════════════════════════════════════════════════════════════════

🔹 1. Iteración - Objeto de tipo: Platillo
   Llamando al método: mostrar_informacion()
   Salida del método:
   🍽️  PLATILLO | Principal: Lomo a la Pimienta | Precio: $55.99 | Calorías: 650 cal | ✓ Disponible

🔹 2. Iteración - Objeto de tipo: Platillo
   Llamando al método: mostrar_informacion()
   Salida del método:
   🍽️  PLATILLO | Entrada: Ensalada Mixta | Precio: $12.50 | Calorías: 280 cal | ✓ Disponible

🔹 3. Iteración - Objeto de tipo: Bebida
   Llamando al método: mostrar_informacion()
   Salida del método:
   🥤 BEBIDA | Jugo: Jugo de Naranja Natural | Precio: $4.50 | Volumen: 350 ml | ✓ Disponible

🔹 4. Iteración - Objeto de tipo: Bebida
   Llamando al método: mostrar_informacion()
   Salida del método:
   🥤 BEBIDA | Agua: Agua Mineral | Precio: $2.00 | Volumen: 500 ml | ✓ Disponible

═══════════════════════════════════════════════════════════════════════════════════════════

🎯 CONCLUSIÓN DE POLIMORFISMO:

   ✓ Todos los objetos respondieron al mismo mensaje: mostrar_informacion()
   ✓ Pero CADA UNO mostró su PROPIA versión según su tipo:
     - Platillo mostró: tipo, nombre, precio, calorías, estado
     - Bebida mostró: tipo, nombre, precio, volumen, estado
   ✓ Esto es POLIMORFISMO: Un MISMO MÉTODO, MÚLTIPLES FORMAS de ejecutarse
```

---

### 4️⃣ **PARTE 4: SISTEMA COMPLETO**

Integración de todas las técnicas:
- Creación de un restaurante
- Agregación de múltiples productos
- Listado del menú (demuestra polimorfismo)
- Estadísticas del restaurante

---

## 🎓 Conceptos Clave Explicados

### HERENCIA
```
Producto (CLASE PADRE)
   ↓ hereda
Platillo (CLASE HIJA) + Bebida (CLASE HIJA)
```
- **Ventaja:** Reutilización de código
- **Método:** `super()` en constructor
- **Verificación:** `isinstance()`

### ENCAPSULACIÓN
```
__precio (PRIVADO)
   ↓ acceso controlado
obtener_precio()      (LECTURA)
cambiar_precio()      (ESCRITURA CON VALIDACIÓN)
```
- **Ventaja:** Protección de datos
- **Validación:** precio > 0

### POLIMORFISMO
```
mostrar_informacion() en Producto
   ↓ sobrescrito en
mostrar_informacion() en Platillo
mostrar_informacion() en Bebida
```
- **Ventaja:** Código flexible
- **Demostración:** Iteración sobre lista heterogénea

### MODULARIDAD
```
restaurante_app/
├── modelos/          (Clases del dominio)
├── servicios/        (Clases de negocio)
└── main.py           (Punto de entrada)
```

---

## 📊 Ejemplos de Salida

### Herencia - Verificación
```
>>> isinstance(platillo_1, Platillo)
True  ✅ Es instancia de Platillo

>>> isinstance(platillo_1, Producto)
True  ✅ Es instancia de Producto
└─ Esto demuestra que HEREDA de Producto
```

### Encapsulación - Pruebas
```
PRUEBA 1: Lectura permitida
>>> platillo_1.obtener_precio()
$45.99
✅ Éxito

PRUEBA 2: Acceso directo no permitido
>>> platillo_1.precio
❌ AttributeError
✅ Protección funciona

PRUEBA 3: Validación funcionando
>>> platillo_1.cambiar_precio(-10)
⚠️ Error: Precio debe ser > 0
✅ Validación funcionó
```

### Polimorfismo - Iteración
```
🔹 1. Tipo: Platillo
   🍽️  PLATILLO | Principal: Lomo... (versión Platillo)

🔹 2. Tipo: Bebida
   🥤 BEBIDA | Jugo: Jugo de... (versión Bebida)
   
✓ Mismo método, diferente salida = POLIMORFISMO
```

---

## 💡 Consejos para Aprender

1. **Ejecuta sin prisa:** Lee cada sección antes de presionar Enter
2. **Observa los cambios:** Fíjate cómo cambian los valores según las operaciones
3. **Identifica patrones:** 
   - Herencia → atributos heredados
   - Encapsulación → validación de precios
   - Polimorfismo → diferente salida por tipo
4. **Modifica y experimenta:** Cambia valores en main.py y observa resultados

---

## 🔧 Personalización

Para experimentar, edita `/main.py` y cambia:

**Crear más productos:**
```python
platillo_4 = Platillo(
    nombre="Tu Platillo",
    precio=15.00,
    calorias=500,
    tipo_platillo="Tipo"
)
```

**Cambiar validaciones:**
En `/modelos/producto.py`:
```python
def cambiar_precio(self, nuevo_precio: float) -> bool:
    if nuevo_precio <= 0:  # Cambia esta condición
        ...
```

---

## 📚 Archivos Relacionados

- **main.py** → Programa interactivo didáctico
- **README.md** → Documentación completa
- **modelos/producto.py** → Clase padre con encapsulación
- **modelos/platillo.py** → Clase hija con herencia
- **modelos/bebida.py** → Clase hija con herencia
- **servicios/restaurante.py** → Demostración de polimorfismo

---

## ✨ Conclusión

Este programa educativo te permite:
✅ Ver cómo funciona la **herencia** en acción  
✅ Entender la **encapsulación** con validación  
✅ Experimentar el **polimorfismo** en iteraciones  
✅ Apreciar la **modularidad** del código  

¡Ahora comprenderás por qué POO es fundamental en programación profesional!

