from fastapi import APIRouter,Query,Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    comments:int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog:BlogModel,id:int,version:int=1):
    return {"data":blog,"id":id,"version":version}


@router.post('/new/{id}/comment')
def create_comment(
        blog:BlogModel,
        id:int,
        comment_id:int=Query(None),
        title='Id for comment',
        description="Some description",
        alias="commentId",
        deprecated=False,
        content:str=Body(
                ...,
                min_length=5,
                max_length=40,
                regex='^[a-z\s]*$'
                )
        ):
    return {"blog":blog,"id":id,"comment_id":comment_id,"content":content}

def required_func():
    return {"message":"Auth function"}