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
/app - Armazena o código-fonte

/app/controllers - Armazena funções que cada rota irá assumir e a define

/app/funcoes - Armazena funções auxiliares utilizadas em todo o aplicativo ou em uma parte específica

/app/models - Armazena classes

/app/rotas - Unifica rotas antes de passá-las para o main vindas de múltiplos arquivos de controllers
```
