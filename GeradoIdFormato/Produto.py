import copy 
class Produto:
    @staticmethod
    def formatar( nome ):
        return copy.copy(nome).replace(" ", "-").lower()