# Programa de Programación Tradicional - Registro de Mascotas
# Sin uso de clases ni objetos, utilizando funciones y variables

def obtener_datos_mascota():
    """Función para obtener los datos de la mascota por teclado"""
    print("\n" + "="*50)
    print("Ingrese los datos de su mascota")
    print("="*50)
    
    nombre = input("Ingrese nombre mascota: ")
    especie = input("Ingrese especie mascota: ")
    edad = input("Ingrese edad mascota: ")
    color = input("Ingrese color mascota: ")
    peso = input("Ingrese peso mascota (kg): ")
    
    return nombre, especie, edad, color, peso


def mostrar_datos_mascota(nombre, especie, edad, color, peso):
    """Función para mostrar los datos de la mascota de forma organizada"""
    print("\n" + "="*50)
    print("INFORMACIÓN DE LA MASCOTA")
    print("="*50)
    print(f"Nombre:  {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad:    {edad} años")
    print(f"Color:   {color}")
    print(f"Peso:    {peso} kg")
    print("="*50 + "\n")


def menu_principal():
    """Función para mostrar el menú principal"""
    print("Hola bienvenido a tu tienda mascotas. ¡Ayudame con los datos de tu mascota!!!")
    
    # Obtener datos de la mascota
    nombre, especie, edad, color, peso = obtener_datos_mascota()
    
    # Mostrar datos registrados
    mostrar_datos_mascota(nombre, especie, edad, color, peso)


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()


