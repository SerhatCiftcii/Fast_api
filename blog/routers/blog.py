from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import blog as blog_repository

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", response_model=list[schemas.ShowBlog])
def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return blog_repository.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog_repository.create(request, db)

@router.get("/{id}", response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog_repository.show(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    return blog_repository.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog_repository.update(id, request, db)
