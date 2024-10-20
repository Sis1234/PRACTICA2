from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
data_store = {
    'inscripcion_curso': [],
    'registro_usuarios': [],
    'registro_productos': [],
    'registro_libros': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        
        data_store['inscripcion_curso'].append({'nombre': nombre, 'apellidos': apellidos, 'curso': curso})
        
        return redirect(url_for('index', success=True))
    return render_template('inscripcion_curso.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        
        data_store['registro_usuarios'].append({'nombre': nombre, 'apellidos': apellidos, 'email': email, 'password': password})
        
        return redirect(url_for('index', success=True))
    return render_template('registro_usuarios.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        
        data_store['registro_productos'].append({'producto': producto, 'categoria': categoria, 'existencia': existencia, 'precio': precio})
        
        return redirect(url_for('index', success=True))
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        
        data_store['registro_libros'].append({'titulo': titulo, 'autor': autor, 'resumen': resumen, 'medio': medio})
        
        return redirect(url_for('index', success=True))
    return render_template('registro_libros.html')

@app.route('/mostrar_datos')
def mostrar_datos():
    return render_template('mostrar_datos.html', data_store=data_store)

if __name__ == '__main__':
    app.run(debug=True)
