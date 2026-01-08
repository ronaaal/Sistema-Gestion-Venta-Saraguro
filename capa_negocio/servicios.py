import threading
import time
from capa_datos.repositorio import RepositorioArtesanias

class ServicioVentas:
    def __init__(self):
        self.repo = RepositorioArtesanias()
        # Iniciamos el hilo de simulación automáticamente
        self._iniciar_simulacion()

    def _iniciar_simulacion(self):
        def tarea_automatica():
            while True:
                time.sleep(5) # Espera 5 segundos
                self.repo.simular_avance_estados()
                
        hilo = threading.Thread(target=tarea_automatica, daemon=True)
        hilo.start()

    def obtener_todo(self):
        # Método auxiliar para traer todo de una vez a la vista
        prods = [{"id": p[0], "nombre": p[1], "tipo": p[2], "precio": float(p[3]), "stock": p[4], "artesana": p[5]} for p in self.repo.obtener_productos()]
        evts = [{"id": e[0], "nombre": e[1], "fecha": e[2], "lugar": e[3], "destacado": e[4]} for e in self.repo.obtener_eventos()]
        pedidos = [{"id": p[0], "prod": p[1], "total": float(p[3]), "pago": p[4], "cliente": p[5], "estado": p[6]} for p in self.repo.obtener_pedidos()]
        return prods, evts, pedidos

    def realizar_venta(self, id_producto, cantidad, pago, tipo_cliente):
        datos_prod = self.repo.obtener_productos()
        producto = next((p for p in datos_prod if p[0] == int(id_producto)), None) # Buscamos por ID en la tupla

        if not producto or producto[4] < cantidad: # index 4 es stock
            return "Error: Stock insuficiente."

        total = float(producto[3]) * cantidad
        
        self.repo.reducir_stock(id_producto, cantidad)
        self.repo.registrar_pedido(producto[1], cantidad, total, pago, tipo_cliente)
        
        return f"Pedido Registrado para {tipo_cliente}. Estado: Pendiente."