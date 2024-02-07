from fastapi import APIRouter
from controllers import anexo 

router = APIRouter()

router.include_router(router=anexo.router)