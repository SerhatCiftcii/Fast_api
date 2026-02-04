from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas ,database,models# .. nokta ile üst dizine çıkıyoruz
from sqlalchemy.orm import Session
from ..repository import blog  as blog_repository
router = APIRouter(
prefix="/blog",
tags=["blogs"]
)

@router.get("/",response_model=list[schemas.ShowBlog])
def all(db : Session = Depends(database.get_db)):
    #bu kısmı repositorye taşıyoruz!!!!!!!!!!!!!!!!!!
    # blogs = db.query(models.Blog).all()
    # return blogs

    return blog_repository.get_all(db)

# @router.post("/blog",status_code=status.HTTP_201_CREATED,tags=["blogs"]) tags tanımalamsını yukarda yapıyoruz şimdi tek tek yazmaya gerek yok
@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(database.get_db)):
    return blog_repository.create(request, db)
    
    # bu kısmı repositorye taşıyoruz!!!!!!!!!!!!!!!!!!
    # new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response:Response,   db : Session = Depends(database.get_db)):
    # bu kısmı repositorye taşıyoruz!!!!!!!!!!!!!!!!!!
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {"detail": f" kayıtlı {id}'li blog id bulunamadı"}
    #     # alternatif exceptıonlu olanı
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
    # return blog
    return blog_repository.show(id, db)



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    return blog_repository.destroy(id, db)
    # deleted_rows = (
    #     db.query(models.Blog)
    #     .filter(models.Blog.id == id)
    #     .delete(synchronize_session=False)
    # )

    # if deleted_rows == 0:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"{id} id'li blog bulunamadı"
    #     )

    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
#udpate
def update(id:int,request:schemas.Blog, db : Session = Depends(database.get_db)):
    return blog_repository.update(id,request, db)
    
