from fastapi import APIRouter
from controllers import anexo, extrairTabelas 

router = APIRouter()

router.include_router(router=anexo.routerAX, prefix='/anexo')
router.include_router(router=extrairTabelas.routerED, prefix='/anexo')