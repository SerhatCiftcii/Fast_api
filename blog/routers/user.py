
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..repository import user as user_repository
from .. import database, schemas

router = APIRouter(
    prefix="/user",
    tags=["users"]
)
@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User, db: Session = Depends(database.get_db)):
    # bu kısmı repositorye taşıyoruz!!!!!!!!!!!!!!!!!!
    # new_user=models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user_repository.create(request, db)

@router.get('/{id}',response_model=schemas.ShowUserWithBlogs, status_code=status.HTTP_200_OK)
def show_user(id: int, db: Session = Depends(database.get_db)):
    # bu kısmı repositorye taşıyoruz!!!!!!!!!!!!!!!!!!
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" kayıtlı {id}'li kullanıcı bulunamadı")
    # return user
    return user_repository.show(id, db)