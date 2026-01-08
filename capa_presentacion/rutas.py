from flask import Flask, render_template, request
from capa_negocio.servicios import ServicioVentas

app = Flask(__name__)
gestor = ServicioVentas()

@app.route('/')
def inicio():
    productos = gestor.obtener_catalogo()
    return render_template('index.html', productos=productos)

@app.route('/comprar', methods=['POST'])
def procesar_compra():
    id_prod = int(request.form['id'])
    cant = int(request.form['cantidad'])
    
    mensaje = gestor.realizar_venta(id_prod, cant)
    
    # Recargamos la página con los datos actualizados
    productos = gestor.obtener_catalogo()
    return render_template('index.html', productos=productos, mensaje=mensaje)

def main():
    app.run(debug=True, port=5000)