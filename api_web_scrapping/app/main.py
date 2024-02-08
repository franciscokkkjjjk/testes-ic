"""
# oq pode ser feito em relação a organização do projeto?
- [] criar um projeto para cada um dos topicos
- [X] criar um projeto apenas para o topico 1 e 2. E criar projetos separados para os topicos 3 e 4
# como vai ser feito para armazenar os arquivos?
- /app/arquivos/ 

## Organização de arquivos
rotas: unificação das rotas
models: Onde serão armazenados as classes do projeto
Conrollers: definição de uma rota por arquivo com sua função 

"""

from fastapi import FastAPI
from rotas import anexo

app = FastAPI()

app.include_router(router=anexo.router)

