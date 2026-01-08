from capa_datos.repositorio import RepositorioArtesanias

class ServicioVentas:
    def __init__(self):
        self.repo = RepositorioArtesanias()

    def obtener_catalogo(self):
        datos_crudos = self.repo.obtener_todos()
        lista_productos = []
        
        # Transformamos tuplas a diccionarios para que el HTML entienda
        for p in datos_crudos:
            lista_productos.append({
                "id": p[0],
                "nombre": p[1],
                "tipo": p[2],
                "precio": float(p[3]),
                "stock": p[4],
                "artesana": p[5]
            })
        return lista_productos

    def realizar_venta(self, id_producto, cantidad):
        catalogo = self.obtener_catalogo()
        producto = next((p for p in catalogo if p["id"] == int(id_producto)), None)

        # Reglas de Negocio
        if not producto:
            return "Error: Producto no existe."
        
        if cantidad <= 0:
            return "Error: La cantidad debe ser mayor a 0."
            
        if producto["stock"] < cantidad:
            return f"Error: Stock insuficiente. Solo quedan {producto['stock']}."

        # Si pasa las reglas, llamamos a Datos para actualizar
        self.repo.reducir_stock(id_producto, cantidad)
        total = producto["precio"] * cantidad
        
        return f"¡Éxito! Compra realizada por ${total:.2f}. Gracias por apoyar el arte Saraguro."