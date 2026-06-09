# Programa principal - Programación Orientada a Objetos
# Demostración de uso de clases y objetos

from mascota import Mascota


def main():
    """Función principal que crea objetos Mascota y ejecuta sus métodos"""
    
    print("="*50)
    print("BIENVENIDO A LA TIENDA DE MASCOTAS")
    print("="*50)
    print("\nDemostración de Programación Orientada a Objetos")
    print("Creando instancias (objetos) de la clase Mascota\n")
    
    # Crear el primer objeto Mascota
    mascota1 = Mascota("Max", "Perro", 5)
    
    # Crear el segundo objeto Mascota
    mascota2 = Mascota("Whiskers", "Gato", 3)
    
    # Crear objetos adicionales para mayor demostración
    mascota3 = Mascota("Tweety", "Pajaro", 2)
    mascota4 = Mascota("Luna", "Conejo", 1)
    
    # Lista de mascotas para iterar
    mascotas = [mascota1, mascota2, mascota3, mascota4]
    
    # Ejecutar métodos para cada mascota
    print("\n" + "-"*50)
    print("MOSTRANDO INFORMACIÓN DE MASCOTAS")
    print("-"*50)
    
    for mascota in mascotas:
        mascota.mostrar_informacion()
    
    # Demostrar el método hacer_sonido()
    print("\n" + "-"*50)
    print("SONIDOS DE LAS MASCOTAS")
    print("-"*50)
    
    for mascota in mascotas:
        mascota.hacer_sonido()
    
    print("\n" + "="*50)
    print("FIN DEL PROGRAMA")
    print("="*50 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

