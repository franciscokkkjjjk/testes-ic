# testes-ic

## instalação
### Backend
```
    cd api_web_scrapping
    pip install -r requirements.txt
```
### start backend
```
    cd api_web_scrapping/app
    uvicorn main:app --reload
```

## Estrutura de arquivos implementada até agora
```
/app: Código-fonte do aplicativo.

/app/controllers: Definição e funções de rotas.

/app/funcoes: Funções auxiliares.

/app/models: Classes do aplicativo.

/app/rotas: Unificação de rotas de diferentes arquivos de controllers antes de serem passadas para o arquivo main.
```
