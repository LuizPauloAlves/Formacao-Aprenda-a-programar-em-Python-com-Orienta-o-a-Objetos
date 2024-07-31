# o class Livro é um exemplo para o class Pessoa
class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'''Nome: {self._nome}
            Idade: {self._idade}
            Profissão: {self._profissao}'''

    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        return f'Bem vindo {self._nome}, o melhor profissional de {self._profissao} com {self._idade}' if self._profissao else  f'Bem vindo {self._nome}'

joao = Pessoa('Joao', 20, 'TI')
print(joao)
joao.aniversario()
print(joao.saudacao)

#1
class ContaBancaria:
    def __init__(self, titular = '', saldo = 0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False


#2
    def __str__(self):
        return f'''Titular: {self.titular}
            Saldo: {self._saldo}
            Status: {self._ativo}'''

#3
    def ativar_conta(self):
        self._ativo = not self._ativo


#4
class ContaBancariaPythonica:
    def __init__(self, titular = '', saldo = 0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
#5
conta = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta: {conta.titular}")

#6
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
#7
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")