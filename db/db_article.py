# Third Party
from sqlalchemy.orm.session import Session
from fastapi import HTTPException,status

# Project Library
from schemas import ArticleBase
from db.models import DbArticle
from exception import StoryException

def create_article(db:Session,request:ArticleBase):
    if request.content.lower().startswith("once upon a time"):
        raise StoryException("No Story Please!!")
    new_article = DbArticle(
        title =request.title,
        content =request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_all_articles(db:Session):
    return db.query(DbArticle).all()

def get_article(db:Session,id:int):
    article = db.query(DbArticle).filter(DbArticle.id==id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with id {id} not found!")
    return article

# def update_user(db:Session,id:int,request:UserBase):
#     user = db.query(DbUser).filter(DbUser.id==id)
#     user.update({
#         DbUser.username : request.username,
#         DbUser.email : request.email,
#         DbUser.password : Hash.bcryptPwd(request.password)
#     })
#     db.commit()
#     return "Updated"

# def delete_user(db:Session,id:int):
#     user = db.query(DbUser).filter(DbUser.id==id).first()
#     db.delete(user)
#     db.commit()
#     return "User Deleted"