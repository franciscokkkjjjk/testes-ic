from fastapi import APIRouter
from controllers.buscaDados import routerBD

routerPesquisa = APIRouter()

routerPesquisa.include_router(routerBD, prefix='/pesquisa')