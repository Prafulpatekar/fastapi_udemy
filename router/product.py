# Third Party Library
from fastapi import  Cookie, APIRouter,Header,Form
from fastapi.responses import Response
# Standard Library
from typing import List,Optional

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['Laptop','Mobile','Mouse']

@router.get('/all')
def get_all_product():
    data = " ".join(products)
    response = Response(content=data,media_type='application/json')
    response.set_cookie(key='test_cookie',value="test_cookie_value")
    return response

# Make request from POSTMAN
@router.get('/withheader')
def get_product(
        response:Response,
        custom_header:Optional[List[str]]=Header(None),
        test_cookie:Optional[str]=Cookie(None)
        ):
    if custom_header:
        response.headers['custom_response_header'] = " ".join(custom_header)

    return {
        "data":products,
        "custom_header":custom_header,
        "test_cookie":test_cookie
    }

# FORM HANDLer
@router.post('/new')
def create_product(name:str=Form(...)):
    products.append(name)
    return products