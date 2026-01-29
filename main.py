
from fastapi import FastAPI

app = FastAPI()
# yukardan aşşağıya doğru olur herşeyi dkkatli kullan.
@app.get('/')
def index():
    return {"data":"blog list"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}
@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments of blog with id =id
    return {"data":{"1","2"}}