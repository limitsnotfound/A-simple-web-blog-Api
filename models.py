import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates="publisher")


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key= True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    publisher_id = Column(Integer, ForeignKey("users.id"))

    publisher = relationship("User", back_populates="blogs")

