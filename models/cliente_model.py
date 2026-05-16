from sqlalchemy import create_engine,String,Numeric,Integer,ForeignKey,Column,LargeBinary,DateTime
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
from config.config import Keys_securit
from datetime import datetime
engine = create_engine(Keys_securit.DATA_BASE_URL)
Base = declarative_base()
session = sessionmaker(bind=engine)

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer,primary_key=True)
    nome = Column(String(30),nullable=False)
    idade = Column(Integer,nullable=False)
    cpf = Column(String(11),nullable=False,unique=True)
    senha = Column(LargeBinary,nullable=False)
    conta = relationship("Conta", back_populates= "cliente")
class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer,primary_key=True)
    saldo = Column(Numeric(10,2),nullable=False,default=0)
    limite = Column(Numeric(10,2),nullable=False,default=0)
    cliente_id = Column(Integer,ForeignKey("cliente.id"))
    nivel = Column(Integer,default=0)
    cliente = relationship("Cliente", back_populates= "conta")
    transacoes_enviadas = relationship("Transacao",foreign_keys="Transacao.conta_origem_id")
    transacoes_recebidas = relationship("Transacao",foreign_keys="Transacao.conta_destino_id")
class Transacao(Base):
    __tablename__ = "transacao"
    id = Column(Integer,primary_key=True)
    conta_origem_id = Column(Integer,ForeignKey("conta.id"),nullable=False)
    conta_destino_id = Column(Integer,ForeignKey("conta.id"),nullable=False)
    valor = Column(Numeric(10,2),nullable=False)
    data = Column(DateTime,default=datetime.utcnow)

    conta_origem = relationship("Conta",foreign_keys=[conta_origem_id])
    conta_destino = relationship("Conta",foreign_keys=[conta_destino_id])
Base.metadata.create_all(engine)