from fastapi import FastAPI,status,Response
from enum import Enum
app = FastAPI()

@app.get('/hello')
def index():
    return {"message":"Hello World!"}

@app.post('/hello')
def index2():
    return "Hi!"

# Path parameters
@app.get('/blog/all')
def blog():
    return {"message":"All Blogs provided!"}

class BlogType(str , Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type:BlogType):
    return {"message":f"Blog type {type}"}

@app.get('/blog/{id}')
def blog(id:int,response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Erro Blog with id {id} not found"}
    response.status_code =status.HTTP_200_OK
    return {"message":f"Blog with id {id}"}

# Predefined value with ENUM
# command to run 
# if myApp = FastAPI()
# then => uvicorn main:myApp --reload
# => uvicorn main:app --reload