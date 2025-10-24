from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Portal de Pagos</title>
</head>
<body>
    <h1>Hola, {{ nombre }}!</h1>
    <p>Esta es la aplicación de ejemplo del App Lead.</p>
    <p>Prueba: ?nombre=<script>alert('XSS')</script></p>
</body>
</html>
"""

@app.route('/')
def home():
    nombre = request.args.get('nombre', 'Mundo')
    return render_template_string(HTML_TEMPLATE, nombre=nombre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
