# Third Party Library
from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
# Project Library
from db.db_article import ArticleBase
from db.database import get_db
from db import db_article
from schemas import ArticleBase, ArticleDisplay
# Standard Library
from typing import List
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Write
@router.post('/',response_model=ArticleDisplay)
def create_article(request:ArticleBase,db:Session=Depends(get_db)):
    return db_article.create_article(db,request)

# Read all
@router.get('/',response_model=List[ArticleDisplay])
def get_all_articles(db:Session=Depends(get_db)):
    return db_article.get_all_articles(db)

# Read One
@router.get('/{id}',response_model=ArticleDisplay)
def get_article(id:int,db:Session=Depends(get_db)):
    return db_article.get_article(db,id)

# Update User
# @router.put('/{id}/update')
# def update_user(id:int,request:UserBase,db:Session = Depends(get_db)):
#     return db_article.update_user(db,id,request)

# Delete One
# @router.delete('/{id}/delete')
# def delete_user(id:int,db:Session=Depends(get_db)):
#     return db_user.delete_user(db,id)

