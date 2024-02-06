from fastapi import APIRouter
from ..controllers import AnexoController 

router = APIRouter()

router.include_router(router=AnexoController.router)