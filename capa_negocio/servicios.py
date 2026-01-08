from capa_datos.repositorio import RepositorioArtesanias

class ServicioVentas:
    def __init__(self):
        self.repo = RepositorioArtesanias()

    def obtener_catalogo(self):
        datos = self.repo.obtener_productos()
        return [{"id": p[0], "nombre": p[1], "tipo": p[2], "precio": float(p[3]), "stock": p[4], "artesana": p[5]} for p in datos]

    def obtener_eventos(self):
        # Lógica de Promoción: Traer eventos para mostrar cultura
        datos = self.repo.obtener_eventos()
        return [{"id": e[0], "nombre": e[1], "fecha": e[2], "lugar": e[3], "destacado": e[4]} for e in datos]

    def realizar_venta(self, id_producto, cantidad, metodo_pago="Efectivo"):
        catalogo = self.obtener_catalogo()
        producto = next((p for p in catalogo if p["id"] == int(id_producto)), None)

        if not producto or producto["stock"] < cantidad:
            return "Error: Stock insuficiente o producto no encontrado."

        # 1. Actualizar Stock
        self.repo.reducir_stock(id_producto, cantidad)
        
        # 2. Registrar el Pedido (Requisito nuevo)
        total = producto["precio"] * cantidad
        self.repo.registrar_pedido(producto["nombre"], cantidad, total, metodo_pago)
        
        return f"Pedido Registrado: {cantidad}x {producto['nombre']} | Estado: Pendiente | Total: ${total:.2f}"