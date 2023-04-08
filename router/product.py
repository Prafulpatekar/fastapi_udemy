# Third Party Library
from fastapi import  Cookie, APIRouter,Header,Form
from fastapi.responses import Response
from fastapi.background import BackgroundTasks
# Standard Library
from typing import List,Optional
import time
# Project Library
from custom_log import log

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['Laptop','Mobile','Mouse']


async def time_consuming_func():
    time.sleep(10)
    return "Complete"

@router.get('/all')
async def get_all_product():
    log("Product API","Call to get all products")
    await time_consuming_func()
    data = " ".join(products)
    response = Response(content=data,media_type='text/plain')
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
def create_product(bt: BackgroundTasks,name:str=Form(...)):
    bt.add_task(log_background_task,f"Calling create product {time.time()}")
    products.append(name)
    return products

def log_background_task(message:str):
    log("Product API",message)