# Third Party Library
from fastapi import FastAPI,Request,status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Project Library
from router import blog_get,blog_post,user,article,product
from auth import authentication
from db import models
from db.database import engine
from exception import StoryException

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.exception_handler(StoryException)
def story_exception_handler(request:Request,exc:StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={
            "detail":exc.name
        }
    )

models.Base.metadata.create_all(engine)

# Adding CORS Middleware Setting
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
 
