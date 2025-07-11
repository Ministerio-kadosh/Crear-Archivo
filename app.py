from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    data = request.get_json()
    nombre = data.get('nombre', 'SinNombre')

    contenido = f"Informe generado para: {nombre}\nGracias por usar el sistema."

    buffer = io.BytesIO()
    buffer.write(contenido.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='informe.txt', mimetype='text/plain')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
