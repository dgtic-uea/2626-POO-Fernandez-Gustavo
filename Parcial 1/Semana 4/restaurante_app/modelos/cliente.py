"""
Módulo que define la clase Cliente para representar a los clientes del restaurante.
"""


class Cliente:
    """
    Representa un cliente del restaurante.

    Atributos:
        - id: identificador único del cliente
        - nombre: nombre completo del cliente
        - email: correo electrónico del cliente
        - telefono: número de teléfono del cliente
        - pedidos: lista de pedidos realizados por el cliente
    """

    # Variable de clase para generar IDs únicos automáticamente
    contador_id = 500

    def __init__(self, nombre, email, telefono):
        """
        Constructor que inicializa un nuevo cliente.

        Args:
            nombre: nombre completo del cliente
            email: correo electrónico del cliente
            telefono: número de teléfono del cliente
        """
        self.id = Cliente.contador_id
        Cliente.contador_id += 1
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos = []  # Lista para almacenar los pedidos del cliente

    def agregar_pedido(self, numero_pedido):
        """
        Registra un nuevo pedido en el historial del cliente.

        Args:
            numero_pedido: número o identificador del pedido
        """
        self.pedidos.append(numero_pedido)

    def obtener_cantidad_pedidos(self):
        """
        Retorna la cantidad total de pedidos realizados por el cliente.

        Returns:
            cantidad de pedidos (entero)
        """
        return len(self.pedidos)

    def obtener_info(self):
        """
        Retorna un diccionario con la información del cliente.

        Returns:
            diccionario con los atributos del cliente
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'total_pedidos': self.obtener_cantidad_pedidos()
        }

    def __str__(self):
        """
        Representación en texto del cliente.
        """
        return f"[{self.id}] {self.nombre} | Email: {self.email} | Tel: {self.telefono} | Pedidos: {self.obtener_cantidad_pedidos()}"

    def __repr__(self):
        """Representación para desarrolladores."""
        return f"Cliente(id={self.id}, nombre='{self.nombre}', email='{self.email}')"

