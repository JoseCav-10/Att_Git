from .index import *

class PessoaFisica(Cliente):
    def __init__(self, nome, sobrenome, cpf, pais, datacadastro, id):
        super().__init__(pais, datacadastro, id)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def falar(self):
        print("Oi, my name is ", self.nome)
