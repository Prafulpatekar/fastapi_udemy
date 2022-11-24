from fastapi import FastAPI,status,Response
from enum import Enum
from typing import Optional
app = FastAPI()

# @app.get('/hello')
# def index():
#     return {"message":"Hello World!"}

# @app.post('/hello')
# def index2():
#     return "Hi!"

# Path parameters
@app.get(
    '/blog/all',
    tags=['blog'],
    summary="This retrives all blogs",
    description="This api call simulates all blog !"
    )
def blog():
    return {"message":"All Blogs provided!"}

class BlogType(str , Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}',tags=['blog'])
def get_blog_type(type:BlogType):
    return {"message":f"Blog type {type}"}

@app.get('/blog/{id}',tags=['blog'])
def blog(id:int,response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Erro Blog with id {id} not found"}
    response.status_code =status.HTTP_200_OK
    return {"message":f"Blog with id {id}"}

@app.get('/blog/all/query_parameters',tags=['blog'])
def get_all_blog_query_parameters(response:Response,page=1,page_size:Optional[int]=None):
    response.status_code =status.HTTP_200_OK
    return {"message":f"Blog page no. {page} on page size {page_size}"}

@app.get('/blog/{id}/comments/{comment_id}',tags=['blog','comment'])
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

# Predefined value with ENUM
# command to run 
# if myApp = FastAPI()
# then => uvicorn main:myApp --reload
# => uvicorn main:app --reload