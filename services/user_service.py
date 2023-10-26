from fastapi import HTTPException, status
import models
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate
from passlib .context import CryptContext
import hashing
from database import engine
from models import User
 

session = Session(bind=engine)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_by_username(username: str,  db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"User with id {id} is not found") 
    return user



def create_user(form:UserCreate ,db: Session):
    db_username=session.query(User).filter(User.username==form.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with username already exists")


    
    db_email=session.query(User).filter(User.email==form.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with email already exists")
    

    new_user = models.User(name = form.name, 
                           username = form.username, 
                           email = form.email,
                           password = hashing.Hash.bycrypt(form.password))
    
                           
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"Publisher Id" : new_user.id,
            "Name": form.name, 
            "Username" : form.username,
            "Email": form.email}