from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str = "Let Give title"
    content: str
    comments:int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog:BlogModel,id:int,version:float=1):
    return {"data":blog,"id":id,"version":version}