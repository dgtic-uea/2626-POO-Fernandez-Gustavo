"""
Módulo Cliente: contiene la clase Cliente implementada con @dataclass
para simplificar la definición de clases de datos.
"""
from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante.

    Utiliza el decorador @dataclass que genera automáticamente __init__,
    __repr__, __eq__ y otros métodos especiales.

    Atributos:
        id_cliente: identificador único del cliente
        nombre: nombre completo del cliente
        correo: correo electrónico del cliente
    """
    id_cliente: str
    nombre: str
    correo: str

    def mostrar_informacion(self):
        """
        Retorna una representación legible de la información del cliente.

        Returns:
            str: información formateada del cliente
        """
        return (
            f"Cliente ID: {self.id_cliente}\n"
            f"  Nombre: {self.nombre}\n"
            f"  Correo: {self.correo}"
        )

    def __str__(self):
        """Representación en string del cliente."""
        return f"{self.nombre} ({self.id_cliente}) - {self.correo}"

