"""
Archivo principal de la aplicación de restaurante.
Demostración DIDÁCTICA de los principios de POO:
- Herencia (Platillo y Bebida heredan de Producto)
- Encapsulación (precio privado con métodos de acceso)
- Polimorfismo (mostrar_informacion() se ejecuta diferente en cada tipo de objeto)
"""

from modelos import Producto, Platillo, Bebida
from servicios import Restaurante


def separador(titulo: str = "", simbolo: str = "=", ancho: int = 100):
    """Imprime un separador visual con título opcional."""
    if titulo:
        espacios_laterales = (ancho - len(titulo) - 4) // 2
        print(f"\n{simbolo * espacios_laterales} {titulo} {simbolo * espacios_laterales}\n")
    else:
        print(f"\n{simbolo * ancho}\n")


def pausa(texto: str = "Presiona Enter para continuar..."):
    """Pausa el programa y espera entrada del usuario."""
    input(f"\n⏸️  {texto}")


def main():
    """
    Función principal que demuestra de forma DIDÁCTICA cómo funcionan los
    principios fundamentales de la Programación Orientada a Objetos.
    """
    
    # ===================== PORTADA =====================
    print("\n" + "="*100)
    print("╔" + "="*98 + "╗")
    print("║" + " "*98 + "║")
    print("║" + " " * 15 + "🏪 SISTEMA DE RESTAURANTE - DEMONSTRACIÓN DIDÁCTICA DE POO" + " " * 20 + "║")
    print("║" + " " * 20 + "Herencia | Encapsulación | Polimorfismo | Modularidad" + " " * 16 + "║")
    print("║" + " "*98 + "║")
    print("╚" + "="*98 + "╝")
    print("="*100)

    pausa()

    # ==================== 1. DEMOSTRACIÓN DE HERENCIA ====================
    separador("1️⃣  PARTE 1: DEMOSTRACIÓN DE HERENCIA", "═")
    
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES LA HERENCIA?                                                                  ┃
┃  ─────────────────────                                                                 ┃
┃  La herencia permite que una clase (hija) herede atributos y métodos de otra           ┃
┃  clase (padre), evitando la duplicación de código y promoviendo reutilización.         ┃
┃                                                                                         ┃
┃  JERARQUÍA EN NUESTRO PROYECTO:                                                        ┃
┃                                                                                         ┃
┃                         ┌──────────────┐                                                ┃
┃                         │  Producto    │  ← CLASE PADRE (superclase)                   ┃
┃                         │ (clase base) │    Atributos: nombre, __precio, disponible   ┃
┃                         └──────────────┘                                                ┃
┃                              ▲                                                          ┃
┃                         ┌────┴────┐                                                     ┃
┃                         │          │                                                    ┃
┃                    ┌─────────┐ ┌──────────┐                                             ┃
┃                    │ Platillo│ │ Bebida   │  ← CLASES HIJAS                            ┃
┃                    └─────────┘ └──────────┘    Heredan todo de Producto               ┃
┃                    + calorias  + volumen_ml    + Agregan atributos propios             ┃
┃                    + tipo      + tipo                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

    pausa("Vamos a crear objetos para demostrar la herencia...")

    print("\n📝 PASO 1: Creando un objeto de tipo Platillo\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1 = Platillo(")
    print("        nombre='Lomo a la Pimienta',")
    print("        precio=45.99,")
    print("        calorias=650,")
    print("        tipo_platillo='Principal'")
    print("    )")
    print("─" * 100)
    
    platillo_1 = Platillo(
        nombre="Lomo a la Pimienta",
        precio=45.99,
        calorias=650,
        tipo_platillo="Principal"
    )
    
    print("\n✅ Objeto Platillo creado exitosamente\n")
    print("🔍 Analizando los atributos del objeto:")
    print(f"   ┌─ Atributo: nombre = '{platillo_1.nombre}'")
    print(f"   │  └─ Origen: HEREDADO de Producto ✓")
    print(f"   │")
    print(f"   ├─ Atributo: __precio = ${platillo_1.obtener_precio():.2f}")
    print(f"   │  └─ Origen: HEREDADO de Producto (acceso a través de obtener_precio()) ✓")
    print(f"   │")
    print(f"   ├─ Atributo: disponible = {platillo_1.disponible}")
    print(f"   │  └─ Origen: HEREDADO de Producto ✓")
    print(f"   │")
    print(f"   ├─ Atributo: calorias = {platillo_1.calorias}")
    print(f"   │  └─ Origen: PROPIO de Platillo (específico) ✓")
    print(f"   │")
    print(f"   └─ Atributo: tipo_platillo = '{platillo_1.tipo_platillo}'")
    print(f"      └─ Origen: PROPIO de Platillo (específico) ✓")

    pausa()

    print("\n📝 PASO 2: Creando un objeto de tipo Bebida\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> bebida_1 = Bebida(")
    print("        nombre='Jugo de Naranja Natural',")
    print("        precio=4.50,")
    print("        volumen_ml=350,")
    print("        tipo_bebida='Jugo'")
    print("    )")
    print("─" * 100)
    
    bebida_1 = Bebida(
        nombre="Jugo de Naranja Natural",
        precio=4.50,
        volumen_ml=350,
        tipo_bebida="Jugo"
    )
    
    print("\n✅ Objeto Bebida creado exitosamente\n")
    print("🔍 Analizando los atributos del objeto:")
    print(f"   ┌─ Atributo: nombre = '{bebida_1.nombre}'")
    print(f"   │  └─ Origen: HEREDADO de Producto ✓")
    print(f"   │")
    print(f"   ├─ Atributo: __precio = ${bebida_1.obtener_precio():.2f}")
    print(f"   │  └─ Origen: HEREDADO de Producto (acceso a través de obtener_precio()) ✓")
    print(f"   │")
    print(f"   ├─ Atributo: disponible = {bebida_1.disponible}")
    print(f"   │  └─ Origen: HEREDADO de Producto ✓")
    print(f"   │")
    print(f"   ├─ Atributo: volumen_ml = {bebida_1.volumen_ml} ml")
    print(f"   │  └─ Origen: PROPIO de Bebida (específico) ✓")
    print(f"   │")
    print(f"   └─ Atributo: tipo_bebida = '{bebida_1.tipo_bebida}'")
    print(f"      └─ Origen: PROPIO de Bebida (específico) ✓")

    pausa()

    print("\n📝 PASO 3: Verificando la relación de herencia\n")
    print("─" * 100)
    print("Usando la función isinstance() para verificar herencia:")
    print("─" * 100)
    
    print(f"\n>>> isinstance(platillo_1, Platillo)")
    print(f"    {isinstance(platillo_1, Platillo)}  ✅ Es instancia de Platillo")
    
    print(f"\n>>> isinstance(platillo_1, Producto)")
    print(f"    {isinstance(platillo_1, Producto)}  ✅ Es instancia de Producto")
    print(f"    └─ Esto demuestra que HEREDA de Producto")
    
    print(f"\n>>> isinstance(bebida_1, Bebida)")
    print(f"    {isinstance(bebida_1, Bebida)}  ✅ Es instancia de Bebida")
    
    print(f"\n>>> isinstance(bebida_1, Producto)")
    print(f"    {isinstance(bebida_1, Producto)}  ✅ Es instancia de Producto")
    print(f"    └─ Esto demuestra que HEREDA de Producto")

    pausa()

    # ==================== 2. DEMOSTRACIÓN DE ENCAPSULACIÓN ====================
    separador("2️⃣  PARTE 2: DEMOSTRACIÓN DE ENCAPSULACIÓN", "═")
    
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES LA ENCAPSULACIÓN?                                                             ┃
┃  ──────────────────────────                                                            ┃
┃  La encapsulación protege los atributos internos de una clase impidiendo su acceso     ┃
┃  directo desde fuera. Solo se permite acceso a través de métodos específicos que       ┃
┃  pueden validar los datos.                                                             ┃
┃                                                                                         ┃
┃  EN NUESTRO PROYECTO:                                                                  ┃
┃  • El atributo __precio (con doble guion) es PRIVADO                                   ┃
┃  • NO se puede acceder como: producto.precio                                           ┃
┃  • SOLO se accede a través de estos métodos:                                           ┃
┃                                                                                         ┃
┃    ┌─ obtener_precio()      → LECTURA segura (sin validación)                          ┃
┃    │  Uso: precio = producto.obtener_precio()                                         ┃
┃    │                                                                                    ┃
┃    └─ cambiar_precio()      → ESCRITURA con VALIDACIÓN                                 ┃
┃       Uso: producto.cambiar_precio(nuevo_precio)                                      ┃
┃       Validación: nuevo_precio debe ser > 0                                            ┃
┃                                                                                         ┃
┃  VENTAJAS:                                                                             ┃
┃  ✓ Protege la integridad de los datos                                                  ┃
┃  ✓ Valida datos antes de cambiarlos                                                    ┃
┃  ✓ Evita cambios accidentales o maliciosos                                             ┃
┃  ✓ Permite cambiar la implementación interna sin afectar el código externo              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

    pausa("Vamos a demostrar la encapsulación del atributo __precio...")

    print("\n📝 PRUEBA 1: ACCESO DE LECTURA (PERMITIDO)\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1.obtener_precio()")
    print("─" * 100)
    
    precio = platillo_1.obtener_precio()
    print(f"\nResultado: ${precio:.2f}")
    print("✅ Lectura exitosa a través del método obtener_precio()")

    pausa()

    print("\n📝 PRUEBA 2: ACCESO DIRECTO (NO PERMITIDO)\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1.precio  # Intento de acceso DIRECTO al atributo")
    print("─" * 100)
    
    try:
        valor = platillo_1.precio
        print(f"Resultado: {valor}")
    except AttributeError as e:
        print(f"\n❌ Error: {e}")
        print("✅ Correcto: El atributo NO es accesible directamente")
        print("   └─ Está PROTEGIDO por la encapsulación")

    pausa()

    print("\n📝 PRUEBA 3: CAMBIO DE PRECIO A VALOR VÁLIDO\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1.cambiar_precio(55.99)")
    print("─" * 100)
    
    print(f"\nPrecio actual: ${platillo_1.obtener_precio():.2f}")
    print("Nuevo precio: $55.99")
    platillo_1.cambiar_precio(55.99)
    print(f"Precio actualizado: ${platillo_1.obtener_precio():.2f}")
    print("✅ Cambio exitoso - Precio válido aceptado")

    pausa()

    print("\n📝 PRUEBA 4: CAMBIO DE PRECIO A VALOR INVÁLIDO (NEGATIVO)\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1.cambiar_precio(-10.00)")
    print("─" * 100)
    
    print(f"\nPrecio actual: ${platillo_1.obtener_precio():.2f}")
    print("Intento de cambio a: -$10.00")
    resultado = platillo_1.cambiar_precio(-10.00)
    print(f"Precio después del intento: ${platillo_1.obtener_precio():.2f}")
    print("✅ Cambio rechazado - Valor inválido (negativo)")
    print("   └─ La VALIDACIÓN en cambiar_precio() lo impidió")

    pausa()

    print("\n📝 PRUEBA 5: CAMBIO DE PRECIO A VALOR INVÁLIDO (CERO)\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> platillo_1.cambiar_precio(0)")
    print("─" * 100)
    
    print(f"\nPrecio actual: ${platillo_1.obtener_precio():.2f}")
    print("Intento de cambio a: $0.00")
    resultado = platillo_1.cambiar_precio(0)
    print(f"Precio después del intento: ${platillo_1.obtener_precio():.2f}")
    print("✅ Cambio rechazado - Valor inválido (cero)")
    print("   └─ La VALIDACIÓN en cambiar_precio() lo impidió")

    pausa()

    print("\n🎯 CONCLUSIÓN DE ENCAPSULACIÓN:\n")
    print("   El atributo __precio está PROTEGIDO de la siguiente forma:")
    print("   ✓ Solo se puede LEER a través de: obtener_precio()")
    print("   ✓ Solo se puede ESCRIBIR a través de: cambiar_precio()")
    print("   ✓ Cada cambio es VALIDADO (precio > 0)")
    print("   ✓ Nunca puede tener valores inválidos")

    pausa()

    # ==================== 3. DEMOSTRACIÓN DE POLIMORFISMO ====================
    separador("3️⃣  PARTE 3: DEMOSTRACIÓN DE POLIMORFISMO", "═")
    
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ¿QUÉ ES EL POLIMORFISMO?                                                              ┃
┃  ─────────────────────────                                                             ┃
┃  Polimorfismo significa "muchas formas". Es la capacidad que tienen objetos            ┃
┃  diferentes de responder al MISMO mensaje (llamada de método) de FORMAS DIFERENTES.    ┃
┃                                                                                         ┃
┃  EN NUESTRO PROYECTO:                                                                  ┃
┃  • Todas las clases tienen el método: mostrar_informacion()                            ┃
┃                                                                                         ┃
┃  • Pero cada clase LO IMPLEMENTA DE FORMA DIFERENTE:                                   ┃
┃                                                                                         ┃
┃    ┌─ Producto.mostrar_informacion()                                                   ┃
┃    │  Muestra: nombre, precio, disponibilidad                                          ┃
┃    │                                                                                    ┃
┃    ├─ Platillo.mostrar_informacion()  (SOBRESCRITO)                                    ┃
┃    │  Muestra: tipo, nombre, precio, calorías, disponibilidad                          ┃
┃    │           └─ Información ESPECÍFICA del platillo                                  ┃
┃    │                                                                                    ┃
┃    └─ Bebida.mostrar_informacion()    (SOBRESCRITO)                                    ┃
┃       Muestra: tipo, nombre, precio, volumen, disponibilidad                           ┃
┃                └─ Información ESPECÍFICA de la bebida                                  ┃
┃                                                                                         ┃
┃  DEMOSTRACIÓN:                                                                         ┃
┃  Cuando se llama a mostrar_informacion() en cada objeto,                               ┃
┃  CADA UNO ejecuta su PROPIA versión del método.                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

    pausa("Vamos a demostrar el polimorfismo...")

    print("\n📝 PASO 1: Creando más objetos para la demostración\n")

    platillo_2 = Platillo(
        nombre="Ensalada Mixta",
        precio=12.50,
        calorias=280,
        tipo_platillo="Entrada"
    )

    bebida_2 = Bebida(
        nombre="Agua Mineral",
        precio=2.00,
        volumen_ml=500,
        tipo_bebida="Agua"
    )

    print("─" * 100)
    print("Objetos creados:")
    print("  • platillo_2 = Platillo('Ensalada Mixta', 12.50, 280, 'Entrada')")
    print("  • bebida_2 = Bebida('Agua Mineral', 2.00, 500, 'Agua')")
    print("─" * 100)
    print("\n✅ Objetos creados exitosamente")

    pausa()

    print("\n📝 PASO 2: Almacenando todos los objetos en una LISTA\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> productos = [platillo_1, platillo_2, bebida_1, bebida_2]")
    print("─" * 100)
    
    productos = [platillo_1, platillo_2, bebida_1, bebida_2]
    
    print(f"\n✅ Lista 'productos' creada con {len(productos)} elementos")
    for i, producto in enumerate(productos, 1):
        tipo = type(producto).__name__
        print(f"   {i}. [{tipo}] {producto.nombre}")

    pausa()

    print("\n📝 PASO 3: Iterando la lista y LLAMANDO mostrar_informacion()\n")
    print("─" * 100)
    print("Código Python:")
    print(">>> for producto in productos:")
    print(">>>     producto.mostrar_informacion()")
    print("─" * 100)
    
    print("\n🔄 ITERACIÓN EN PROGRESO:")
    print("   Cada objeto responde al MISMO mensaje de forma DIFERENTE:\n")
    print("=" * 100)

    for i, producto in enumerate(productos, 1):
        tipo_obj = type(producto).__name__
        print(f"\n🔹 {i}. Iteración - Objeto de tipo: {tipo_obj}")
        print(f"   Llamando al método: mostrar_informacion()")
        print(f"   Salida del método:")
        print(f"   ", end="")
        producto.mostrar_informacion()
        print()

    print("=" * 100)

    pausa()

    print("\n🎯 CONCLUSIÓN DE POLIMORFISMO:\n")
    print("   ✓ Todos los objetos respondieron al mismo mensaje:")
    print("     mostrar_informacion()")
    print("   ")
    print("   ✓ Pero CADA UNO mostró su PROPIA versión según su tipo:")
    print("     - Platillo mostró: tipo, nombre, precio, calorías, estado")
    print("     - Bebida mostró: tipo, nombre, precio, volumen, estado")
    print("   ")
    print("   ✓ Esto es POLIMORFISMO:")
    print("     Un MISMO MÉTODO, MÚLTIPLES FORMAS de ejecutarse")

    pausa()

    # ==================== 4. INTEGRACIÓN: SISTEMA COMPLETO ====================
    separador("4️⃣  PARTE 4: SISTEMA COMPLETO DE RESTAURANTE", "═")

    print("Ahora vamos a ver cómo todas estas técnicas de POO funcionan integradas\n")

    # Creamos el restaurante
    mi_restaurante = Restaurante("La Esquina Gourmet")

    print("📝 PASO 1: Creando el restaurante y más productos\n")

    platillo_3 = Platillo(
        nombre="Tiramisú Italiano",
        precio=8.99,
        calorias=420,
        tipo_platillo="Postre"
    )

    bebida_3 = Bebida(
        nombre="Cerveza Artesanal",
        precio=6.99,
        volumen_ml=355,
        tipo_bebida="Cerveza"
    )

    print("✅ Restaurante creado: 'La Esquina Gourmet'")
    print("✅ Platillo adicional: 'Tiramisú Italiano'")
    print("✅ Bebida adicional: 'Cerveza Artesanal'")

    pausa()

    print("\n📝 PASO 2: Agregando todos los productos al restaurante\n")

    mi_restaurante.agregar_producto(platillo_1)
    mi_restaurante.agregar_producto(platillo_2)
    mi_restaurante.agregar_producto(platillo_3)
    mi_restaurante.agregar_producto(bebida_1)
    mi_restaurante.agregar_producto(bebida_2)
    mi_restaurante.agregar_producto(bebida_3)

    pausa()

    print("\n📝 PASO 3: Listando el menú (POLIMORFISMO en acción)\n")
    print("─" * 100)
    print("Al iterar sobre la lista de productos y llamar mostrar_informacion(),")
    print("cada uno ejecuta su propia versión del método:")
    print("─" * 100)
    
    mi_restaurante.listar_productos()

    pausa()

    print("📝 PASO 4: Mostrando estadísticas\n")
    mi_restaurante.mostrar_estadisticas()

    pausa()

    # CIERRE
    separador("✅ RESUMEN FINAL - CONCEPTOS APRENDIDOS", "═")

    print("""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                          ║
║  1️⃣  HERENCIA                                                                            ║
║  ─────────                                                                               ║
║      ✓ Producto es la clase PADRE (superclase)                                           ║
║      ✓ Platillo y Bebida HEREDAN de Producto                                            ║
║      ✓ Las clases hijas REUTILIZAN: nombre, __precio, disponible                         ║
║      ✓ Las clases hijas AGREGAN: atributos específicos propios                           ║
║      ✓ Se usa super() en el constructor para inicializar la clase padre                  ║
║      ✓ Se verifica con isinstance() para comprobar relaciones                            ║
║                                                                                          ║
║  2️⃣  ENCAPSULACIÓN                                                                       ║
║  ──────────────────                                                                      ║
║      ✓ El atributo __precio es PRIVADO (protegido)                                       ║
║      ✓ Método obtener_precio() → LECTURA segura                                          ║
║      ✓ Método cambiar_precio() → ESCRITURA con VALIDACIÓN                                ║
║      ✓ Impide valores inválidos (precio debe ser > 0)                                     ║
║      ✓ Protege la integridad de los datos                                                ║
║                                                                                          ║
║  3️⃣  POLIMORFISMO                                                                        ║
║  ────────────────                                                                        ║
║      ✓ Todas las clases tienen el método mostrar_informacion()                           ║
║      ✓ Cada clase IMPLEMENTA su propia versión (sobrescritura)                           ║
║      ✓ Todos los objetos responden al MISMO mensaje                                      ║
║      ✓ Pero CADA UNO se comporta diferente según su tipo                                 ║
║      ✓ Se demuestra iterando una lista de productos base                                 ║
║                                                                                          ║
║  4️⃣  MODULARIDAD                                                                         ║
║  ──────────────                                                                          ║
║      ✓ Código organizado en paquetes: modelos/ y servicios/                              ║
║      ✓ Separación clara de responsabilidades                                             ║
║      ✓ Fácil de mantener, extender y reutilizar                                          ║
║      ✓ Cada archivo tiene una responsabilidad específica                                 ║
║                                                                                          ║
║  ════════════════════════════════════════════════════════════════════════════════════════  ║
║                                                                                          ║
║  BENEFICIOS DE APLICAR POO:                                                              ║
║  ✓ Reutilización de código (Herencia)                                                    ║
║  ✓ Protección de datos (Encapsulación)                                                   ║
║  ✓ Flexibilidad del código (Polimorfismo)                                                ║
║  ✓ Mantenibilidad mejorada (Modularidad)                                                 ║
║  ✓ Fácil extensión sin modificar código existente                                        ║
║  ✓ Código más limpio, profesional y escalable                                            ║
║                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
    """)

    print("🎓 ¡Ahora entiendes cómo funcionan los pilares de la Programación Orientada a Objetos!")
    print("="*100 + "\n")


if __name__ == "__main__":
    main()
