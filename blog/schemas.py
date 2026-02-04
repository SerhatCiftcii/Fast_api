from pydantic import BaseModel, ConfigDict
from typing import List

class BlogBase(BaseModel):
    title:str
    body:str
 
class Blog(BlogBase):
    model_config = ConfigDict(from_attributes=True)

class ShowUser(BaseModel):
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    model_config = ConfigDict(from_attributes=True)    

#N+1İ ÖNEMLEMK İÇİN AYRI BİR ŞEMA OLUŞTURDUK ÖNCEDEN Showblogdada croter user varda .all dediğimizde karmakarışık oluyordu
class BlogSimple(BaseModel):
    title:str
    body:str
    model_config = ConfigDict(from_attributes=True)

class ShowUserWithBlogs(BaseModel):
    name:str
    email:str
    blogs:list[BlogSimple]
    model_config = ConfigDict(from_attributes=True)


