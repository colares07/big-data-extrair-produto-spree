from GeradoIdFormato.Id import Id
from GeradoIdFormato.Produto import Produto
from GeradoIdFormato.Horario import Horario
from GeradoIdFormato.NumeroAleatorio import NumeroAleatorio

class Gerador:

    @staticmethod
    def id(id, produto):
        return Id.formatar(id) + '|' + Produto.formatar(produto) +'|'+ Horario.obter() +'|'+ NumeroAleatorio.obter()

    def __init__(self, id, produto):
        self.id = Id.formatar(id)
        self.produto = Produto.formatar(produto)
        self.data =  Horario.obter()
        self.aleatorio = NumeroAleatorio.obter()

    def getId(self):
        return self.id

    def getProduto(self):
        return self.produto

    def getData(self):
        return self.data

    def getAleatorio(self):
        return self.aleatorio

    def getIdFormatado(self):
        return self.id + '|' + self.produto +'|'+ self.data +'|'+ self.aleatorio
