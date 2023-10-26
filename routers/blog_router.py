from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Response, HTTPException
from schemas.blog_schema import BlogCreate, BlogBase, DisplayBlog, Blog
from schemas.user_schema import User
from database import get_db
from typing import List
from services import blog_service
from oauth2 import get_current_user



router = APIRouter()


@router.get("/", response_model=List[DisplayBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    return blog_service.get_all(db)



@router.get ("/{id}", status_code=200, response_model=DisplayBlog)
def get_single_blog(id: int, db: Session = Depends(get_db)):
    return blog_service.get_by_id(id, db)
 

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(form: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blog_service.create_blog(form, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, form: BlogBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_service.update_blog(id, form, db)


 
@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog_service.delete_blog(id, db)