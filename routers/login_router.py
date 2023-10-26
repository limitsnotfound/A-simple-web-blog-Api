from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session
import models
from hashing import Hash
from token_file import create_access_token

router = APIRouter()

@router.post("/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user =  db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "Invalid username")  
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "Invalid password")  
    
     
    access_token = create_access_token(data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}