#regras de entrada e saida
from flask import Flask,request,jsonify
from services.conta_service import Authenticarservice,Contaservice,Transacoes
from services.jwt_services import gerar_token
class Authcontroler:
    @staticmethod
    def cadastrar():
        try:
            dados = request.get_json()

            nome = dados.get("nome")
            idade = dados.get("idade")
            cpf = dados.get("cpf")
            senha = dados.get("senha")

            cliente = Authenticarservice.cadastrar(
                nome,
                idade,
                cpf,
                senha
            )
            if isinstance(cliente,str):
                return jsonify({"erro":"erro ao tentar cadastrar cliente "}),500
            return jsonify({"CONCLUIDO":"CLIENTE CRIADO COM SUCESSO"})
        except Exception as erro:
            return f"ERRO AO TENTEAR CADASTRAR{erro}"
    @staticmethod
    def login():
        dados = request.get_json()

        cpf = dados.get("cpf")
        senha = dados.get("senha")

        cliente = Authenticarservice.fazer_login(
            cpf,
            senha

        )
        if isinstance(cliente,str):
            return jsonify({"erro":"cliente não existe"}),401
        if not cliente:
            return jsonify({"erro":"cliente nao encontrado"}),404

        token = gerar_token(cliente.id)
        return jsonify({"SUCESSO":"login feito com sucesso",
                        "token":token})
    @staticmethod
    def buscar_cliente(cliente_id):
        resultado_busca = Authenticarservice.buscar_cliente(
            cliente_id
        )
        if isinstance(resultado_busca,str):
            return jsonify({"resultado":"cliente nao encontrado"}),404
        if not resultado_busca:
            return jsonify({"erro":"cliente ainda nao foi criado"}),401

        return jsonify({"id":resultado_busca.id,
                        "cpf":resultado_busca.cpf})
    @staticmethod
    def depositar():

        dados = request.get_json()

        conta_id = dados.get("conta_id")
        valor = dados.get("valor")

        resultado = Contaservice.depositar(
            conta_id,
            valor
        )

        return jsonify({"resultado":resultado}),200
    @staticmethod
    def sacar():
        dados = request.get_json()

        conta_id = dados.get("conta_id")
        valor = dados.get("valor")

        resultado = Contaservice.sacar(
            conta_id,
            valor
        )

        return jsonify({"resultado":resultado}),200
    @staticmethod
    def ver_saldo(conta_id):

        resultado  =Contaservice.ver_saldo(
           conta_id
        
        )

        if isinstance(resultado,str):
            return jsonify({"erro":"cliente nao encontrado"}),404

        return jsonify({"resultado":resultado})
    @staticmethod
    def buscar_conta(conta_id):

        resultado_busca = Contaservice.buscar_conta(
            conta_id
        )
        if isinstance(resultado_busca,str):
            return jsonify({"erro":"conta não encontrada"}),404
        if not resultado_busca:
            return jsonify({"resultado":"conta nao existe"}),401

        return jsonify ({"id":resultado_busca.id,
                         "saldo":float(resultado_busca.saldo),
                         "limite":float(resultado_busca.limite)})
class Transacao_controller:    
    @staticmethod
    def transferir():
        dados = request.get_json()

        valor = dados.get("valor")
        conta_destino = dados.get("conta_destino")

        cliente_id = request.cliente_id
        resultado = Transacoes.transacao(
            conta_origem=cliente_id,
            valor=valor,
            conta_destino=conta_destino
        )
        if isinstance(resultado,str):
            return jsonify({"erro":f"{resultado}"}),400
        if not resultado:
            return jsonify({"erro":"erro contao nao existe "}),401
        return jsonify({"sucesso":"tranferencia realizada com sucesso"})