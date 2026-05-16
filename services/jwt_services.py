import jwt
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
load_dotenv()
import os
from config.config import Keys_securit
SECRET_KEY = Keys_securit.SECRET_KEY

def gerar_token(cliente_id):
    payload = {
        "id":cliente_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(payload,SECRET_KEY,algorithm=Keys_securit.ALGORITHM)
    return token
def validar_token(token):
    
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[Keys_securit.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        
        return None
    except jwt.InvalidTokenError:
        
        return None