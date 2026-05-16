from flask import Flask
from routes.rotas import rota
app = Flask(__name__)

app.register_blueprint(rota)
if __name__ == "__main__":
    app.run(debug=True)