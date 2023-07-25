from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esta clave por una segura en producción
jwt = JWTManager(app)

# Datos de usuarios para este ejemplo (en una aplicación real, estos datos deben almacenarse de manera segura)
USUARIOS = {
    "usuario": "contrasena"
}

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('xxxxx')
    password = request.json.get('xxxxx')

    if not username or not password:
        return jsonify({"error": "Falta el nombre de usuario o contraseña"}), 400

    if username in USUARIOS and USUARIOS[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

@app.route('/api/operacion', methods=['POST'])
@jwt_required()  # Esta ruta está protegida con JWT, el cliente debe proporcionar un token válido para acceder a ella
def operacion():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operator = data['operator']

    if operator == 'add':
        result = num1 + num2
    elif operator == 'sub':
        result = num1 - num2
    elif operator == 'mul':
        result = num1 * num2
    elif operator == 'div':
        result = num1 / num2
    else:
        return jsonify({'error': 'Operador inválido'}), 400

    # Acceder al usuario autenticado (si lo necesitas)
    current_user = get_jwt_identity()

    return jsonify({'resultado': result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
