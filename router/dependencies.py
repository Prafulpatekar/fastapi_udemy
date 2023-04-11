from fastapi import APIRouter,Depends
from fastapi.requests import Request
from custom_log import log

router = APIRouter(
    prefix='/dependencies',
    tags=['dependencies'],
    dependencies=[Depends(log)]
)


def convert_params(request:Request,separator:str):
    query = []
    for key,value in request.query_params.items():
        query.append(f"{key} {separator} {value}")
    return query
 
def convert_headers(request:Request,separator:str='--',query=Depends(convert_params)):
    out_headers = []
    for key,value in request.headers.items():
        out_headers.append(f"{key} {separator} {value}")
    return {
        "headers":out_headers,
        "queries":query
    }

@router.get('')
def get_items(test:str,headers=Depends(convert_headers)):
    return {
        "items":['a','b','c'],
        "headers":headers
    }

@router.post('/new')
def create_items(headers=Depends(convert_headers)):
    return {
        "items":'New item created',
        "headers":headers
    }

class Account:
    def __init__(self,name:str,email:str) -> None:
        self.name = name
        self.email = email
    
@router.post('/user')
def create_user(password:str,account:Account=Depends()):
    return {
        "name":account.name,
        "email":account.email
    }