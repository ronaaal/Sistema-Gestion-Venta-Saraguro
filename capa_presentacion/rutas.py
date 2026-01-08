from flask import Flask, render_template, request, redirect, url_for
from capa_negocio.servicios import ServicioVentas

app = Flask(__name__)
gestor = ServicioVentas()

@app.route('/')
def inicio():
    # Capturamos el mensaje si viene en la URL (después de una redirección)
    mensaje = request.args.get('mensaje')
    
    productos, eventos, pedidos = gestor.obtener_todo()
    return render_template('index.html', productos=productos, eventos=eventos, pedidos=pedidos, mensaje=mensaje)

@app.route('/comprar', methods=['POST'])
def procesar_compra():
    id_prod = int(request.form['id'])
    cant = int(request.form['cantidad'])
    pago = request.form['pago']
    tipo_cliente = request.form['tipo_cliente']
    
    # Procesamos la venta
    mensaje_resultado = gestor.realizar_venta(id_prod, cant, pago, tipo_cliente)
    
    # CORRECCIÓN: En lugar de renderizar aquí, redirigimos al inicio
    # enviando el mensaje en la URL para que no se pierda.
    return redirect(url_for('inicio', mensaje=mensaje_resultado))

def main():
    app.run(debug=True, port=5000)