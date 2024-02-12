from fastapi import APIRouter
from controllers import downloadAnexo, extrairTabelas 

routerAnexo = APIRouter()
prefixo = '/anexo'
prefixo_plural = '/anexos'
routerAnexo.include_router(router=downloadAnexo.routerDW, prefix=prefixo_plural)
routerAnexo.include_router(router=extrairTabelas.routerED, prefix=prefixo)