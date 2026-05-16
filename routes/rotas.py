from flask import Blueprint
from controllers.autenticacao_controler import Authcontroler,Transacao_controller
from middleware.autenticacao_middleware import requer_token
rota = Blueprint("rota",__name__)
#PRIMEIRA VEZ CRIANDO END POINTS 

@rota.route("/cadastro",methods = ["POST"])
def cadastrar():
    return Authcontroler.cadastrar()

@rota.route("/login",methods = ["POST"])

def login():
    return Authcontroler.login()

@rota.route("/buscar_cliente/<int:id>",methods = ["GET"])
@requer_token
def buscar_cliente(id):
    return Authcontroler.buscar_cliente(id)

@rota.route("/depositar",methods = ["POST"])
@requer_token
def depositar():
    return Authcontroler.depositar()

@rota.route("/sacar", methods = ["POST"])
@requer_token
def sacar():
    return Authcontroler.sacar()

@rota.route("/ver_saldo/<int:id>",methods = ["GET"])
@requer_token
def ver_saldo(id):
    return Authcontroler.ver_saldo(id)

@rota.route("/buscar_conta/<int:id>",methods = ["GET"])
@requer_token
def buscar_conta(id):
    return Authcontroler.buscar_conta(id)

@rota.route("/transferir", methods = ["POST"])
@requer_token
def transferir():
    return Transacao_controller.transferir()
