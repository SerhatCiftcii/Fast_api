from fastapi import FastAPI ,Depends, status , Response ,HTTPException

from .import schemas
from . import schemas, models
from .database import engine ,SessionLocal
from sqlalchemy.orm import Session



app=FastAPI()
models.Base.metadata.create_all(engine)
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog= models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    deleted_rows = (
        db.query(models.Blog)
        .filter(models.Blog.id == id)
        .delete(synchronize_session=False)
    )

    if deleted_rows == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{id} id'li blog bulunamadı"
        )

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
#udpate
def update(id,request:schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'

@app.get("/blog")
def all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def show(id: int, response:Response,   db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f" kayıtlı {id}'li blog id bulunamadı"}
        # alternatif exceptıonlu olanı
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
    return blog