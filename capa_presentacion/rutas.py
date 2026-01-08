from flask import Flask, render_template, request
from capa_negocio.servicios import ServicioVentas

app = Flask(__name__)
gestor = ServicioVentas()

@app.route('/')
def inicio():
    # Ahora traemos productos Y eventos
    productos = gestor.obtener_catalogo()
    eventos = gestor.obtener_eventos()
    return render_template('index.html', productos=productos, eventos=eventos)

@app.route('/comprar', methods=['POST'])
def procesar_compra():
    id_prod = int(request.form['id'])
    cant = int(request.form['cantidad'])
    pago = request.form['pago'] # Capturamos forma de pago
    
    mensaje = gestor.realizar_venta(id_prod, cant, pago)
    
    # Recargar todo
    productos = gestor.obtener_catalogo()
    eventos = gestor.obtener_eventos()
    return render_template('index.html', productos=productos, eventos=eventos, mensaje=mensaje)

def main():
    app.run(debug=True, port=5000)