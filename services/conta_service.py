from models.cliente_model import Conta
from models.cliente_model import Cliente
from models.cliente_model import session
from utils.regras_auxiliares import regras_nedocio_auxiliares
from models.cliente_model import Transacao
class Authenticarservice:

    @staticmethod
    def cadastrar(nome,idade,cpf,senha):
        if not regras_nedocio_auxiliares.validar_cpf(cpf):
            return "CPF invalido"
        
        with session() as sessao:
            cpf_existennte = sessao.query(Cliente).filter_by(cpf=cpf).first()
            if cpf_existennte:
                return "cliente ja cadastrado"
            
            senha_1 = regras_nedocio_auxiliares.senha_hash(senha)
            cliente = Cliente(
            nome=nome,
            idade=idade,
            cpf=cpf,
            senha=senha_1
        )
            sessao.add(cliente)
            sessao.flush()

            conta = Conta(
              cliente_id=cliente.id
            )
            sessao.add(conta)
            sessao.commit()
        return cliente

    @staticmethod
    def fazer_login(cpf,senha):
        with session() as sessao:
            cliente = sessao.query(Cliente).filter_by(cpf=cpf).first()
 
            if not cliente:
                return "cliente nao encontrado ou nao criado ainda "
            senha_valida = regras_nedocio_auxiliares.verificar_senha(senha,cliente.senha)
            if not senha_valida:
                return "senha invalida"
            return cliente
    @staticmethod
    def buscar_cliente(cliente_id):
        with session() as sessao:
            cliente = sessao.query(Cliente).filter_by(id=cliente_id).first()
            if not cliente:
                return "cliente não encontrado"
            return cliente
class Contaservice:
    @staticmethod
    def sacar(conta_id,valor):
        with session() as sessao:
            conta = sessao.query(Conta).filter_by(id=conta_id).first()
            if not conta:
                return "conta nao encontrada"
            if valor <= 0:
                return "valor invalido"
            if conta.saldo + conta.limite < valor:
                return "saldo insuficiente"
            conta.saldo -= valor
            sessao.commit()
            return "saque realizado com sucesso"
    @staticmethod
    def depositar(conta_id,valor):
        with session() as sessao:
            conta = sessao.query(Conta).filter_by(id=conta_id).first()
            if not conta:
                return "conta nao encotrada"
            if valor <= 0:
                return "valor invalido "
            conta.saldo += valor

            sessao.commit()
        return "deposito realizado com sucesso"
    @staticmethod
    def ver_saldo(conta_id):
        with session() as sessao:
            conta = sessao.query(Conta).filter_by(id  = conta_id).first()
            if not conta:
                return "conta ainda nao existe "
            return conta.saldo,conta.limite

    @staticmethod
    def buscar_conta(conta_id):
        with session() as sessao:
            conta = sessao.query(Conta).filter_by(id=conta_id).first()
            if not conta:
                return "conta nao encontrada"
            return conta
class Transacoes:
    @staticmethod
    def transacao(conta_origem,conta_destino,valor):
        with session() as sessao:
            conta_origem = sessao.query(Conta).filter_by(id=conta_origem).first()
            conta_destino = sessao.query(Conta).filter_by(id=conta_destino).first()

            if not conta_origem:
                return "connta origem nao existe"
            if not conta_destino:
                return "conta destino nao existe "
            if conta_origem ==conta_destino:
                return "n foi possivel finalizar a trasaçção pois você esta tentando mandar dinheiro para si mesmo "
            if conta_origem.saldo + conta_origem.limite < valor:
                return "saldo insuficiente"
            
            conta_origem.saldo -= valor
            conta_destino.saldo += valor 

            transacao = Transacao(
                conta_origem_id= conta_origem.id,
                conta_destino_id= conta_destino.id,
                valor=valor
            )
            sessao.add(transacao)
            sessao.commit()
            return "tranferencia enviada com suceeso "
