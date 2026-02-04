from fastapi import FastAPI ,Depends, status , Response ,HTTPException

from .import schemas
from . import schemas, models 
# from .database import engine ,SessionLocal
from .database import engine, get_db # databsaete taşıdık
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import blog, user



app=FastAPI()
models.Base.metadata.create_all(engine)# tabloları oluşturur otomatik migrations yapıyor
app.include_router(blog.router)
app.include_router(user.router)

#databsaete taşııdık 
# def get_db():
#     db= SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/blog",status_code=status.HTTP_201_CREATED,tags=["blogs"])
# def create(request: schemas.Blog, db : Session = Depends(get_db)):
#     new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
# def delete_blog(id: int, db: Session = Depends(get_db)):
#     deleted_rows = (
#         db.query(models.Blog)
#         .filter(models.Blog.id == id)
#         .delete(synchronize_session=False)
#     )

#     if deleted_rows == 0:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"{id} id'li blog bulunamadı"
#         )

#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
# #udpate
# def update(id,request:schemas.Blog, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li blog id bulunamadı")
#     blog.update({'title':request.title,'body':request.body})
#     db.commit()
#     return 'updated'


# bunuda router altındaki bloga taşııdk
# @app.get("/blog",response_model=list[schemas.ShowBlog],tags=["blogs"])
# def all(db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


#response_model burda ne döndüreceğimizi belirtiyoruz
# @app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED,tags=["users"])
# def create_user(request:schemas.User, db: Session = Depends(get_db)):
   
#     new_user=models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUserWithBlogs, status_code=status.HTTP_200_OK,tags=["users"])
# def show_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li kullanıcı bulunamadı")
#     return user