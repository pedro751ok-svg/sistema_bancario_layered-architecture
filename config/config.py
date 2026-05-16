import os 
from dotenv import load_dotenv
load_dotenv()
class Keys_securit:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATA_BASE_URL = os.getenv("ENGINE_DB")
    ALGORITHM = os.getenv("ALGORITHMS" , "HS256")