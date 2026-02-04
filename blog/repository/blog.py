from fastapi import HTTPException,status, Response
from sqlalchemy.orm import Session
from .. import models
from ..import schemas
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db: Session):
    new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db: Session):
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

def update(id:int,request:schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f" kayıtlı {id}'li blog id bulunamadı"}
        # alternatif exceptıonlu olanı
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
    return blog

