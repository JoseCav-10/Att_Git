class Cliente():
    def __init__(self, pais, datacadastro, id):
        self._id = id
        self.pais = pais
        self.__datacadastro = datacadastro

    def getdatacadastro(self):
        return self.__datacadastro
    
    def setdatacadastro(self, data):
        self.__datacadastro = data