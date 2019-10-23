# Docker compose de extração de dados 

Com objetivo obter os dados de produto disponivel atraves de [spreecommerce/spree](https://hub.docker.com/r/spreecommerce/spree) onde são armazenando do pymongo

## Começando


### Pré-requisitos

O que você precisa para executar, é necessario criar o arquivo de variavel de ambiente **"config.env"** com as seguintes informações:

```
API_TOKEN=TOKEN PELA APLICACAO SPREE 

```
Esse [**token**](http://localhost:3000/admin/users/1/edit) é obtido dentro da aplicação.

### Executando

Para executar o extrator será necessário baixar o projeto e com arquivo **"config.env"** no mesmo local.

Executar a aplicação

```
docker-compose up
```

Para a execução

```
docker-compose down
```


