#vai ajudar com os tokens
from flask import request,jsonify
from services.jwt_services import validar_token
from functools import wraps

def requer_token(function):
    @wraps(function)
    def decorated(*args , **kwargs):
        auth = request.headers.get("Authorization")
       
        if not auth:
            return jsonify({
                "erro":"token não enviado"
            }),401
        try:
            token = auth.split(" ")[1]
        except:
            return jsonify({
                "erro":"token invalido"
            }),401
        payload = validar_token(token)

        if not payload:
            return jsonify({"erro":"token invalido ou expirado"}),401
        
        request.cliente_id = payload["id"]

        return function(*args , **kwargs)
    return decorated