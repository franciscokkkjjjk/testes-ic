from fastapi import APIRouter

router = APIRouter(
    prefix='/anexo'
)

@router.get('/download')
async def downloadAnexo():
    return {'ola': None}