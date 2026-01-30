
from typing import Optional
from fastapi import FastAPI
# ilk string alanı yaz unut olarak alır sonrada id yaz blog/str  sonra blog/id yoksa blog/id eziyor strigi,,
#pydantic ile validasyon yapabiliriz. ve tip belirtebiliriz. ve fastapi otomatik olarak tip dönüşümü yapar.
app = FastAPI()
# yukardan aşşağıya doğru olur herşeyi dkkatli kullan.

# @app.get('/')
@app.get("/blog")
def index(limit=10,published : bool = True, sort: Optional[str] = None):
    
    if published:
        return {"data":f" {limit} published blogs from the db"}
    else:
        return {"data":f" {limit} blogs from the db"}



@app.get("/blog/unpublished")
def unpublished():
     return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}

# bu allta kalırsa yukardaki id li olan bunu ezıyor bunu yukkarı al
# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data":"all unpublished blogs"}
@app.get("/blog/{id}/comments")
def comments(id,limit=10):
    #fetch comments of blog with id =id
    # return limit
    return {"data":{"1","2"}}
