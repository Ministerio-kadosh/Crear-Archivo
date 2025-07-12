from flask import Flask, render_template, request, send_file
from docx import Document
import io
import os
from email import enviar_por_correo  # 👈 Import necesario

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    data = request.get_json()
    nombre = data.get('nombre', 'SinNombre')

    # Crear documento Word
    doc = Document()
    doc.add_heading('Informe de Usuario', 0)
    doc.add_paragraph(f'Nombre: {nombre}')

    table = doc.add_table(rows=2, cols=3)
    table.style = 'Table Grid'
    table.cell(0, 0).text = 'Producto'
    table.cell(0, 1).text = 'Cantidad'
    table.cell(0, 2).text = 'Precio'
    table.cell(1, 0).text = 'Chetos'
    table.cell(1, 1).text = '2'
    table.cell(1, 2).text = '$20'

    # Guardar en memoria
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    # Enviar por correo
    correos = ['correo1@gmail.com', 'correo2@gmail.com']
    enviar_por_correo(buffer, correos)

    # Descargar
    buffer.seek(0)
    return send_file(
    buffer,
    as_attachment=True,
    download_name='informe.docx',
    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
