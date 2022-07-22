from threading import Thread

class Cliente(Thread):
    """
    Gestiona los clientes.
    """
    
    def __init__(self, conexion, direccion):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conexion = conexion
        self.direccion = direccion
    
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                datos_recibidos = self.conexion.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if datos_recibidos:
                    self.conexion.send(datos_recibidos)
