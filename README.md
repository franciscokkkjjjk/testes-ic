# testes-ic

## Frameworks utilizados no servidor python
+ [FastApi](https://fastapi.tiangolo.com/)
+ [Uvicorn](https://www.uvicorn.org/)
+ [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
+ [Pandas](https://pandas.pydata.org/docs/user_guide/)
+ [tabula-py](https://tabula-py.readthedocs.io/en/latest/) - esse framework depende do java, então é necessário que ele esteja instalado.

## instalação
### Backend
```
    cd api_web_scrapping
    pip install -r requirements.txt
```
### Frontend
```
    cd teste_api_vue
    npm install
```
## start backend
```
    cd api_web_scrapping/app
    uvicorn main:app --reload
```

## start frontend
```
    npm run dev
```

## Estrutura de arquivos do servidor python
```
/app: Código-fonte do aplicativo.

/app/assets - arquivos utilizados no código.

/app/controllers: - Definição e funções de rotas.

/app/funcoes: - Funções auxiliares.

/app/models: - Classes do aplicativo.

/app/rotas: - Unificação de rotas de diferentes arquivos de controllers antes de serem passadas para o arquivo main.

/app/uploads - Arquivos baixados durante a execução do código, podendo variar. 
```

## Rotas do servidor python 
```
/anexos/download - Responsável pela seção 1 do documento.

/anexo/extrairTabelas - Responsável pela seção 2 do documento.

/pesquisa/ - Responsável pela busca textual do item 4.2. 
```
