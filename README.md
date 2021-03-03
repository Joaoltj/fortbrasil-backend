# Desafio Fortbrasil - Backend

### Linguagem e Framework
* Python e Flask

#### Desafio  
* Desenvolver uma aplicação de gerenciamento de estabelecimentos.


### Subir servidor via docker
```
docker-compose up -d 
```
### Criar as tabelas no banco de dados

```
docker exec -ti backend_api sh -c "flask create_tables"
```
