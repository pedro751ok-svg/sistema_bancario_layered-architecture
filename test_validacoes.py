import pytest 
from utils.regras_auxiliares import validar_cpf,senha_segura

def test_cpf_valido():
    assert validar_cpf.validar_cpf("12345678909") == True
    assert validar_cpf.validar_cpf("55326653893") == True
def test_cpf_invalido():
    assert validar_cpf.validar_cpf("00000000000") == False
    assert validar_cpf.validar_cpf("123456789091") == False

def test_hash_gerado():
    senha = "pepe199291"
    assert senha_segura.senha_hash(senha) is not None
def test_verificar_senha():
    senha= "pepe199291"
    hash_gerado = senha_segura.senha_hash(senha)
    assert senha_segura.verificar_senha(senha,hash_gerado) == True