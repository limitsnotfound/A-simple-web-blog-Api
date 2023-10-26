from pydantic import BaseModel, PastDatetime
from typing import List

class UserBase(BaseModel):
    name: str
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserCreate):
    pass

class DisplayBlog(BaseModel):
    title: str
    content : str
    date_time: PastDatetime

class DisplayUser(UserBase):
    blogs: List[DisplayBlog] = []
     
    class Config:
        from_attributes = True


class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True
