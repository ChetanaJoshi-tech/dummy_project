# schemas.py
from pydantic import BaseModel
from typing import List

class PostBase(BaseModel):
    title: str
    content: str
    

class PostCreate(PostBase):
    pass
    owner_id: int
class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True
