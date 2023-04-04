# Third Party Library
from fastapi import APIRouter,status,Response,Depends
# Standard Library
from enum import Enum
from typing import Optional
# Project Library
from .blog_post import required_func

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get(
    '/all',
    summary="This retrives all blogs",
    description="This api call simulates all blog !",
    response_description="The list of blog is available!"
    )
def blog():
    return {"message":"All Blogs provided!"}

class BlogType(str , Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type:BlogType):
    return {"message":f"Blog type {type}"}

@router.get('/{id}')
def blog(id:int,response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Erro Blog with id {id} not found"}
    response.status_code = status.HTTP_200_OK
    return {"message":f"Blog with id {id}"}

@router.get('/all/query_parameters')
def get_all_blog_query_parameters(response:Response,page=1,page_size:Optional[int]=None,req_params:dict=Depends(required_func)):
    response.status_code =status.HTTP_200_OK
    return {
        "message":f"Blog page no. {page} on page size {page_size}",
        "req":req_params
        }

@router.get('/{id}/comments/{comment_id}',tags=['comment'])
def get_comment(response:Response,id:int,comment_id:int,valid:bool=True,username:Optional[str]="Praful"):
    """
    Simulates retriveing a common blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    response.status_code = status.HTTP_200_OK
    return {"message":f"Blog id {id} comment {comment_id} valid {valid} username {username}"}

