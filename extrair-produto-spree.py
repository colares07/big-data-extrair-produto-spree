import os
from ApiSpree import ApiSpree
from Banco import BancoDado
from GeradoIdFormato.Gerador import Gerador

CAMPO_ID = 'id'
CAMPO_NOME = 'name'

DATABASE = "EP1"
COLLECTION = "produtos"

API_TOKEN = os.environ['API_TOKEN']

bd = BancoDado(database=DATABASE, host="database")
apiSpree = ApiSpree(token=API_TOKEN, url='http://spree:3000')

listaProdutos = apiSpree.getListaProduto()

for registro in listaProdutos:
    gerador = Gerador(id=registro[CAMPO_ID], produto=registro[CAMPO_NOME])
    json = {
       #"_id" : Gerador.id(id=registro[CAMPO_ID], produto=registro[CAMPO_NOME]),
        '_id' : gerador.getIdFormatado(),
        'id' : registro[CAMPO_ID],
        'produto' : gerador.getProduto(),
        'data' : gerador.getData(),
        'aleatorio' : gerador.getAleatorio(),
        'metadados' : registro
    }
    print(bd.add(collection=COLLECTION, json=json))
