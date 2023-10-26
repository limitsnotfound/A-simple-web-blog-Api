from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from schemas.user_schema import UserCreate, UserBase, DisplayUser
from database import get_db
from passlib .context import CryptContext
from services import user_service

router = APIRouter()

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/{username}", response_model=DisplayUser)
def get_user(username: str, db: Session = Depends(get_db)):
    return user_service.get_by_username(username, db)


@router.post("/", status_code=status.HTTP_200_OK)
def create_user(form:UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(form, db)
