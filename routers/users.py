from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['User requests'])

@router.get()