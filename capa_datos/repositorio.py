import mysql.connector

class RepositorioArtesanias:
    def __init__(self):
        # Configuración de conexión
        self.config = {
            'user': 'root',          
            'password': 'UTPL2023',          
            'host': 'localhost',
            'database': 'sistema_sarag', 
            'port': 3306
        }
        self._inicializar_db()

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def _inicializar_db(self):
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Crear tabla si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100),
                    tipo VARCHAR(50),
                    precio DECIMAL(10, 2),
                    stock INT,
                    artesana VARCHAR(100)
                )
            """)
            
            # Insertar datos de prueba si la tabla está vacía
            cursor.execute("SELECT count(*) FROM productos")
            if cursor.fetchone()[0] == 0:
                sql = "INSERT INTO productos (nombre, tipo, precio, stock, artesana) VALUES (%s, %s, %s, %s, %s)"
                datos = [
                    ('Collar Chakana', 'Collar', 25.00, 10, 'María Saraguro'),
                    ('Aretes de Mullos', 'Aretes', 12.50, 20, 'Juana Quizhpe'),
                    ('Manilla Tejida', 'Manilla', 8.00, 15, 'Rosa Gualán')
                ]
                cursor.executemany(sql, datos)
                conn.commit()
            
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error en BD: {err}")

    def obtener_todos(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

    def reducir_stock(self, id_producto, cantidad):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (cantidad, id_producto))
        conn.commit()
        cursor.close()
        conn.close()