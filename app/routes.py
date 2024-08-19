from flask import Blueprint, request, jsonify
import jwt
import uuid
import datetime

# Crear un Blueprint para las rutas
routes = Blueprint('routes', __name__)

# Definimos la API Key, User y Password para acceder a la generación de JWT
API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "your_jwt_secret_key"  # Esto debe ser seguro y único para tu aplicación
USERNAME = "neoris"
PASSWORD = "abc123"

# Middleware para manejar OPTIONS
@routes.before_app_request
def handle_options_request():
    if request.method == 'OPTIONS':
        # Responder con los métodos permitidos
        return '', 204, {'Allow': 'POST, OPTIONS'}

@routes.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

@routes.route('/jwt', methods=['POST'])
def generate_jwt():
    auth_data = request.get_json()
    username = auth_data.get('username')
    password = auth_data.get('password')

    # Validar credenciales
    if username == USERNAME and password == PASSWORD:
        # Generar un JWT único
        transaction_id = str(uuid.uuid4())
        payload = {
            "transaction_id": transaction_id,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)  # El JWT expira en 1 hora
        }
        jwt_token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
        return jsonify({"jwt": jwt_token}), 200
    else:
        return "ERROR: Invalid credentials", 403

@routes.route('/DevOps', methods=['POST'])
def devops_endpoint():
    # Validar la API Key
    api_key = request.headers.get('X-Parse-REST-API-Key')
    if api_key != API_KEY:
        return "ERROR", 403

    # Validar el JWT
    jwt_token = request.headers.get('X-JWT-KWY')
    if not jwt_token:
        return "ERROR: JWT missing", 401

    try:
        decoded_jwt = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
        # Aquí puedes hacer cualquier validación adicional con el contenido del JWT
    except jwt.InvalidTokenError:
        return "ERROR: Invalid JWT", 401

    # Procesar el JSON de entrada
    if request.is_json:
        data = request.get_json()
        message = data.get('message')
        to = data.get('to')
        from_ = data.get('from')
        time_to_life_sec = data.get('timeToLifeSec')

        # Validar que todos los campos están presentes
        if message and to and from_ and time_to_life_sec:
            # Generar la respuesta
            response_message = f"Hello {to}, your message will be send"
            return jsonify({"message": response_message}), 200
        else:
            return "ERROR: Missing fields in the JSON payload", 400
    else:
        return "ERROR: Invalid JSON", 400

@routes.route('/DevOps', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def devops_invalid_method():
    return "ERROR", 405
