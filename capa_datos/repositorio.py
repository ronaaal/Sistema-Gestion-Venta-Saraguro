import mysql.connector

class RepositorioArtesanias:
    def __init__(self):
        self.config = {
            'user': 'root', 'password': 'UTPL2023', 'host': 'localhost',
            'database': 'sistema_sarag', 'port': 3306
        }
        self._inicializar_db()

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def _inicializar_db(self):
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100), tipo VARCHAR(50), precio DECIMAL(10, 2), stock INT, artesana VARCHAR(100)
                )
            """)
            
            # ACTUALIZADO: Agregamos tipo_cliente
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    producto_nombre VARCHAR(100),
                    cantidad INT,
                    total DECIMAL(10,2),
                    metodo_pago VARCHAR(50),
                    tipo_cliente VARCHAR(50),
                    estado VARCHAR(50),
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS eventos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(150), fecha VARCHAR(50), lugar VARCHAR(100), destacado BOOLEAN
                )
            """)
            
            # Datos semilla (solo si está vacío)
            cursor.execute("SELECT count(*) FROM productos")
            if cursor.fetchone()[0] == 0:
                sql_prod = "INSERT INTO productos (nombre, tipo, precio, stock, artesana) VALUES (%s, %s, %s, %s, %s)"
                datos_prod = [('Collar Chakana', 'Collar', 25.00, 10, 'María Saraguro'), ('Aretes Mullos', 'Aretes', 12.50, 20, 'Juana Quizhpe'), ('Poncho Tradicional', 'Vestimenta', 150.00, 5, 'Luis Macas')]
                cursor.executemany(sql_prod, datos_prod)
                
            cursor.execute("SELECT count(*) FROM eventos")
            if cursor.fetchone()[0] == 0:
                sql_evt = "INSERT INTO eventos (nombre, fecha, lugar, destacado) VALUES (%s, %s, %s, %s)"
                cursor.executemany(sql_evt, [('Feria Saraguro', '20-Oct', 'Plaza', True)])

            conn.commit(); cursor.close(); conn.close()
        except Exception as e: print(f"Error DB: {e}")

    def obtener_productos(self):
        conn = self._get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        res = cursor.fetchall(); conn.close()
        return res

    def reducir_stock(self, id_producto, cantidad):
        conn = self._get_connection(); cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (cantidad, id_producto))
        conn.commit(); conn.close()

    def registrar_pedido(self, prod_nombre, cantidad, total, pago, tipo_cliente):
        conn = self._get_connection(); cursor = conn.cursor()
        sql = "INSERT INTO pedidos (producto_nombre, cantidad, total, metodo_pago, tipo_cliente, estado) VALUES (%s, %s, %s, %s, %s, 'Pendiente')"
        cursor.execute(sql, (prod_nombre, cantidad, total, pago, tipo_cliente))
        conn.commit(); conn.close()

    def obtener_eventos(self):
        conn = self._get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT * FROM eventos"); res = cursor.fetchall(); conn.close()
        return res

    # NUEVO: Para ver los pedidos en pantalla
    def obtener_pedidos(self):
        conn = self._get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos ORDER BY id DESC LIMIT 5")
        res = cursor.fetchall(); conn.close()
        return res

    # NUEVO: Simulación de cambio de estado
    def simular_avance_estados(self):
        conn = self._get_connection(); cursor = conn.cursor()
        # 1. De Enviado pasa a Entregado
        cursor.execute("UPDATE pedidos SET estado = 'Entregado' WHERE estado = 'Enviado'")
        # 2. De Pendiente pasa a Enviado
        cursor.execute("UPDATE pedidos SET estado = 'Enviado' WHERE estado = 'Pendiente'")
        conn.commit(); conn.close()