from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..database import db
from ..database.models import User
from ..schemas import UserCreate

router = APIRouter()

@router.post("/register/", response_model=User)
def register_user(user_data: UserCreate, db: Session = Depends(db.get_db)):
    # Перевірка, чи користувач з таким email вже існує
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    
    # Створення нового користувача
    new_user = User(email=user_data.email)
    new_user.set_password(user_data.password)  # Встановлення хешованого пароля
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
