import bcrypt

class validar_cpf:
    @staticmethod
    def calcular_cpf(cpf,peso):
        soma = 0 
        for i in range(peso):
            soma += int(cpf[i]) * (peso + 1 - i)
        resto = soma %11
        return 0 if resto < 2 else 11 - resto 
    @staticmethod
    def validar_cpf(cpf):
        cpf = "". join(filter(str.isdigit,cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        digit1 = validar_cpf.calcular_cpf(cpf,9)
        digit2 = validar_cpf.calcular_cpf(cpf,10)
        return cpf [-2:] == f"{digit1}{digit2}"
class senha_segura:
    @staticmethod
    def senha_hash(senha_digitada):
        senha =  senha_digitada.encode("Utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha,salt)
    @staticmethod
    def verificar_senha(senha_digitada,senha_hash):
        senha = senha_digitada.encode("utf-8")
        if isinstance(senha_hash,str):
            senha_hash = senha_hash.encode("utf-8")
        return bcrypt.checkpw(senha,senha_hash)
    
