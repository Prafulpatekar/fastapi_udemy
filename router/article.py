# Third Party Library
from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session

# Project Library
from db.db_article import ArticleBase
from db.database import get_db
from db import db_article
from schemas import ArticleBase, ArticleDisplay,UserBase
from auth.oauth2 import oauth2_schema,get_session_user

# Standard Library
from typing import List
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Write
@router.post('/',response_model=ArticleDisplay)
def create_article(request:ArticleBase,db:Session=Depends(get_db),session_user:UserBase=Depends(get_session_user)):
    return db_article.create_article(db,request)

# Read all
@router.get('/',response_model=List[ArticleDisplay])
def get_all_articles(db:Session=Depends(get_db),session_user:UserBase=Depends(get_session_user)):
    return db_article.get_all_articles(db)

# Read One
# @router.get('/{id}',response_model=ArticleDisplay)
# def get_article(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_schema)):
#     return db_article.get_article(db,id)

# Read One
@router.get('/{id}')#,response_model=ArticleDisplay)
def get_article(id:int,db:Session=Depends(get_db),session_user:UserBase=Depends(get_session_user)):
    return {
        'data':db_article.get_article(db,id),
        'user':session_user 
    }
