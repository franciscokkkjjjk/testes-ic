from fastapi import APIRouter
from controllers import downloadAnexo, extrairTabelas, substituirNomeclaturaTabela 

router = APIRouter()
prefixo = '/anexo'
router.include_router(router=downloadAnexo.routerDW, prefix=prefixo)
router.include_router(router=extrairTabelas.routerED, prefix=prefixo)
router.include_router(router=substituirNomeclaturaTabela.routerSNT, prefix=prefixo)