from pydantic import BaseModel, PastDatetime

class BlogBase(BaseModel):
    title: str
    content: str
    
    class Config():
        from_attributes = True


class BlogCreate(BlogBase): 
    publisher_id: int 


class UserBase(BaseModel):
    name: str
    username: str
    email: str

class DisplayBlog(BaseModel):
    id : int
    title: str
    content : str
    date_time: PastDatetime
    publisher: UserBase
    
    class Config():
       from_attributes =  True

class Blog(BlogBase):
    id: int
    date_time: PastDatetime
    publisher_id: int

    class Config():
       from_attributes =  True

